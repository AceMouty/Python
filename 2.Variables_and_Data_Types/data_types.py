def main():
    # some simple data types that we have in Python

    # boolean: True or False
    isGameOver = False
    print("isGameOver is of type")
    print(type(isGameOver))
    print()

    # integer: integers are whole numbers
    myAge = 23
    print("myAge is of type")
    print(type(myAge))
    print()

    # string: a stirng is a word / multipile characters in a row
    fName = "John"
    print("fName is of type")
    print(type(fName))
    print()

    # list: list is a python array, it can hold any type of data
    # we can access and set data in a list using an index
    myList = ["John Doe", 23, False, {"name": "Billy"}]
    print("myList is of type")
    print(type(myList))
    print()
    print("*** Here is what is in myList ***")
    print(myList[0])
    print(myList[1])
    print(myList[2])
    print(myList[3])
    print("Lets change False to True...")
    myList[2] = True
    print(myList[2])
    print()

    # dictionary (dict): storing data with key / value pairs. This is
    # in a way storing a collection of different variables
    # just like in a list we can store ANY kind of data in here
    # we instead access its data via a key / name and in return
    # we get the value stored in that key / name

    myDict = {"name": "John Doe", "age": 22, "city": "Austin"}
    print("myDict is of type")
    print(type(myDict))
    print("*** Here is what is in myDict")
    print(myDict["name"])
    print(myDict["age"])
    print(myDict["city"])
    

if __name__ == "__main__":
    main()
