#BMI

weight = float(input("Input the weight: "))
height = float(input("Input the height: "))

bmi = weight/(height**2)

print(f"Body mass indice: {bmi}")

if bmi < 18.5:
    print("Weight above normal")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")

