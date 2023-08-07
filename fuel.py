def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = guage(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            #spliting the fuel
            numerator, denumerator = fraction.split("/")
            #converting the numerator and denumerator to integers
            new_numerator = int(numerator)
            new_denumerator = int(denumerator)

            #calculating the percentage
            f = new_numerator / new_denumerator
            #checking if its less than 1 and then stop the loop
            if f <= 1:
                # Multiply percentage by 100
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass

        except(ValueError, ZeroDivisionError):
            # here we use pass bcz this way we're gonna prompt the user again for a new input and the try and except will repeat
            raise


def guage(percentage):
    #checking if percentage is less than 1, so then print E
    if percentage <= 1:
        return 'E'
    #else if the percentage is greater than 99, so then print F
    elif percentage >= 99:
        return 'F'
    #otherwise, print the %, so we will use "formated string" aka: fstring
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
