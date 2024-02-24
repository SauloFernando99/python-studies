#Kitchen dimensions for tiles


length = float(input("Insert length: "))
width = float(input("Insert width: "))
height = float(input("Insert height: "))

def AreaCalculator(length, width, height):

    wallType1 = (length * height) * 2
    wallType2 = (width * height) * 2

    totalWallArea = wallType1 + wallType2

    return totalWallArea

def TilesCalculator(length, width, height):

    totalArea = AreaCalculator(length, width, height)

    totalTilesBoxes = totalArea/2

    return totalTilesBoxes

print(f"Total number of tiles boxes is: {TilesCalculator(length, width, height)}")




