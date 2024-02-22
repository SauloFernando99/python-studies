# Find the biggest number between 3 numbers

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

if (number1 > number2 and number1 > number3):
    print(f"First number: {number1}, is the biggest")
if (number2 > number1 and number2 > number3):
    print(f"Second number: {number2}, is the biggest")
if (number3 > number1 and number3 > number2):
     print(f"Third number: {number3}, is the biggest")