from bank import value

def main():
    test_return_0()
    test_return_20()
    test_return_100()

def test_return_0():
    assert value('hello') == 0

def test_return_20():
    assert value('h') == 20

def test_return_100():
    assert value('Salam') == 100
    assert value('Good Morning') == 100

def test_entire_phrase():
    assert value('Hello, how are you?') == 0
    assert value('Hooray, it worked!') == 20

if __name__ == "__main__":
    main()