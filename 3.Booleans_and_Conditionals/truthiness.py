#!/usr/bin/python3

class EmptyObj:
    pass


def main():

    # Pthon has falsy values
    # these are values that when evaluated
    # resolve to false.
    # falsy values include:
    # 1. empty objects
    # 2. empty strings
    # 3. None and 0

    # truth and falsy with numbers
    if 0:
        print("This is falsy")

    if 1:
        print("This is truthy")

    # truthy falsy strings
    if "":
        print("This is falsy")

    if "Some text":
        print("This is also truthy")


if __name__ == "__main__":
    main()
