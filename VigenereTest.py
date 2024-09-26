import unittest
from Vigenere import Vigenere


class MyTestCase(unittest.TestCase):
    def test_encrypt(self):
        plaintext = "TOBEO"
        encrypt = "KSMEH"
        self.assertEqual(encrypt,Vigenere(plaintext, None).encrypt())

    def test_encrypt(self):
        plaintext = "TOBEO"
        encrypt = "KSMEH"
        self.assertEqual(plaintext ,Vigenere(None,encrypt).decrypt())


if __name__ == '__main__':
    unittest.main()
