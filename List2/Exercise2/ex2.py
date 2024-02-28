#multiplication table

def multiply(chosen_number):
    if not (isinstance(chosen_number, int)) or chosen_number <= 0 or chosen_number > 10:
        raise ValueError("Chosen number must be an integer and be between 1 and 10")

    for i in range(1, 11):
        print(f"{chosen_number} x {i} = {chosen_number * i}")

try:
    chosen_number = int(input("Insert a integer number between 0 and 10: "))
    multiply(chosen_number)

except ValueError as e:
    print(e)