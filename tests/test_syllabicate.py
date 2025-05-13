"""
Tests para la función syllabicate
"""

import unittest
from epa_syllabicate import syllabicate


class TestSyllabicate(unittest.TestCase):
    def test_basic_word(self):
        """Test para palabras básicas"""
        self.assertEqual(syllabicate("toque"), ["to", "que"])

    def test_casa_word(self):
        """Test para palabras con qu"""
        self.assertEqual(syllabicate("casa"), ["ca", "sa"])

    def test_meça_word(self):
        """Test para palabras con ç"""
        self.assertEqual(syllabicate("meça"), ["me", "ça"])

    def test_çofá_word(self):
        """Test para palabras con ç"""
        self.assertEqual(syllabicate("çofá"), ["ço", "fá"])

    def test_empty_word(self):
        """Test para palabra vacía"""
        self.assertEqual(syllabicate(""), [])

    def test_single_letter(self):
        """Test para palabras de una letra"""

    def test_e_word(self):
        """Test para palabras con ae"""
        self.assertEqual(syllabicate("ê"), ["ê"])

    def test_a_word(self):
        """Test para palabras con ae"""
        self.assertEqual(syllabicate("â"), ["â"])

    def test_complex_words_1(self):
        """Test para palabras más complejas"""
        self.assertEqual(syllabicate("çôh"), ["çôh"])

    def test_complex_words_2(self):
        """Test para palabras más complejas"""
        self.assertEqual(syllabicate("êttanda"), ["ê", "ttan", "da"])

    def test_complex_words_3(self):
        """Test para palabras más complejas"""
        self.assertEqual(syllabicate("cohêl-lo"), ["co", "hêl", "lo"])

    def test_complex_words_4(self):
        """Test para palabras más complejas"""
        self.assertEqual(syllabicate("ôhhetibâh"), ["ô", "hhe", "ti", "bâh"])


if __name__ == "__main__":
    unittest.main()
