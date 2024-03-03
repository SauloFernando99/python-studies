from random import randint


def main():
    random_number = 0
    count_less_than_10 = 0

    while random_number != 45:
        random_number = randint(0, 100)

        if random_number < THRESHOLD:
            count_less_than_10 += 1

    print(f"Total of random numbers lesser than {THRESHOLD} generated until 45 is generated: {count_less_than_10}")


if __name__ == "__main__":
    THRESHOLD = 10
    main()
