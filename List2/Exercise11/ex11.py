def calculate_months(company_a_production, company_b_production):
    company_a_total = company_a_production
    company_b_total = company_b_production
    total_months = 0

    while company_b_total <= company_a_total:
        company_a_total *= 1.15
        company_b_total *= 1.20
        total_months += 1

    return total_months


def main():
    company_a_production = 10000
    company_b_production = 8000

    print(f"Total months necessary for Company B to surpass Company A production: "
          f"{calculate_months(company_a_production, company_b_production)}")


main()
