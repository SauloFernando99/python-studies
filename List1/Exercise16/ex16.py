#Days for new year

month = int(input("Insert the month number: "))
day = int(input("Insert the day number: "))

def days_till_new_year(month, day):

    actual_date = ((month-1) * 30) + day
    days_until_new_year = 365 - actual_date

    return days_until_new_year

print(f"There are {days_till_new_year(month, day)} days till new year")