from random import randint


def calculate_mean(numbers_count, numbers_sum):
    numbers_mean = numbers_sum / numbers_count
    return numbers_mean


def show_results(numbers_count, numbers_sum, numbers_mean):
    print("Showing results:")
    print(f"Total numbers generated: {numbers_count}")
    print(f"Sum of the generated numbers: {numbers_sum}")
    print(f"Mean of the generated numbers: {numbers_mean}")


def main():
    random_number = 0
    numbers_count = 0
    numbers_sum = 0

    while random_number != 88:
        random_number = randint(0, 100)

        numbers_count += 1
        numbers_sum += random_number

    numbers_mean = calculate_mean(numbers_count, numbers_sum)

    show_results(numbers_count, numbers_sum, numbers_mean)


main()
