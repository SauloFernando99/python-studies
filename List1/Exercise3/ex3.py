#Read 5 numbers and count how many of then are bigger than 10

count = 0

for i in range(5):
    num = int(input(f"number {i+1}: "))
    if num > 10:
        count += 1

print(f"Numbers bigger than 10: {count}")


