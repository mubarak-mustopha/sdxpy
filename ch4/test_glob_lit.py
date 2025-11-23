from glob_lit import Lit

def test_literal_match_entrire_string():
    # /abc/ matches "abc"
    assert Lit("abc").match("abc")

def test_literal_substring_alone_no_match():
    # /ab/ doesn't matches "abc"
    assert not Lit("ab").match("abc")

def test_literal_superstring_no_match():
    # /abc/ doesn't matches "ab"
    assert not Lit("abc").match("ab")

def test_literal_followed_by_literal_match():
    # /a/ + /b/ matches "ab"
    assert Lit("a", Lit("b")).match("ab")

def test_literal_followed_by_literal_no_match():
    # /a/ + /b/ doesn't matches "ac" 
    assert not Lit("a", Lit("b")).match("ac")
