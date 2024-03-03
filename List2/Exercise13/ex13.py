def calculate_mean(total_cars_sold, total_sold_value):
    mean = total_sold_value / total_cars_sold
    return mean


def main():
    highest_value_car_model = ""
    highest_value_car_price = 0
    cars_between_20000_and_30000 = 0
    seller_commission = 0
    total_sold_value = 0

    try:
        total_cars_sold = int(input("Insert how many cars were sold: "))

        if total_cars_sold < 0:
            raise ValueError("Total cars sold must be an positive integer number")
        else:
            for i in range(total_cars_sold):
                car_price = float(input(f"Insert car {i} price: "))
                car_model = str(input(f"Insert car {i} model: "))

                total_sold_value += car_price

                if car_price > highest_value_car_price:
                    highest_value_car_price = car_price
                    highest_value_car_model = car_model

                if 20000 < car_price < 30000:
                    cars_between_20000_and_30000 += 1

                if car_price <= 10000:
                    seller_commission += ((car_price / 100) * 10)
                else:
                    seller_commission += ((car_price / 100) * 11)

            mean_price = calculate_mean(total_cars_sold, total_sold_value)

            print(f"Seller commission: {seller_commission}")
            print(f"Most expensive car: {highest_value_car_model}")
            print(f"Number of cars with price between $20.000 and $30.000: {cars_between_20000_and_30000}")
            print(f"Mean cars price: {mean_price}")


    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
