startingBalance = float(input("Enter your starting balance: $"))
addingPerMonth = float(input("How much will you be adding per month?: $"))

balance = 0
balance += startingBalance

count = 0
while (count != (3 * 12)):
    balance += addingPerMonth
    count += 1

print("Your balance after 3 years is: ${0:.2f}".format(balance))
