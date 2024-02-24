# Credit line

salary = float(input("Insert functionary salary: "))
installment = float(input("Insert installment: "))


def CreditLiberation(salary, installment):
    if installment <= (salary * 0.3):
        print("Credit approved")
    else:
        print("Credit reproved")


CreditLiberation(salary, installment)
