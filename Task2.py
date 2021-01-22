if user_input1 in [1, 2, 3, 4, 5]:
    first = eval(input("Enter first number:"))
    second = eval(input("Enter second number:"))
    if user_input1 == 1:
        print("Addition:", first + second)
    elif user_input1 == 2:
        print("Subtraction:", first - second)
    elif user_input1 == 3:
        print("Division:", first / second)
    elif user_input1 == 2:
        print("Multiplication:", first * second)
    else:
        first1 = eval(input("Enter the third number:"))
        second1 = eval(input("Enter fourth number:"))
        print("Average:", sum([first, second, first1, second1]) / 4)
else:
    print("ZSA")