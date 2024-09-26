import unittest
from Monoalphabetic import  MonoAlphabetic


class MyTestCase(unittest.TestCase):
    def test_encrypt(self):
        plaintext = "Hello"
        encrypted_text = "Stssg"
        self.assertEqual(encrypted_text, MonoAlphabetic(plaintext, None).encrypt())

    def test_decrypt(self):
        plaintext = "Hello"
        encrypted_text = "Stssg"
        self.assertEqual(plaintext, MonoAlphabetic(None, encrypted_text).decrypt())


if __name__ == '__main__':
    unittest.main()
