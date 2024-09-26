class Vigenere:
    def __init__(self,plaintext,cipher_text):
        self.plaintext = plaintext
        self.cipher_text = cipher_text

    def encrypt(self):
        text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = "RELATIONS"
        new_key = ''
        update = ''
        new_char = ''

        # key is updated to the length of planetext
        if len(key) < len(self.plaintext):
            length = 0
            new_key = key
            for i in range(len(key), len(self.plaintext)):
                new_key = new_key + key[length]
                length = length+1
                if length > len(key):
                    length = 0
        else:
            for i in range(len(self.plaintext)):
                new_key = new_key + key[i]
        counter = -1
        for i in new_key:
            counter = counter + 1

            if i in text:

                print(len(text),text.index(i))
                for j in range(text.index(i), len(text)):
                    update = update + text[j]
                for j in range(text.index(i)):

                    update = update + text[j]

                print(len(update))

            for j in text:
                    if j == self.plaintext[counter]:
                        new_char = new_char + update[text.index(j)]
                        update = ''
        return new_char


    def decrypt(self):
        text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = "RELATIONS"
        new_key = ''
        update = ''
        new_char = ''

        # key is updated to the length of cipher_text
        if len(key) < len(self.cipher_text):
            length = 0
            new_key = key
            for i in range(len(key), len(self.cipher_text)):
                new_key = new_key + key[length]
                length = length + 1
                if length > len(key):
                    length = 0
        else:
            for i in range(len(self.cipher_text)):
                new_key = new_key + key[i]

        counter = -1
        for i in new_key:
            counter = counter + 1
            if i in text:
                for j in range(text.index(i), len(text)):
                    update = update + text[j]
                for j in range(text.index(i)):
                    update = update + text[j]

            for j in update:
                if j == self.cipher_text[counter]:
                    new_char = new_char + text[update.index(j)]

                    update = ''
        return new_char








