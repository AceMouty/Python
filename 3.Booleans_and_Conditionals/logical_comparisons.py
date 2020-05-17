#!/usr/bin/python3

def main():

    # check for an age between 2 and 8

    # and op: both the left and right side need to resolve to
    #   True, if either side is false the entire evaluation is false
    age = 5
    if age > 2 and age < 8:
        print("You are older than 2 but younger than 8")

    # or op: only one side needs to evaluate to True
    #   in order for the entire evaluation to be True
    print("What city do you live in?")
    city = input()

    # make the first letter in a string lowercase
    if city:
        city = city.lower()

    if city == "austin" or city == "dallas":
        print("You live in Texas")


if __name__ == "__main__":
    main()
