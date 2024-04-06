from List2.Exercise17.person import Person


def register_subjects(subjects_number):
    subjects_list = []
    for i in range(subjects_number):
        age = int(input(f"Insert subject {i+1} age: "))
        weight = int(input(f"Insert subject {i+1} weight in kilos: "))
        height = int(input(f"Insert subject {i+1} height in centimeters: "))

        people = Person(age, weight, height)

        subjects_list.append(people)

    return subjects_list


def calculate_age_mean(subjects_list):
    age_sum = 0

    for people in subjects_list:
        age_sum += people.age

    age_mean = age_sum / len(subjects_list)

    return age_mean


def weight_above_90_and_height_under_150(subjects_list):
    subjects_count = 0

    for people in subjects_list:
        if people.weight > 90 and people.height < 150:
            subjects_count += 1

    return subjects_count


def percent_age_between_10_30_height_above_90(subjects_list):
    height_above_190_count = 0
    both_conditions_meet_count = 0

    for people in subjects_list:
        if 10 < people.age < 30 and people.height > 190:
            both_conditions_meet_count += 1

        if people.height > 190:
            height_above_190_count += 1

    if height_above_190_count == 0:
        return 0

    subjects_percent = (both_conditions_meet_count / height_above_190_count) * 100

    return subjects_percent


def print_data(mean, count, percentage):
    print(f"Total age mean: {mean}")
    print(f"Number of people with weight above 90 kilos and height under 150cm: {count}")
    print(
        f"Percentage of people with age between 10 and 30 years within the people with height above 190: {percentage}%")


def main():
    subjects_number = int(input("Insert the number of people: "))

    subjects_list = register_subjects(subjects_number)
    mean = calculate_age_mean(subjects_list)
    count = weight_above_90_and_height_under_150(subjects_list)
    percentage = percent_age_between_10_30_height_above_90(subjects_list)

    print_data(mean, count, percentage)


if __name__ == "__main__":
    main()
