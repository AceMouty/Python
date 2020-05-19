
def main():
    nums = range(1, 21)
    nums = list(nums)

    for num in nums:
        if num == 4 or num == 13:
            print(f"{num} is unlucky")
        elif num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")


if __name__ == "__main__":
    main()