import tkinter as tk
from des import DES


class Gui:
    def __init__(self, *args, **kwargs):
        # 定義GUI界面
        window = tk.Tk()
        window.title('DES加解密應用程式')
        window.geometry('768x432')
        window.resizable(False, False)

        tk.Label(window, text='請在這裡輸入明文：').place(
            x=10, y=70, width=120, height=26)
        tk.Label(window, text='請在這裡輸入密鑰：').place(
            x=10, y=163, width=120, height=26)
        tk.Label(window, text='請在這裡輸入密文：').place(
            x=10, y=245, width=120, height=26)

        self.plain_text = tk.Text(window,
                                  highlightthickness=1.2,
                                  highlightbackground='#CCCCCC',
                                  highlightcolor='#A1CBF1',
                                  height=9, width=82)
        self.plain_text.place(x=140, y=30)

        self.key_text = tk.Entry(window, show='*')
        self.key_text.place(x=138, y=163, width=582, height=26)
        # text variable暫時不用

        self.cypher_text = tk.Text(window,
                                   highlightthickness=1.2,
                                   highlightbackground='#CCCCCC',
                                   highlightcolor='#A1CBF1',
                                   height=9, width=82)
        self.cypher_text.place(x=140, y=203)

        encrypt_button = tk.Button(
            window, text='DES加密', width=50, height=30, command=self.des_en)
        encrypt_button.place(x=200, y=350, width=80, height=26)
        decrypt_button = tk.Button(
            window, text='DES解密', width=50, height=30, command=self.des_de)
        decrypt_button.place(x=500, y=350, width=80, height=26)
        encrypt_button = tk.Button(
            window, text='清空數據', width=50, height=30, command=self.des_clear)
        encrypt_button.place(x=200, y=390, width=80, height=26)
        decrypt_button = tk.Button(
            window, text='退出程式', width=50, height=30, command=self.des_exit)
        decrypt_button.place(x=500, y=390, width=80, height=26)

        self.window = window
        window.mainloop()

    def des_en(self):
        plain_text = self.plain_text.get(0.0, 'end')
        key_key = self.key_text.get(0.0, 'end')
        # result = des_decode()
        # print(result)

    def des_de(self):
        cypher_text = self.cypher_text.get(0.0, 'end').split('\n')[0]
        print(f'cypher text: {cypher_text} length is {len(cypher_text)}')
        key_text = self.key_text.get()
        print(f'key: {key_text}')
        return_text = DES().decrypt(cypher_text, key_text)
        print(return_text)

    def des_clear(self):
        pass

    def des_exit(self):
        self.window.quit()


if __name__ == '__main__':
    Gui()
