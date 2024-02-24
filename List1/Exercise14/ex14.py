#Voting class by age

age = int(input("Insert age of analysis: "))

if age < 16:
    print("Not elector")
elif 18 <= age < 65:
    print("Obligated elector")
else:
    print("Facultative elector")