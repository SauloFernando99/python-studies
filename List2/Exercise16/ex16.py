def find_biggest_number(total_numbers_to_be_inserted):
    biggest_number = -1

    for i in range(total_numbers_to_be_inserted):
        try:
            number = int(input(f"Insert the {i + 1}º positive number: "))

            if number < 0:
                raise ValueError("Only positive numbers are accepted")

            else:
                biggest_number = compare_numbers(biggest_number, number)

        except ValueError:
            return ValueError

    return biggest_number


def compare_numbers(biggest_number, number):
    if biggest_number > number:
        return biggest_number
    else:
        return number


def main():
    try:
        total_numbers_to_be_inserted = int(input("Insert a positive integer number to be the amount of numbers whose "
                                                 "will be insert: "))

        if total_numbers_to_be_inserted <= 0:
            raise ValueError("Only positive integer numbers are accepted")

        else:
            found_value = find_biggest_number(total_numbers_to_be_inserted)

            if found_value == ValueError:
                print("A invalid number was inserted, please restart from the beginning")
            else:
                print(f"The biggest number is: {found_value}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
