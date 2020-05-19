# a text based app that will copy / mock
# what yo uhave to say

def main():
    print("Hey hows it going?")
    userInput = input()
    killMsg = "stop copying me"

    while userInput.lower() != killMsg:
        print(userInput)
        userInput = input()
    print("UGH youre no fun 😝")


if __name__ == "__main__":
    main()
