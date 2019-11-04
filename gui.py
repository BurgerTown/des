import tkinter as tk
import re

####定義GUI界面####
window = tk.Tk("")
window.title('DES加解密工具')
window.geometry('640x200')
window.resizable(False,False)

def des_en():
    pass

def des_de():
    pass

tk.Label(window,text='原文：').place(x=30,y=40,width=40,height=26)
tk.Label(window,text='密鑰：').place(x=30,y=100,width=40,height=26)

input = tk.Entry(window).place(x=80,y=40,width=500,height=26)
key = tk.Entry(window,show='*').place(x=80,y=100,width=500,height=26)

encrypt_Button = tk.Button(window,text='加密',width=50,height=30,command=des_en).place(x=160,y=150,width=60,height=26)
decrypt_Button = tk.Button(window,text='解密',width=50,height=30,command=des_de).place(x=400,y=150,width=60,height=26)

window.mainloop()