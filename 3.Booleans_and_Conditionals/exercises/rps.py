
from random import choice

# some global vars
rock = "rock"
paper = "paper"
scissors = "scissors"


def main():

    print("Which do you choose...?")
    print(f"{rock} {paper} or {scissors}")
    user_choice = input()

    options = [rock, paper, scissors]
    while (user_choice not in options):
        print("Please pick either rock, paper or scissors")
        user_choice = input()

    ai_choice = choice(options)
    if user_choice == ai_choice:
        print("\n\n")
        print("Its a draw")
    elif user_choice == paper and ai_choice == rock:
        print("\n\n")
        print(f"You won with {user_choice}, the ai picked {ai_choice}")
    elif user_choice == scissors and ai_choice == paper:
        print("\n\n")
        print(f"You won with {user_choice}, the ai picked {ai_choice}")
    elif user_choice == rock and ai_choice == scissors:
        print("\n\n")
        print(f"You won with {user_choice}, the ai picked {ai_choice}")
    elif ai_choice == paper and user_choice == rock:
        print("\n\n")
        print(f"You lost with {user_choice}, the ai picked {ai_choice}")
    elif ai_choice == scissors and user_choice == paper:
        print("\n\n")
        print(f"You lost with {user_choice}, the ai picked {ai_choice}")
    elif ai_choice == rock and user_choice == scissors:
        print("\n\n")
        print(f"You lost with {user_choice}, the ai picked {ai_choice}")


if __name__ == "__main__":
    main()

    playAgain = True
    while playAgain:
        print("Play again, Yes or No?")
        user_input = input()

        if not user_input or user_input[0].lower() != "y":
            playAgain = False
        else:
            print("\n" * 100)
            main()
