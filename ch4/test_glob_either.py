from glob_either import Either
from glob_lit import Lit

def test_either_two_literals_first():
    # /{a,b}/ matches "a"
    assert Either(Lit("a"), Lit("b")).match("a")

def test_either_two_literals_not_both():
    # /{a,b}/ doesn't matches "ab"
    assert not Either(Lit("a"), Lit("b")).match("ab")
