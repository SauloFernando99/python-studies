#Divisible by 10, 5 or 2

number = int(input("Provide a integer number: "))
dividers = []

if not number % 10:
    dividers.append(10)

if not number % 5:
    dividers.append(5)

if not number % 2:
    dividers.append(2)

if len(dividers) == 0:
    print(f"{number} isn't divisible by 10, 5 or 2")

for divisor in dividers:
    print(f"{number} is divisible by {divisor}")