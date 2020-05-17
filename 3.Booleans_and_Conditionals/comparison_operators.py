#!/usr/bin/python3

def main():
    # comparison operators will return a True or False
    # value which can be used in our conditional logic.
    # this allows us to control more with our programs

    """
        a = 1
        b = 1

        == : checks to see if two vlaues are equal
            a == b -> True
        != : checks that a value is NOT eaqul to another
            a != b -> False
        > (greater) / < (less): checks if values are greater or
                                less than one another.
            a > b -> False
            a < b -> False
        >= (greater or equal)
        <= (less than or equal) : checks to see if two values
                                  are greater or equal OR less than
                                  or equal to one another.
            a >= b -> True
            a <= b -> True
    """

    num1 = 10
    num2 = 20
    if num2 > num1:
        print(f"{num2} is greater than {num1}")

    num1 = 5
    num2 = 5
    if num1 == num2:
        print(f"{num1} is equal to {num2}")

    num1 = 4
    num2 = 20
    if num1 < num2:
        print(f"{num1} is less than {num2}")

    if num1 != num2:
        print(f"{num1} is NOT equal to {num2}")


if __name__ == "__main__":
    main()
