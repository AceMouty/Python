# some extra list methods

# index: returns the index of the specified
# item in the list
#
# you can also pass in a starting index
# to start the search from
# index(item, start_index)
#
# you can also pass in a ending index to
# identify a stop point for the index search
# index(item, start_index, end_index)

numbers = [5, 6, 7, 8, 9, 10]

print("The index of number 6 is: ", numbers.index(6))
print("The index of number 9 is: ", numbers.index(9))


# count: returns the number of times an item
# appears in a list

numbers = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2]
freqThree = numbers.count(3)
print("The number 3 shows up " + str(freqThree) + " times")

# reverse: will reverse the order of a list
# this is an inplace operation, meaning that
# it doesnt make a new copy or anything. It
# updates the original copy

names = ["Billy", "Joe", "Jane", "John", "Skylar"]
print("Names before the reverse")
print(names)
names.reverse()
print("Names after the reverse")
print(names)

# sort: sorts the list for you, another inplace
# operation

names.sort()
print("Names sorted")
print(names)


# join: a string method, used to join / convert a list
# to a string
#
# "string to join".join(list)
# the string that calls on join will join
# the list with every element joined with
# the string provided

phrase = "Coding is fun"
# cretae an array from a string
words = phrase.split(" ")

print("Words is currently")
print(words)
print("*** Joining Words List ***")
# join the words back into a string
phrase = " ".join(words)
print(phrase)

name = ["Mr", "Blue"]
print("Name before join")
print(name)
name = ". ".join(name)
print("Name after join")
print(name)
