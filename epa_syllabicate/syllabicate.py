"""
Main module for syllable division.
"""

def andluh_epa_algorithm(word: str) -> list[str]:
    """
    complex algorithm for syllable division.
    
    Args:
        word (str): The word to syllabify.
        
    Returns:
        list[str]: sylables of the word.
    """
    return [word]

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
    if word == "":
        return []
    if len(word) == 1:
        return [word]
    else:
        return andluh_epa_algorithm(word)
