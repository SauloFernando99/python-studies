#Age type

age = int(input("Insert age of analysis: "))

if 0 <= age < 18:
    print("Underage")
elif 18 <= age < 65:
    print("Adult")
elif age >= 65:
    print("Elderly")
else:
    print("Invalid age")