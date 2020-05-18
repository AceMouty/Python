#!/usr/bin/python3

# use this as a random num generator
from random import randint


def main():
    # generate a random number between 1 and 10
    choice = randint(1, 10)

    # check to see if the number is 7 or not
    if choice == 7:
        print("Lucky 7")
    else:
        print("Unlucky")
        print(f"Number was {choice}")

    return


if __name__ == "__main__":
    # run the game atleast one time
    main()

    # check to see if the user wants to play again.
    # if yes replay else we will quit
    isTrue = True
    while isTrue:
        print("Play again?")
        play_again = input()

        if play_again[0].lower() == 'y':
            print("\n\n***Reroll***\n")
            main()
        else:
            isTrue = False
