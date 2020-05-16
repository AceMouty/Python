def main():

    # variables MUST start with a letter or underscore
    # the rest of a varibale name can only have a
    # letter, number or underscore

    # variables are ways for us to store data that
    myFavNumber = 7
    fName = "John"
    lName = "Doe"
    print(myFavNumber)
    print(fName + " " + lName)
    # we can assign multiple variables at a time
    we, are, together = 2, 4, 6
    print(we + are + together)
    print()
    num_of_cats = 99
    print("we currently have " + str(num_of_cats) + " cats")
    num_of_cats = num_of_cats - 1
    print("But..we got rid of a cat so now we have " + str(num_of_cats))


if __name__ == "__main__":
    main()
