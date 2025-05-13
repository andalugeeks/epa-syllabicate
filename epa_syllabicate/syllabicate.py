"""
Main module for syllable division.
"""

from epa_syllabicate.lark_syllabicator import syllabicate as lark_syllabicate


def syllabicate(word: str) -> list[str]:
    """
    Divide una palabra en sílabas.

    Args:
        word (str): The word to syllabify.

    Returns:
        list[str]: sylables of the word.

    Examples:
        >>> syllabicate("ehemplo")
        ['e', 'hem', 'plo']
    """
    low_word = word.lower()
    if low_word == "":
        return []
    if len(low_word) == 1:
        return [low_word]
    else:
        return lark_syllabicate(low_word)
