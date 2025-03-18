# ©️ Ayça "Alex" Kaygusuz 2025

import unittest
from src.substring_concat import findSubstring

class TestFindSubstring(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(findSubstring("barfoothefoobarman", ["foo", "bar"]), [0, 9])
        self.assertEqual(findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]), [])
        self.assertEqual(findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]), [6, 9, 12])

    def test_empty_string(self):
        self.assertEqual(findSubstring("", ["foo", "bar"]), [])
        self.assertEqual(findSubstring("", []), [])

    def test_empty_words(self):
        self.assertEqual(findSubstring("barfoothefoobarman", []), [])

    def test_no_matching_substring(self):
        self.assertEqual(findSubstring("abcdefg", ["hij", "klm"]), [])
        self.assertEqual(findSubstring("barfoothefoobarman", ["xyz", "abc"]), [])

    def test_single_word(self):
        self.assertEqual(findSubstring("foobar", ["foo"]), [0])
        self.assertEqual(findSubstring("foobar", ["bar"]), [3])

    def test_repeated_words(self):
        self.assertEqual(findSubstring("wordgoodgoodgoodbestword", ["good", "good", "best", "word"]), [8])

if __name__ == '__main__':
    unittest.main()