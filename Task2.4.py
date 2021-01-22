while True:
    try:
        user_input = int(input("Enter an integer number:"))
        if user_input < 0:
            print("It's over")
            break
        else:
            print("Good Going! Enter negative number to exit else continue.")
    except ValueError:
        pass
