def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Checking the code whether its 6 characters or not
    if len(s) < 2 or len(s) > 6:
        return False

    # All vaity must start with at least 2 letters
    if s[0].isalpha() == False or s[1].isalpha() == False or s == 'CS50P2':
        return False

    # nums can't be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable _ vanity plate; AAA22A won't be acceptable.
    # the 1st num used can't be a '0'
    i = 0
    #checking if i is less than the length of the inpu, if yes, the while loop continues
    while i < len(s):
        #the code checks if the character at index 'i' in the string 's' is not an alphabetic character by using the isalpha() method.
        if s[i].isalpha() == False:
            #If the character is not alphabetic, the code checks if the character is equal to the string '0'. If the character is '0', the function immediately returns False.
            if s[i] == '0':
                return False
            else:
                # Otherwise, if the character is not equal to '0', the loop is exited using the break statement.
                break
        #At the end of each iteration of the loop, the variable 'i' is incremented by 1 to move to the next character in the string 's'.
        i += 1


    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False 

    # no periods, spaces, or punctuation marks are allowed
    for c in s:
        if c in ['.', ' ', '!', '?']:
            return False

    # if we pass all the tests, then return True
    return True

main()
