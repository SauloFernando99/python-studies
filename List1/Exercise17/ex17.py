#Days until birthday

birthday_month = int(input(("Insert the month of birthday: ")))
birthday_day = int(input(("Insert the day of birthday: ")))

actual_month = int(input(("Insert the actual month: ")))
actual_day = int(input(("Insert the actual day: ")))

def days_till_birthday(birthday_month, birthday_day, actual_month, actual_day):

    actual_date = ((actual_month - 1) * 30) + actual_day
    birthday_date = ((birthday_month - 1) * 30) + birthday_day

    if actual_date < birthday_date:
        days = birthday_date - actual_date
        return days
    elif actual_date > birthday_date:
        days = 365 - (actual_date + birthday_date)
        return days
    else:
        return 0

days = days_till_birthday(birthday_month, birthday_day, actual_month, actual_day)

if days != 0:
    print(f"There are still {days} days until your birthday")
else:
    print("Congratulations today is your birthday")
