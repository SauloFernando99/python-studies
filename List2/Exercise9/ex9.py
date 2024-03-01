from random import randint


def verify_even(number):
    if not number % 2:
        return True


def even_numbers_counter():
    number = 0
    even_numbers_count = 0

    while number != 50:
        number = randint(0, 100)

        if verify_even(number):
            even_numbers_count += 1

    return even_numbers_count


print(f"There was {even_numbers_counter()} even numbers generated")
