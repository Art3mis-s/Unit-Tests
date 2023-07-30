def main():
    #Get user input
    message = input("Input: ")
    #Removing all vowels
    message_without_vowels = shorten(message)
    #print "Output:
    print("Output: " + message_without_vowels)


def shorten(word):
    word_without_vowels = ""
    #Looping through every letter
    for letter in word:
        #Check if its not vowels whether inputed lowercase or uppercase
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            #print the letter
            word_without_vowels += letter
    #returning the new word
    return word_without_vowels

#add a new line
if __name__ == "__main__":
    main()