#!/usr/bin/python3

def main():
    # strings anything in ""s or ''s
    print("Today is a good day to learn python")
    print('Python is fun')
    print("Python strings are ez to use")
    print('We can use "quotes" in strings')
    print()
    print("We can even add strings to other strings")
    print("Like " + "this")

    # variable
    firstName = "Kyle "
    lastName = "Guerrero"
    print(firstName + lastName)

    # we can even take in user input
    entry_one = input("What is your name?\n")
    lastName = " Doe"
    print(entry_one + lastName)

    # we can also us \ to escape characters in strings
    print('The pet shop owner said "No, no, \'e\'s uuuh......he\'s resting"')

    # a raw string (raw strings ignore \)
    print(r"\who\are\you")


if __name__ == "__main__":
    main()
