def is_prime_number(number):
    if number < 2:
        return "no"

    for i in range(2, number):
        if number % i == 0:
            return "no"

    return "yes"


def print_result(number):
    prime_number = is_prime_number(number)

    if prime_number == "yes":
        print(f"The number {number} is a prime number")
    else:
        print(f"The number {number} isn't a prime number")


def main():
    number = int(input("Insert number: "))
    print_result(number)


if __name__ == "__main__":
    main()
