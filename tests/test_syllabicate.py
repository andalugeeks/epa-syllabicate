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
        self.assertEqual(syllabicate("mesa"), ["me", "sa"])
        self.assertEqual(syllabicate("sol"), ["sol"])

    def test_empty_word(self):
        """Test para palabra vacía"""
        self.assertEqual(syllabicate(""), [])

    def test_single_letter(self):
        """Test para palabras de una letra"""
        self.assertEqual(syllabicate("a"), ["a"])
        self.assertEqual(syllabicate("e"), ["e"])

    def test_complex_words(self):
        """Test para palabras más complejas"""
        self.assertEqual(syllabicate("ejemplo"), ["e", "jem", "plo"])
        self.assertEqual(syllabicate("árbol"), ["ár", "bol"])

if __name__ == "__main__":
    unittest.main() 