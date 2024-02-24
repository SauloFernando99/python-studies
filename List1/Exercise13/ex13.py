# Sum of ages

age1, age2, age3 = map(int, input("Insert three ages: ").split())

total_sum = age1 + age2 + age3

if total_sum >= 100:
    print("Sum is bigger or equal to 100")
else:
    print("Sum is under 100")