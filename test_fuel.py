from fuel import convert, guage
import pytest

def main():
    # calling the test function
    test_correct_input()
    test_ZeroDivisionError()
    test_ValueError()

# testing ZeroDivisionError
def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

# Testing ValueError
def test_ValueError():
    with pytest.raises(ValueError):
        convert('cat/dog')

# testing the correct input
def test_correct_input():
    assert convert('1/4') == 25 and guage(25) == '25%'
    assert convert('1/100') == 1 and guage(1) == 'E'
    assert convert('99/100') == 99 and guage(99) == 'F'


if __name__ == "__main__":
    main()
