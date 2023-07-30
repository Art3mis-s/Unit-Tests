from twttr import shorten

def main():
    # Calling test function
    test_upper_lower_cases()



def test_upper_lower_cases():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwtTR') == 'TwtTR'

# Test numbers
def test_number():
    assert shorten('1234') == '1234'


# Test Punctuation
def test_punctuation():
    assert shorten('!?.,') == '!?.,'


if __name__ == "__main__":
    main()