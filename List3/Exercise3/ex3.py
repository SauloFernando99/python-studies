def register_patients():
    patients = []
    keep_registering = "yes"

    while keep_registering == "yes":
        name = str(input("Insert patient's name: "))
        age = int(input("Insert patient's age: "))
        sex = str(input("Insert patient's sex (M or F): "))
        weight = float(input("Insert patient's weight: "))

        patient = [name, age, sex, weight]
        patients.append(patient)

        keep_registering = str(input("Do you want do register a new patient? (yes or no): "))

    return patients


def oldest_patient_with_weight_above_50(patients):
    highest_age = -1
    oldest_patient_name = ""

    for patient in patients:
        if patient[3] > 50 and patient[1] > highest_age:
            highest_age = patient[1]
            oldest_patient_name = patient[0]

    return oldest_patient_name


def mean_weight_female_over_30_years(patients):
    total_female = 0
    weight_sum = 0

    for patient in patients:
        if patient[2] == "F" and patient[1] > 30:
            total_female += 1
            weight_sum += patient[3]

    if total_female == 0:
        return 0

    return weight_sum / total_female


def amount_male_age_under_45(patients):
    male_count = 0

    for patient in patients:
        if patient[2] == "M" and patient[1] < 45:
            male_count += 1

    return male_count


def percentage_patients_older_than_59(patients):
    elders_count = 0

    for patient in patients:
        if patient[1] > 59:
            elders_count += 1

    if len(patients) == 0:
        return 0

    return (elders_count / len(patients)) * 100


def main():
    patients = register_patients()

    print(f"Oldest patient with weight over 50 kilos: {oldest_patient_with_weight_above_50(patients)}")
    print(f"Mean weight of the female patients older than 30 years: {mean_weight_female_over_30_years(patients)}")
    print(f"Amount of male patients with age under 45 years: {amount_male_age_under_45(patients)}")
    print(f"Percentage of elder patients: {percentage_patients_older_than_59(patients)}")


if __name__ == "__main__":
    main()
