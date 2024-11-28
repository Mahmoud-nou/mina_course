from cryptography.fernet import Fernet

class DataEncrypt:
    # print(Fernet.generate_key())
    key = b'KVsUvEGgLDFQ5rQwIQoK3Kse5aVBWqkqaKEq1n-1cb0='

    @classmethod
    def encrypt(cls, data : str):
        try:
            return str(Fernet(cls.key).encrypt(data.encode()), 'utf-8')
        except:
            return False

    @classmethod
    def decrypt(cls, enc_data : str, type : str = 'str'):
        try:
            if type == 'str':
                return Fernet(cls.key).decrypt(enc_data).decode()
            elif type == 'obj':
                return eval(Fernet(cls.key).decrypt(enc_data).decode())
        except:
            return False
