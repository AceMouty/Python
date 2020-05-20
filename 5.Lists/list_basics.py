# what is a list
#   lists are just a general collection
#   or grouping of items
#   lists are arrays in other languages

# a basic list
tasks = ["Eat", "Sleep", "Code", "Repeat"]

# to get the length of a list
# you can use the len() function
print(len(tasks))

# creating a list out of a range
numsList = list(range(10))
print(numsList)
print('The length of nums list', len(numsList))

# create a list full of none
noneList = [None] * 10
print(noneList)

# =====================================================

# list are 0 based, this means that list start counting at 0

friends = ["Ashley", "Ron", "Harry"]
print(friends[0])
print(friends[1])
my_bestie = friends[2]
print(my_bestie)

# we can index a list using negative numbers as well

print(friends[-2])

# we are also able to use the "in" operator to check for something
# in a list, the value returned is a boolean True or False

colors = ["red", "green", "blue", "yellow"]
print("purple" in colors)


# print out all items in a list
for friend in friends:
    print(friend)

for color in colors:
    print(color)

# print out all items using a while loop
i = 0
while i < len(numsList):
    print(numsList[i])
    i += 1
