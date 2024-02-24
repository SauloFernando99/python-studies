# Possible classes

age = int(input("Insert age: "))
sex = str(input("Insert sex (M or F): ").upper())
salary = float(input("insert salary: "))

if sex == "M" and (20 > age > 18 or 31 < age):
    print("Masculine, with more than 18 years old")
elif sex == "F" and salary > 50000 and age > 40:
    print("Female, salary over $50000, age over 40")
elif sex in ["M", "F"] and 20 < age < 30:
    print("Masculine or feminine, age between 20 and 30 years old")
else:
    print("Don't fit any of the previous possibilities")