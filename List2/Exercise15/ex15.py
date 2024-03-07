def find_even_numbers(first_number, second_number):
    even_numbers_list = []

    for i in range(second_number - first_number):
        if not (i + first_number) % 2:
            even_numbers_list.append(i + first_number)

    return even_numbers_list

def print_even_numbers(even_number_list):
    print("Even numbers in the interval:")

    for i in range(len(even_number_list)):
        print(f"{i + 1}: {even_number_list[i]}")

def sum_even_numbers(even_number_list):
    even_numbers_sum = 0

    for i in range(len(even_number_list)):
        even_numbers_sum += even_number_list[i]

    return even_numbers_sum

def print_even_numbers_sum(even_numbers_sum):
    print(f"Total sum of all even numbers in the interval: {even_numbers_sum}")


def main():
    first_number = int(input("Insert a integer number to be the beginning of the limit: "))

    try:
        second_number = int(input("insert a integer number higher than the first one to be the final of the limit: "))

        if second_number < first_number:
            raise ValueError("Second number must be higher than the first one")
        else:
            even_numbers_list = find_even_numbers(first_number, second_number)
            print_even_numbers(even_numbers_list)
            even_numbers_sum = sum_even_numbers(even_numbers_list)
            print_even_numbers_sum(even_numbers_sum)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()