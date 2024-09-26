class CaesarCipher:
    def __init__(self, plaintext,cipher_text ,difference):
        self.plaintext = plaintext
        self.cipher_text = cipher_text
        self.difference = difference

    def encrypt(self):
        new_char = ''
        for i in self.plaintext:
            if (ord(i) >= 65) and ord(i) <= 90:
                new_value = ord(i) + self.difference
                if new_value>90:
                    diff = new_value - 90
                    new_value = 65 + diff

            elif (ord(i) >= 97) and ord(i) <= 122:
                new_value = ord(i) + self.difference
                if new_value>122:
                    diff = new_value - 122
                    new_value = 97 + diff

            elif ord(i) == 32:
                new_value = ord(i)

            new_char = new_char + chr(new_value)
        return new_char

    def decrypt(self):
        new_char = '';
        for i in self.cipher_text:
            if (ord(i) >= 65) and ord(i) <= 90:
                new_value = ord(i) - self.difference

            elif (ord(i) >= 97) and ord(i) <= 122:
                new_value = ord(i) - self.difference

            elif ord(i) == 32:
                new_value = ord(i)

            new_char = new_char + chr(new_value)
        return new_char





