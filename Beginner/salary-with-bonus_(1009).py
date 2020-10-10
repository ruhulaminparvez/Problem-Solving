n = input()
salary = float(input())
month_salary = float(input())

bonus = float(month_salary * (15/100))

total = salary + bonus

print("TOTAL = R$ %0.2f" %total)