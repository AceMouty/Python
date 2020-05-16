def main():

    # conditional logic is using if statements
    # these represent differnt paths that we want
    # to dake based on some condition that we
    # setup

    # ex
    # if some condition here is True:
    #   run the code that is here
    # elif some other condition is True:
    #   run the code in here instead
    # else:
    #   if none of the above is True then run this code here.

    print("*** Lets see if you are old enough to drink ***")
    print("How old are you?")
    age = int(input())
    if age < 21:
        print("You are unable to drink")
    else:
        print("Drink responsibly")


if __name__ == "__main__":
    main()
