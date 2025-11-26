from match import *


def test_nulls_equal():
    assert Null() == Null()


def test_lit_equal_with_equal_chars():
    assert Lit("abc") == Lit("abc")


def test_lit_not_equal_with_diff_chars():
    assert Lit("abc") != Lit("def")


def test_any_lit_equal():
    assert Any(Lit("abc")) == Any(Lit("abc"))


def test_either_equal():
    assert Either(Lit("abc"), Lit("def")) == Either(Lit("abc"), Lit("def"))
