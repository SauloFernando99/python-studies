# Fibonacci over 500

def print_fibonacci_sequence_over_500():
    a = 0
    b = 1
    c = 0

    print(a)
    print(b)

    while c < 500:
        c = a + b
        print(c)
        a = b
        b = c


print("Fibonacci sequence:")
print_fibonacci_sequence_over_500()
