# Factorial

try:
    factored_number = int(input("Insert an integer number to be factored: "))

    if factored_number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    total = 1

    for i in range(1, factored_number + 1):
        total *= i

    print(f"The factorial of {factored_number} is {total}")

except ValueError as e:
    print(e)
