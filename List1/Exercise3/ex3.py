#Find how many numbers between a list of 5 number are bigger than 10

numbers = []
count = 0

for i in range(5):
    num = int(input(f"number {i+1}: "))
    numbers.append(num)

for num in numbers:
    if num > 10:
        count += 1

print(f"Numbers bigger than 10: {count}")


