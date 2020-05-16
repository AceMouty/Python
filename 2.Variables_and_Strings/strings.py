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
    print()

    # String formatting, allows us to inject variables
    # into our strings using what is known as an f string
    # resource: https://realpython.com/python-string-formatting/
    guess = 8
    print(f"your guess was {guess}\n")
    # we can also perform opperations / math in here
    print(f"One number above your guess would be {guess + 1}\n")

    # we are also able to index a string in the same way that we are
    # able to do with a list using [index]
    f_name = "John"
    print(f_name[0])  # -> will give us J

if __name__ == "__main__":
    main()
