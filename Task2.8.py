user_input = input("Enter a string: ")
digit_count = 0
letter_count = 0
for ch in user_input:
    if ch.isnumeric():
        digit_count += 1
    elif ch.isaplha():
        letter_count += 1
print("""
Letters: %d
Digits: %d
""" % (digit_count, letter_count))