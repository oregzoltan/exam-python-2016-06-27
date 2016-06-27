import unittest
from third import count_letter_in_string

class TestCount_letter_in_string(unittest.TestCase):

    def test_zoli_i(self):
        self.assertEqual(count_letter_in_string('Zoli','i'), 1)

    def test_eperke_e(self):
        self.assertEqual(count_letter_in_string('eperke','e'), 3)

    def test_empty_string_s(self):
        self.assertEqual(count_letter_in_string('','s'), 0)

    def test_peti_no_letter(self):
        self.assertEqual(count_letter_in_string('Peti',''), 0)

    def test_empty_string_no_letter(self):
        self.assertEqual(count_letter_in_string('',''), 0)

if __name__ == '__main__':
    unittest.main()
