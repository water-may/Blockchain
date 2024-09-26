class MonoAlphabetic:
    def __init__(self, plaintext ,cipher_text):
        self.plaintext = plaintext
        self.cipher_text = cipher_text

    def encrypt(self):
        new_char = ''
        text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        cipher = 'HTKCUOISJYARGMZNBVFPXDLWQEqwertyuiopasdfghjklzxcvbnm'
        for i in self.plaintext:
            if i in text:
                new_char = new_char + cipher[text.index(i)]
        return new_char

    def decrypt(self):
        new_char = ''
        text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        cipher = 'HTKCUOISJYARGMZNBVFPXDLWQEqwertyuiopasdfghjklzxcvbnm'
        for i in self.cipher_text:
            if i in cipher:
                new_char = new_char + text[cipher.index(i)]
        return new_char


