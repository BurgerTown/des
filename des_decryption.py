#_*_coding:utf-8_*_
'''
	解密
'''

from des_struct import *
import re

__all__=['desdecode']
class DES():
	def __init__(self):
		pass
	def decode(self,string,key,key_len,string_len):
		output=""
		trun_len=0
		num=0
		code_string=self._functionCharToA(string,string_len)
		code_key=self._getkey(key,key_len)
				
		
		#如果密鑰長度不是16的整數倍,則增加0使其變為16的整數倍
		real_len=(key_len/16)+1 if key_len%16!=0 else key_len/16
		trun_len=string_len*4

		for i in range(0,trun_len,64):
			run_code=code_string[i:i+64]
			run_key=code_key[num%real_len]

			#64位明文初始置換
			run_code= self._codefirstchange(run_code)
			
			#迭代16次
			for j in range(16):
				
				code_r=run_code[32:64]
				code_l=run_code[0:32]
				
				#64位左右交換	
				run_code=code_r
				
				#右邊32位擴展置換
				code_r= self._functionE(code_r)
				
				#獲取本輪子密鑰
				key_y=run_key[15-j]

				#異或
				code_r= self._codexor(code_r,key_y)
				
				#S盒代替選擇
				code_r= self._functionS(code_r)
				
				#P轉換
				code_r= self._functionP(code_r)
				
				#異或
				code_r= self._codexor(code_l,code_r)
				
				run_code+=code_r
			num+=1
			
			#32互換
			code_r=run_code[32:64]
			code_l=run_code[0:32]
			run_code=code_r+code_l
			
			#把二進制轉換為16進制、逆初始置換
			output+=self._functionCodeChange(run_code)
		return output
	
	#獲取子密鑰
	def _getkey(self,key,key_len):
		
		#把密鑰轉換為二進制
		code_key=self._functionCharToA(key,key_len)
		
		a=['']*16
		real_len=(key_len/16)*16+16 if key_len%16!=0 else key_len

		b=['']*(real_len/16)
		for i in range(real_len/16):
			b[i]=a[:]
		num=0
		trun_len=4*key_len
		for i in range(0,trun_len,64):
			run_key=code_key[i:i+64]
			run_key= self._keyfirstchange(run_key)
			for j in range(16):
				key_l=run_key[0:28]
				key_r=run_key[28:56]
				key_l=key_l[d[j]:28]+key_l[0:d[j]]
				key_r=key_r[d[j]:28]+key_r[0:d[j]]
				run_key=key_l+key_r
				key_y= self._functionKeySecondChange(run_key)
				b[num][j]=key_y[:]
			num+=1

		return b	
		
	#異或	 							
	def _codexor(self,code,key):
		code_len=len(key)
		return_list=''
		for i in range(code_len):
			if code[i]==key[i]:
				return_list+='0'
			else:
				return_list+='1'
		return return_list

	#密文或明文初始置換		 							
	def _codefirstchange(self,code):
		changed_code=''
		for i in range(64):
			changed_code+=code[ip[i]-1]
		return changed_code
		
	#密鑰初始置換
	def _keyfirstchange (self,key):
		changed_key=''
		for i in range(56):
			changed_key+=key[pc1[i]-1]
		return changed_key
	
	#逆初始置換
	def _functionCodeChange(self, code):
		return_list=''
		for i in range(16):
			list=''
			for j in range(4):
				list+=code[ip_1[i*4+j]-1]
			return_list+="%x" %int(list,2)
		return return_list
	
	#擴展置換	
	def _functionE(self,code):
		return_list=''
		for i in range(48):
			return_list+=code[e[i]-1]
		return return_list		
	
	#置換P	
	def _functionP(self,code):
		return_list=''
		for i in range(32):
			return_list+=code[p[i]-1]
		return return_list

	#S盒代替選擇置換	
	def _functionS(self, key):
		return_list=''
		for i in range(8):
			row=int( str(key[i*6])+str(key[i*6+5]),2)
			raw=int(str( key[i*6+1])+str(key[i*6+2])+str(key[i*6+3])+str(key[i*6+4]),2)
			return_list+=self._functionTos(s[i][row][raw],4)

		return return_list
	
	#密鑰置換選擇2
	def _functionKeySecondChange(self,key):
		return_list=''
		for i in range(48):
			return_list+=key[pc2[i]-1]
		return return_list
	
	#十六進制轉換為二進制
	def _functionCharToA(self,code,lens):
		return_code=''
		lens=lens%16
		for key in code:
			code_ord=int(key,16)
			return_code+=self._functionTos(code_ord,4)
		
		if lens!=0:
			return_code+='0'*(16-lens)*4
		return return_code
	
	#二進制轉換
	def _functionTos(self,o,lens):
		return_code=''
		for i in range(lens):
			return_code=str(o>>i &1)+return_code
		return return_code

#把unicode字符轉換為16進制
def tohex(string):
	return_string=''
	for i in string:
		return_string+="%02x"%ord(i)
	return return_string
		
def tounicode(string):
	return_string=''
	string_len=len(string)
	for i in range(0,string_len,2):
		return_string+=chr(int(string[i:i+2],16))
	return return_string
	

def desdecode(from_code,key):
	key=tohex(key)

	des=DES()
	
	key_len=len(key)
	string_len=len(from_code)
	if string_len%16!=0:
		return False
	if string_len<1 or key_len<1:
		return False

	key_code= des.decode(from_code,key,key_len,string_len)
	return tounicode(key_code)
	

if __name__  == '__main__':
	print("DES解密\n")
	c=raw_input("請輸入密文:")
	k=raw_input("請輸入密鑰:")
	print desdecode(c,k)
	k=raw_input("按任意鍵退出。。。")


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
