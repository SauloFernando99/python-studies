# Arithmetic mean

total_sum = 0
count = 0

while True:
    number = int(input("Insert an integer number (or insert 0 to end the application): "))

    if number == 0:
        break

    if number % 2 == 0:
        count += 1
        total_sum += number
        mean = total_sum / count
        print(f"Current arithmetic mean: {mean}")
    else:
        print("Odd numbers aren't included in the current arithmetic mean calculation.")

if count > 0:
    print(f"Application finished. Final arithmetic mean: {mean}")
else:
    print("Application finished. No even numbers were entered.")
