from remove_vowel import remove_vowel
import unittest


class RemoveVowelTest(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual("bcdfg", remove_vowel("abcdefg"))
        self.assertEqual("bC dFg", remove_vowel("IbC duFg"))
    
    def test_empty_string(self):
        self.assertEqual("", remove_vowel(""))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_vowel(12345)

    def test_extremely_log_string(self):
        self.assertEqual("b"*10, remove_vowel(("a"*10)+("b"*10)+("O"*10)))
        self.assertEqual("", remove_vowel(("U"*100)+("e"*100)+("O"*100)))
