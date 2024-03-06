from random import randint


def odd_number_verifier(random_number):
    if not random_number % 2:
        return True


def lowest_number_verifier(random_number, lowest_number):
    if random_number < lowest_number:
        return random_number
    else:
        return lowest_number


def sum_numbers(random_number, numbers_sum):
    return numbers_sum + random_number


def print_info(odd_number_count, lowest_number, numbers_sum):
    print(f"Total sum of all the generated numbers: {numbers_sum}")
    print(f"Total odd numbers generated: {odd_number_count}")
    print(f"Lowest number generated: {lowest_number}")


def main():
    random_number = 0
    odd_numbers_count = 0
    lowest_number = 51
    numbers_sum = 0

    while random_number != 32:
        random_number = randint(0, 50)

        if odd_number_verifier(random_number):
            odd_numbers_count += 1

        lowest_number = lowest_number_verifier(random_number, lowest_number)

        numbers_sum = sum_numbers(random_number, numbers_sum)

    print_info(odd_numbers_count, lowest_number, numbers_sum)


if __name__ == "__main__":
    main()
