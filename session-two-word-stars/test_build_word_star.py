from build_word_star import build_word_star

def test_simplest_case():
    result = build_word_star("")
    assert result == []

def test_single_character():
    result = build_word_star("a")
    assert result == ["a"]

def test_two_characters():
    result = build_word_star("Hi")
    assert result == [
    			".i.",
    			"iHi",
    			".i." ]

def test_three_characters():
    result = build_word_star("cat")
    assert result == [
    			"..t..",
    			"..a..",
    			"tacat",
    			"..a..",
    			"..t.." ]
