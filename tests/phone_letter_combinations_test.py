# ©️ Ayça "Alex" Kaygusuz 2025

import unittest
from phone_letter_combinations import letter_combinations

class TestPhoneLetterCombinations(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        self.assertEqual(letter_combinations("2"), ["a", "b", "c"])

    def test_two_digits(self):
        self.assertEqual(letter_combinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    def test_three_digits(self):
        self.assertEqual(letter_combinations("234"), [
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
        ])

    def test_invalid_digit(self):
        self.assertEqual(letter_combinations("1"), [])

if __name__ == '__main__':
    unittest.main()