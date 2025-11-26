from match import *
from parser import Parser

def test_parse_either_two_lit():
    assert Parser().parse("{abc,def}") == Either(
        Lit("abc"), Lit("def")
    )
