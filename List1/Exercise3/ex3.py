#Land value calculator

width = float(input("Insert width: "))
length = float(input("Insert length: "))

area = width*length

city = input("The land is in São Paulo or Curitiba? ")

while city not in ["São Paulo", "Curitiba"]:
    city = input("Unknown city, choose São Paulo or Curitiba: ")

print(f"You choose: {city}")

if city == "São Paulo":
    print(f"Land price: {(area * 500.00)}")
else:
    print(f"Land price: {(area * 450.00)}")


