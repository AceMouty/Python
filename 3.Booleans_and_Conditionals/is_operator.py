#!/usr/bin/python3


class A:
    pass


def main():

    # the "is" operator not only checks a value
    # but also checks that two values are objects of the same
    # instance aka are refrencing the same place in memory
    myObj = A()
    myOtherObj = myObj

    # myOtherObj refrences myObj so the evaluation should return true
    print(myObj is myOtherObj)  # -> True

    myObj = A()
    myOtherObj = A()

    # myObj and myOtherObj are two seperate instances of the class A
    # so when "is" runs a check, it returns False since
    # these are two different instances in MEMORY of the same Object Type
    print(myOtherObj is myObj)


if __name__ == "__main__":
    main()
