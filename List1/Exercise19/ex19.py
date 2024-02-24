#Taxi profit

odometer_start = float(input("Insert the starter odometer count: "))
odometer_finish = float(input("Insert the final odometer count: "))
fuel_consumed = float(input("Insert the amount of fuel consumed in liters: "))
profit_from_passengers = float(input("Insert the amount received by passengers: "))

def consume_km_liter(odometer_start, odometer_finish, fuel_consumed):

    odometer_total = odometer_finish - odometer_start

    return fuel_consumed/odometer_total

def calculate_profit(fuel_consumed, profit_from_passengers):

    fuel_total_expenses = fuel_consumed * 2.50

    total_profit = profit_from_passengers - fuel_total_expenses

    return total_profit

print(f"Liters by kilometer fuel consume: {consume_km_liter(odometer_start, odometer_finish, fuel_consumed)}")
print(f"Daily profit: {calculate_profit(fuel_consumed, profit_from_passengers)} dollars")

if calculate_profit(fuel_consumed, profit_from_passengers) < 100:
    print("Cabby must increase his results")


