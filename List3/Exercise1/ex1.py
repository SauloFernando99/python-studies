def register_product():
    price = -1.0
    products = []

    while price != 0:
        name = str(input("Insert product's name: "))
        price = float(input("Insert product's price: "))

        if price == 0:
            break

        amount = int(input("Insert product's amount: "))
        category = str(input("Insert product's category (common or deluxe): "))

        product = [name, price, amount, category]
        products.append(product)

    return products


def deluxe_products_cheaper_than_2000(products):
    count = 0
    for product in products:
        if product[3] == "deluxe" and product[1] < 2000:
            count += 1

    return count


def deluxe_products_mean_price(products):
    total_deluxe_products = 0
    total_product_price_sum = 0

    for product in products:
        if product[3] == "deluxe":
            total_deluxe_products += 1
            total_product_price_sum += product[1]

    if total_deluxe_products == 0:
        return 0

    mean_price = total_product_price_sum / total_deluxe_products

    return mean_price


def most_expensive_product_with_amount_lower_than_50(products):
    product_name = ""
    most_expensive_product_price = 0

    for product in products:
        if product[2] < 50 and product[1] > most_expensive_product_price:
            most_expensive_product_price = product[1]
            product_name = product[0]

    return product_name


def percentage_of_products_with_price_between_100_and_200(products):
    total_products = len(products)
    price_100_200_count = 0

    for product in products:
        if 100 < product[1] < 200:
            price_100_200_count += 1

    if total_products == 0:
        return 0

    percentage = (price_100_200_count / total_products) * 100

    return percentage


def cheaper_product(products):
    product_name = ""
    lower_price = float('inf')

    for product in products:
        if product[1] < lower_price:
            lower_price = product[1]
            product_name = product[0]

    return product_name


def main():
    products = register_product()

    print(f"Amount of deluxe products cheaper than $2000,00: {deluxe_products_cheaper_than_2000(products)}")
    print(f"Deluxe products mean price: {deluxe_products_mean_price(products)}")
    print(
        f"Most expensive product with amount lower than 50: {most_expensive_product_with_amount_lower_than_50(products)}")
    print(
        f"Percentage of products with price between 100 and 200: "
        f"{percentage_of_products_with_price_between_100_and_200(products)}")
    print(f"Cheaper product: {cheaper_product(products)}")


if __name__ == "__main__":
    main()
