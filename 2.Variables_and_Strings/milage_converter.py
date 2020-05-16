def main():

    MILE = 1.60934
    distance_ran = input("How many kilometers did you run?\n")
    print(f"Ok you said {distance_ran}")
    miles = float(distance_ran) // MILE

    # round(thing to round, how many decimal places)
    print("So you ran " + str(round(miles, 2)) + " miles")


if __name__ == "__main__":
    main()
