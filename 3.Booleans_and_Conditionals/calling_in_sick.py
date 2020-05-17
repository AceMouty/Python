
from random import randint, choice


def main():

    # variabel setup
    actually_sick = choice([True, False])
    kinda_sick = choice([True, False])
    hate_your_job = choice([True, False])
    sick_days = randint(0, 10)
    calling_in_sick = None

    if actually_sick and sick_days:
        calling_in_sick = True
    elif kinda_sick and hate_your_job and sick_days:
        calling_in_sick = True
    else:
        calling_in_sick = False

    if calling_in_sick:
        print("Calling in sick today")
    else:
        print("Looks like we are going in")


if __name__ == "__main__":
    main()

    runAgain = True
    while runAgain:

        print("Play again?")
        user_choice = input()

        if not user_choice:
            print("\n" * 50)
            print("Sorry I didnt quite understand that")
        elif user_choice[0].lower() == "y":
            print("\n" * 50)
            main()
        else:
            runAgain = False
