
def main():

    # ask for an age from the user
    print("How old are you?")
    userAge = int(input())

    if userAge >= 18 and userAge < 21:
        print("You may enter, but you need a wristband")
    elif userAge >= 21:
        print("You can drink")
    else:
        print("Sorry I cant let you in, youre to young")


if __name__ == "__main__":
    main()