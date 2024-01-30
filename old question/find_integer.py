X = int(input("Enter an integer X: "))
Y = X + 1

while True:
    digits = set()
    temp = Y
    is_unique = True

    while temp > 0:
        digit = temp % 10
        if digit in digits:
            is_unique = False
            break
        digits.add(digit)
        temp //= 10

    if is_unique:
        print("The smallest number greater than X with unique digits is:", Y)
        break

    Y += 1

