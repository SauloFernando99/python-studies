def calculate_mean(subjects_number):
    age_sum = 0

    for i in range(subjects_number):
        try:
            age = int(input(f"Insert age for subject {i + 1}: "))

            if age < 0:
                raise ValueError("Age must be a positive integer")

            else:
                age_sum += age

        except ValueError as e:
            print(e)

    return age_sum / subjects_number


try:
    subjects_number = int(input("Insert the number of subjects: "))

    if subjects_number < 0:
        raise ValueError("Number of subjects must be a positive integer")

    else:
        print(f"Age mean of the {subjects_number} subjects: {calculate_mean(subjects_number)}")

except ValueError as e:
    print(e)
