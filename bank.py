def greet():
    greet = input("Greeting: ").lower().strip()
    if greet == "hello" or greet == "hello, newman":
        print("$0")
    elif greet == "h" or greet == "Hey" or greet == "how you doing?":
        print("$20")
    else:
        print("$100")
greet()



