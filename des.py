from des_decrypt import DES_Decrypt


class DES:
    def __init__(self, *args, **kwargs):
        pass

    def decrypt(self, from_code, key):
        key = self._to_hex(key)
        des_encrypt = DES_Decrypt()
        key_len = len(key)
        string_len = len(from_code)
        if string_len % 16 != 0:
            return False
        if string_len < 1 or key_len < 1:
            return False
        key_code = des_encrypt.decode(from_code, key, key_len, string_len)
        return self._to_unicode(key_code)

        # 把unicode字符轉換為16進制
    def _to_hex(self, string):
        return_string = ''
        for i in string:
            return_string += "%02x" % ord(i)
        return return_string

    def _to_unicode(self, string):
        return_string = ''
        string_len = len(string)
        for i in range(0, string_len, 2):
            return_string += chr(int(string[i:i+2], 16))
        return return_string


if __name__ == '__main__':
    des = DES()
    print("DES解密\n")
    c = input("請輸入密文:")
    k = input("請輸入密鑰:")
    print(des.decrypt(c, k))
    input("按任意鍵退出。。。")
