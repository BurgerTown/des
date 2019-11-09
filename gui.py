import tkinter as tk
import tkinter.messagebox
from des import DES


class Gui:
    def __init__(self):
        # 定義GUI界面
        window = tk.Tk()
        window.title('DES加解密應用程式')
        window.geometry('768x432')
        window.resizable(False, False)

        tk.Label(master=window, text='請在這裡輸入明文：').place(
            x=10, y=70, width=120, height=26)
        tk.Label(master=window, text='請在這裡輸入密鑰：').place(
            x=10, y=163, width=120, height=26)
        tk.Label(master=window, text='請在這裡輸入密文：').place(
            x=10, y=245, width=120, height=26)

        tk.Scrollbar()

        self.plain_text = tk.Text(master=window,
                                  highlightthickness=1.2,
                                  highlightbackground='#CCCCCC',
                                  highlightcolor='#A1CBF1',
                                  height=9, width=82)
        self.plain_text.place(x=140, y=30)

        self.key_text = tk.Entry(master=window, show='*')
        self.key_text.place(x=138, y=163, width=500, height=26)

        self.cypher_text = tk.Text(master=window,
                                   highlightthickness=1.2,
                                   highlightbackground='#CCCCCC',
                                   highlightcolor='#A1CBF1',
                                   height=9, width=82)
        self.cypher_text.place(x=140, y=203)

        self.display_or_not = tk.IntVar()

        encrypt_button = tk.Button(
            master=window, text='DES加密', width=50, height=30, command=self.des_en)
        encrypt_button.place(x=200, y=350, width=80, height=26)
        decrypt_button = tk.Button(
            master=window, text='DES解密', width=50, height=30, command=self.des_de)
        decrypt_button.place(x=500, y=350, width=80, height=26)
        encrypt_button = tk.Button(
            master=window, text='清空數據', width=50, height=30, command=self.des_clear)
        encrypt_button.place(x=200, y=390, width=80, height=26)
        decrypt_button = tk.Button(
            master=window, text='退出程式', width=50, height=30, command=self.des_exit)
        decrypt_button.place(x=500, y=390, width=80, height=26)
        password_display_selection = tk.Checkbutton(
            master=window, text='顯示密碼',
            variable=self.display_or_not,
            onvalue=1, offvalue=0,
            selectcolor="red",
            command=self.display_password)
        password_display_selection.place(x=640, y=163)

        self.window = window
        window.mainloop()

    def des_en(self):
        plain_text = self.plain_text.get(0.0, 'end').split('\n')[0]
        key_text = self.key_text.get()
        if len(plain_text) < 1:
            tk.messagebox.showerror(title=None, message='請輸入明文！！！')
            # TODO: 退去des_en()
        if len(key_text) < 1:
            tk.messagebox.showerror(title=None, message='請輸入密碼！！！')
            # TODO: 退出des_en()
        return_text = DES().encrypt(plain_text, key_text)
        self.plain_text.delete('1.0', 'end')
        self.cypher_text.delete('1.0', 'end')
        self.cypher_text.insert('end', return_text)
        self.window.clipboard_clear()
        self.window.clipboard_append(return_text)

    def des_de(self):
        cypher_text = self.cypher_text.get(0.0, 'end').split('\n')[0]
        key_text = self.key_text.get()
        if len(cypher_text) < 1:
            tk.messagebox.showerror(title=None, message='請輸入密文！！！')
            # TODO: 退去des_de()
        if len(key_text) < 1:
            tk.messagebox.showerror(title=None, message='請輸入密碼！！！')
            # TODO: 退出des_de()
        return_text = DES().decrypt(cypher_text, key_text).replace('\0', '')
        self.plain_text.delete('1.0', 'end')
        self.cypher_text.delete('1.0', 'end')
        self.plain_text.insert('end', return_text)
        self.window.clipboard_clear()
        self.window.clipboard_append(return_text)

    def des_clear(self):
        self.plain_text.delete('1.0', 'end')
        self.key_text.delete('0', 'end')
        self.cypher_text.delete('1.0', 'end')

    def des_exit(self):
        if tk.messagebox.askyesno(title='', message='你確定現在要退出本程式嗎？'):
            self.window.quit()

    def display_password(self):
        # TODO： 改變參數 （下面的代碼不可用）
        if self.display_or_not.get() == 1:
            self.key_text = tk.Entry(master=self.window, show=None)
            print('1')
        if self.display_or_not.get() == 0:
            self.key_text = tk.Entry(master=self.window, show='*')
            print('0')


if __name__ == '__main__':
    Gui()
