
# a while loop will run until
# some condition is met

print("What is the secret password?")
secret = input()

while secret != "door":
    print("\n\n\n")
    print("WRONG")
    print("I need the secret, what is it....")
    secret = input()

print("\n\n\n")
print("You guessed the secret, you can now enter")

# convert for loop to while loop

# for num in range(1, 11):
#     print(num)

num = 1
while num < 11:
    print(num)
    num += 1

# break: break will allow us to brek
# out of a loop.

while True:
    print("what do you want")
    userInput = input()

    if userInput[0].lower() == 'q':
        break

    print("Whats that I didnt understand?")