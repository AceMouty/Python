#!/usr/bin/python3

from random import randint


def main():

    # setup x and y vars
    x = randint(-100, 100)
    # set x to something other than 0
    while x == 0:
        x = randint(-100, 100)

    y = randint(-100, 100)
    while y == 0:
        y = randint(-100, 100)

    print(checkNumbers(x, y))

    return


def checkNumbers(num1, num2):
    res = None
    if num1 > 0 and num2 > 0:
        res = "both positive"
    elif num1 < 0 and num2 < 0:
        res = "both negative"
    elif num1 > 0 and num2 < 0:
        res = "x is positiveand y is negative"
    else:
        res = "x is negative and y is positive"
    return res


if __name__ == "__main__":
    main()
