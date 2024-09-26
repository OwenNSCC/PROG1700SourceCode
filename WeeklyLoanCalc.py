print("Welcome to the Short Term Loan Calculator")

A = float(input("Enter the amount of the loan: "))
r = float(input("Enter the annual interest rate in percentage: "))
n = int(input("Enter the number of years for the loan: "))

i = r / 5200

N = 52 * n

if i == 0 : weeklyPayment = A / N

else: weeklyPayment = (i * A) / (1 - (1 + i) ** -N)

print("Your weekly payment is: ${:.2f}".format(weeklyPayment))