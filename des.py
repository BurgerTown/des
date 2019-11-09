from des_encrypt import DESEncrypt
from des_decrypt import DESDecrypt


class DES:
    def __init__(self, *args, **kwargs):
        pass

    def encrypt(self, from_code, key):
        # 轉換為16進制
        from_code = self._to_hex(self, from_code)
        key = self._to_hex(self, key)
        des_encrypt = DESEncrypt()
        key_len = len(key)
        string_len = len(from_code)
        if string_len < 1 or key_len < 1:
            print('error input')
            return False
        key_code = des_encrypt.code(from_code, key, string_len, key_len)
        return key_code

    def decrypt(self, from_code, key):
        key = self._to_hex(self, key)
        des_decrypt = DESDecrypt()
        key_len = len(key)
        string_len = len(from_code)
        if string_len % 16 != 0:
            return False
        if string_len < 1:
            return False
        if key_len < 1:
            return False
        key_code = des_decrypt.decode(from_code, key, key_len, string_len)
        return self._to_unicode(self, key_code)

    # 把unicode字符轉換為16進制
    @staticmethod
    def _to_hex(self, string):
        return_string = ''
        for i in string:
            return_string += "%02x" % ord(i)
        return return_string

    @staticmethod
    def _to_unicode(self, string):
        return_string = ''
        string_len = len(string)
        for i in range(0, string_len, 2):
            return_string += chr(int(string[i:i+2], 16))
        return return_string
