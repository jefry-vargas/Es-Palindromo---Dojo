import unittest
from Codigo import es_palindromo, limpiar_texto

class TestPalindromeUtils(unittest.TestCase):

    def test_normalization(self):
        self.assertEqual(limpiar_texto("A man, a plan!"), "amanaplan")

    def test_true_palindromes(self):
        self.assertTrue(es_palindromo("Anita lava la tina"))
        self.assertTrue(es_palindromo("A man a plan a canal Panama"))
        self.assertTrue(es_palindromo("reconocer"))

    def test_false_palindromes(self):
        self.assertFalse(es_palindromo("Hola mundo"))
        self.assertFalse(es_palindromo("Python"))

if __name__ == '__main__':
    unittest.main()