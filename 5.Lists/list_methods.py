

# ==================================
# adding to a list
# ==================================

# append: adds one item to the end of a list
nums = [1, 2, 3, 4]
nums.append(5)
nums.append("orange")
print(nums)

# extend: adds multiple items to the end
# of a list OR will attatch one list
# to the end of another list
friends = ["Jane", "Billy", "Joe"]
friends.extend(["John", "Marry", "Jillian"])
print(friends)

# insert: insert an item at a given index
# to insert at the very end of a list
# use len()
myList = [1, 2, 3, 4]
myList.insert(2, "Hello")

# add to the end of the list with insert
myList.insert(len(myList), "Im at the end")
print(myList)

# ==================================
# removing from a list
# ==================================

# clear: delete ALL items in a list
shoppingList = ["apples", "oranges", "grapes"]
print(shoppingList)
print("*** clearing the shopping list ***")
shoppingList.clear()
print(shoppingList)

# pop: can pass a list index to be removed.
# if no index is passed it will remove
# the last item by default
#
#   pop also returns
#   the item that has been popped off, allowing
#   us to capture the value in a variabel or
#   some other form of storage

shoppingList.extend(["fruit", "mouth wash", "potstickers", "mug"])
produceItem = shoppingList.pop(0)
print("Captured value: ", produceItem)
shoppingList.pop()
print(shoppingList)


# remove: provide a value / item to be removed
# from the list. The first found instance will
# be removed.
# If nothing is found, a ValueError is thrown

numsList = [1, 2, 3, 4, 4, 4]
print(numsList)
numsList.remove(2)
print(numsList)
numsList.remove(4)
print(numsList)
