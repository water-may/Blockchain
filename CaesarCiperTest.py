import unittest
from caesarCipher import CaesarCipher


class MyTestCase(unittest.TestCase):
    def test_encrypt(self):
        plaintext = "SAgar"
        encrypted = "TBhbs"

        self.assertEqual(encrypted, CaesarCipher(plaintext, None, 1).encrypt())

    def test_decrypt(self):
        plaintext = "Sagar"
        encrypted = "Tbhbs"

        self.assertEqual(plaintext, CaesarCipher(None, encrypted, 1).decrypt())


if __name__ == '__main__':
    unittest.main()
