import pytest
from project import *

def main():
    test_cell_pos()
    test_text_pos()
    test_is_guess_valid()

# Test cell_pos
# Ensure error shown if inputs are not positive ints
def test_cell_pos():
    assert cell_pos(0,0) == (40, 40)
    assert cell_pos(1,1) == (130, 130)
    assert cell_pos(2,2) == (220, 220)
    assert cell_pos(4,5) == (400,490)
    with pytest.raises(TypeError):
        cell_pos(1, 'a')
    with pytest.raises(TypeError):
        cell_pos('b', 1)
    return True



# Test text_pos
# Ensure error shown if inputs are not positive ints
def test_text_pos():
    assert text_pos(0,0) == (80, 90)
    assert text_pos(1,1) == (170, 180)
    assert text_pos(2,2) == (260, 270)
    assert text_pos(4,5) == (440, 540)
    with pytest.raises(TypeError):
        text_pos('a', 1)
    with pytest.raises(TypeError):
        text_pos(1, 'b')
    return True


# Test is_valid():
def test_is_guess_valid():
    assert is_guess_valid('aback') == True
    assert is_guess_valid('ababa') == False
    assert is_guess_valid('ROunD') == True
    assert is_guess_valid('SMITE') == True
    with pytest.raises(TypeError):
        is_guess_valid(12345)
    with pytest.raises(TypeError):
        is_guess_valid(['a', 'b', 'a', 'c', 'k'])
    return True



if __name__ == '__main__':
    main()