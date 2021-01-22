import random
guess = 57
counter = 0
while counter < 5:
    user_input = int(input("Guess the lucky number: "))
    if user_input == guess:
        print("Good guess!")
        guess = random.randint(1, 100)
    else:
        print("Try again!")
    counter += 1
print("Game over!")
