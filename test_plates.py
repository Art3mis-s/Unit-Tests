from plates import is_valid

def main():
    test_min_and_max_characters()
    test_start_with_two_letters()

# Plates may contain a mximum of 6 characters (letters or numbers) and a minimum of 2 characters
def test_min_and_max_characters():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False


# Plates must start with at least two letters
def test_start_with_two_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False


if __name__ == "__main__":
    main()