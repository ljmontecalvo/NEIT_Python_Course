bankBalance = float(input("Bank Balance: $"))
initbankBalance = bankBalance

monthlyDeposit = float(input("Monthly Deoposit: $"))
year = int(input("Year: "))
rate = float(input("Rate: "))

monthCount = 1
month = year * 12
rate /= 100

print("Bank Balance     Interest     Ending Balance")

while monthCount <= month:
    monthlyInterest = bankBalance * rate / 12
    endingBalance = bankBalance + monthlyInterest + monthlyDeposit

    print("{0:10.2f}\t{1:10.2f}\t{2:10.2f}".format(bankBalance, monthlyInterest, endingBalance))

    bankBalance = endingBalance

    if monthCount % 18 == 0:
        input(f"Last 18 months are listed. (Current month: {monthCount}) Press [ENTER] to continue.")

    monthCount += 1

rate *= 100

print("Initial Balance: ${0:.2f}\nMonthly Deopsit: ${1:.2f}\nYear: {2}\nRate: {3}\nEnding Balance: ${4:.2f}".format(initbankBalance, monthlyDeposit, year, rate, endingBalance))
print("Year: {0}, Final Balance: ${1}".format(year, endingBalance))
