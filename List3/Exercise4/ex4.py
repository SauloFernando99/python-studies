def print_sequence(numerator):
    print("S", end=" = ")
    plus_minus = " - "

    for i in range(numerator - 1):
        print(f"{i + 2}/{(i + 2) * (i + 2)}", end="")

        if i < numerator - 2:
            print(plus_minus, end="")

            if plus_minus == " - ":
                plus_minus = " + "
            else:
                plus_minus = " - "

    print("\n")

    return 0


def calculate_sum(numerator):
    values_sum = 0

    for i in range(numerator - 1):
        if (i + 2) % 2:
            values_sum -= (i + 2) / ((i + 2) * (i + 2))
        else:
            values_sum += (i + 2) / ((i + 2) * (i + 2))

    return values_sum


def main():
    numerator = int(input("Insert the numerator: "))

    print_sequence(numerator)

    print(f"Total sum: {calculate_sum(numerator)}")


if __name__ == "__main__":
    main()
