
# for loop allows us to do something over
# and over again

# structure of for loop
# for item in collection:
#   print(item)

# print every letter in a word
for char in "hello world":
    print(char)

# range: used to generate a range
# of numbers to help with looping
# in for loops. range will start
# its count at 0 if you only
# provide one number.

# range(end_number)
# end_number -> the number to stop on

# the range generated is up to but not
# including the number passed

# range(start, end, skip_count_by)
# start -> starting number
# end -> up to but not including
# skip_count -> used to skip count
#               can count forward
#               or backward

for num in range(10):
    print(num)

nums = range(1, 10, 2)
myList = list(nums)
for num in myList:
    print(f"NUMBER IN LIST {num}")
