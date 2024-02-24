#Triangle

side1 = int(input("Insert size one: "))
side2 = int(input("Insert size two: "))
side3 = int(input("Insert size three: "))

if (side1 > (side2+side3) or side2 > (side3+side1) or side3 > (side2+side1)):
    print("Those sides cannot form a triangle")
else:
    if side1 == side2 == side3:
        print("Equilateral triangle")
    elif side1 == side2 != side3 or side1 == side3 != side2 or side2 == side3 != side1:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

