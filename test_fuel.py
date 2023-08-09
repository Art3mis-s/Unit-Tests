from fuel import convert, gauge
import pytest

def main():
    # calling the test function
    test_gauge()
    test_ZeroDivisionError()
    test_ValueError()
    test_convert()

# testing ZeroDivisionError
def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

# Testing ValueError
def test_ValueError():
    with pytest.raises(ValueError):
        convert('x/y')


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_convert():
    assert convert("0/1") == 0
    assert convert("1/2") == 50
    assert convert("4/4") == 100

if __name__ == "__main__":
    main()
