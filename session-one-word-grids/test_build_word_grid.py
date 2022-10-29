from build_word_grid import build_word_grid

def test_empty_string():
    assert list(build_word_grid('')) == []

def test_cabbage():
    result = list(build_word_grid('cabbage'))
    assert result[0] == 'Cabbage'
    assert result[1] == 'cAbbage'
    assert result[2] == 'caBbage'
    assert result[3] == 'cabBage'
    assert result[4] == 'cabbAge'
    assert result[5] == 'cabbaGe'
    assert result[6] == 'cabbagE'
