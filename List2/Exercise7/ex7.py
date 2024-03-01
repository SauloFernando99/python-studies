def calculate_series(iterations_number):
    j = 1
    for i in range(iterations_number):
        print(f"{i+1}/{j}")
        j += 2


try:
    iterations_number = int(input("Insert the number of iterations: "))

    if iterations_number < 0:
        raise ValueError("Number of iterations must be a positive integer")

    calculate_series(iterations_number)

except ValueError as e:
    print(e)
