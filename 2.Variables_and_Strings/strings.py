def main():
    # with strings if you want to concat a string to another
    # value you need to make sure that the data type is of type
    # str if not you will get an error
    age = 23
    print("I am " + str(age) + " years old")  # here we make an int into a string

    # escaping with \:
    # with strings we can also use escaping, this is useful for when we need to use double quotes
    # within double quote, if you dont escape them it will throw an error
    my_str = "They told me \"You dont have to pay a dime\" what has changed here?"
    print(my_str)
    print()

    # we can also add in tabs and other characters with the \
    # here we will tab the output
    my_str = "This\t line\t is tabbed a bit"
    print(my_str)
    print()

    # we can also add in a new line with \n
    my_str = "We will add in a new line\nand look a that, we are on a new line"
    print(my_str)


if __name__ == "__main__":
    main()
