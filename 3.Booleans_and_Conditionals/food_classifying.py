#!/usr/bin/python3

# will be used to select a random index
from random import choice


def main():

    # use choice to select a random food
    food = choice([
        "apple",
        "grape",
        "bacon",
        "steak",
        "worm",
        "dirt"
    ])

    # evaluations of our choice
    if food == "apple" or food == "graph":
        print("fruit")
    elif food == "bacon" or food == "steak":
        print("meat")
    elif food == "dirt" or food == "worm":
        print("yuck")


if __name__ == "__main__":
    main()
