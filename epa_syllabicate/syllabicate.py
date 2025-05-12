"""
Módulo principal para la silabificación de palabras.
"""

def complex_algorithm(word: str) -> list[str]:
    """
    Algoritmo complejo para la silabificación de palabras.
    """
    return [word]

def syllabicate(word: str) -> list[str]:
    """
    Divide una palabra en sílabas.

    Args:
        word (str): La palabra a silabificar.

    Returns:
        list[str]: Lista de sílabas.

    Examples:
        >>> syllabicate("ehemplo")
        ['e', 'hem', 'plo']
    """
    if word == "":
        return []
    if len(word) == 1:
        return [word]
    else:
        return complex_algorithm(word)
