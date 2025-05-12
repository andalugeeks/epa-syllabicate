"""
Tests para la función syllabicate
"""

import unittest
from epa_syllabicate import syllabicate

class TestSyllabicate(unittest.TestCase):
    def test_basic_word(self):
        """Test para palabras básicas"""
        self.assertEqual(syllabicate("toque"), ["to", "que"])
        self.assertEqual(syllabicate("casa"), ["ca", "sa"])
        self.assertEqual(syllabicate("meça"), ["me", "ça"])
        self.assertEqual(syllabicate("çofá"), ["ço", "fá"])

    def test_empty_word(self):
        """Test para palabra vacía"""
        self.assertEqual(syllabicate(""), [])

    def test_single_letter(self):
        """Test para palabras de una letra"""
        self.assertEqual(syllabicate("a"), ["a"])
        self.assertEqual(syllabicate("e"), ["e"])
        self.assertEqual(syllabicate("â"), ["â"])

    def test_complex_words(self):
        """Test para palabras más complejas"""
        self.assertEqual(syllabicate("çôh"), ["çôh"])
        self.assertEqual(syllabicate("êttanda"), ["ê", "ttan", "da"])
        self.assertEqual(syllabicate("cohêl-lo"), ["co", "hêl", "lo"])


if __name__ == "__main__":
    unittest.main() 