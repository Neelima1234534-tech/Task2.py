guess = 57
while True:
    user_input = int(input("Guess the lucky number: "))
    if user_input == guess:
        user_input, answer = input("Do you want to guess again? (Enter number & Yes to continue. Enter No to stop")
        if user_input != guess and answer.lower() == 'yes':
            continue
        elif user_input == guess:
            break
        elif answer.lower == 'no':
            break
