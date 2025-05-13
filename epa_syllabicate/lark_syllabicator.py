from lark import Lark, Tree

grammar = """
    start: silaba+

    silaba: CONSONANTE? VOCAL CONSONANTE?
    CONSONANTE: /[bcçdfghjklmnñpqrstvwxyz]/
    VOCAL: /[aeiouáéíóúâêîôûàèìòùâêîôû]/

    %import common.WS
    %ignore WS
"""

def _parse_word(word: str) -> Tree:
    parser = Lark(grammar)
    return parser.parse(word)

def _parse_tree(tree: Tree) -> list[str]:
    result = []
    for silaba in tree.children:
        # Extraer los caracteres de la sílaba
        chars = []
        for child in silaba.children:
            if isinstance(child, Tree):
                chars.extend(child.children)
            else:
                chars.append(child)
        result.append(''.join(chars))
    return result

def syllabicate(word: str) -> list[str]:
    tree = _parse_word(word)
    return _parse_tree(tree)
