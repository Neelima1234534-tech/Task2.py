a, b, c = 10, 20, 30
avg = (a + b + c) / 3
print("avg = ", avg)
if avg > a and avg > b and avg > c:
    print("Average is higher than a, b, c")
else:
    if avg > a and avg > b:
        print("Average is higher than a, b, c")
    elif avg > a and avg > c:
        print("Average is higher than a, c")
    elif avg > b and avg > c:
        print("Average is higher than b, c")
    elif avg > a:
        print("Average is higher than a only.")
    elif avg > b:
        print("Average is higher than b only.")
    elif avg > c:
        print("Average is higher than c only.")