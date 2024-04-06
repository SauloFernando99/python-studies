from List2.Exercise18.country import Country


def calculate_number_of_years_to_overcome(country1, country2):
    years_counter = 0
    total_country1_population = country1.population
    total_country2_population = country2.population

    while total_country1_population < total_country2_population:
        total_country1_population += ((total_country1_population * country1.birth_rate_percentage) / 100)
        total_country2_population += ((total_country2_population * country2.birth_rate_percentage) / 100)
        years_counter += 1

    return years_counter


def main():
    country1 = Country(5000000, 3)
    country2 = Country(7000000, 2)

    print(f"Number of years necessary to country1's population overcome country2's population: " +
          f"{calculate_number_of_years_to_overcome(country1, country2)}")


if __name__ == "__main__":
    main()
