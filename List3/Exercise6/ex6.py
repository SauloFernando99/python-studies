def is_prime_number(number):
    if number < 2:
        return "no"

    for i in range(2, number):
        if number % i == 0:
            return "no"

    return "yes"


def verify_prime_numbers(number):

    for i in range(2, number):
        prime_number = is_prime_number(i)

        if prime_number == "yes":
            print(f"{i}", end=" ")


def main():
    number = int(input("Insert number: "))

    print("Prime numbers: ", end="")
    verify_prime_numbers(number)


if __name__ == "__main__":
    main()
