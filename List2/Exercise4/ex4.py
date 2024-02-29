# Fibonacci

def print_fibonacci_sequence(count_number):
    a = 0
    b = 1

    print(a)
    print(b)

    num_iterations = count_number - 2

    for i in range(num_iterations):
        c = a + b
        print(c)
        a = b
        b = c

try:
    count_number = int(input("Insert how many number the sequence must show: "))

    if count_number <= 0 or not isinstance(count_number, int):
        raise ValueError("Input must be a positive integer")

    else:
        if count_number == 1:
            print(0)

        elif count_number == 2:
            print(0)
            print(1)

        else:
            print_fibonacci_sequence(count_number)

except ValueError as e:
    print(e)
