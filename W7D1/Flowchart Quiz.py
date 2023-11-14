"""
Variable Dictionary:

bankBalance: inputed starting balance for account.
initBankBalance: keeps starting value for future use.
monthlyDeposit: how much money goes into the account every month.
year: how many years the account will be active for.
rate: rate that interest increases each year.
monthCount: current month count.
month: converts the years into months.
monthlyInterest: new interest for current month.
endingBalance: final balance for each month.

"""

bankBalance = float(input("Bank Balance: $"))
initBankBalance = bankBalance

monthlyDeposit = float(input("Monthly Deoposit: $"))
year = int(input("Year: "))
rate = float(input("Rate: "))

monthCount = 1
month = year * 12
rate /= 100

print("Bank Balance  Interest  Ending Balance")

while monthCount <= month:
    monthlyInterest = bankBalance * rate / 12
    endingBalance = bankBalance + monthlyInterest + monthlyDeposit

    print("{0:10.2f}{1:10.2f}{2:10.2f}".format(bankBalance, monthlyInterest, endingBalance))

    bankBalance = endingBalance

    if monthCount % 18 == 0:
        input(f"Last 18 months are listed. (Current month: {monthCount}) Press [ENTER] to continue.")

    monthCount += 1

rate *= 100

print("Initial Balance: ${0:.2f}\nMonthly Deopsit: ${1:.2f}\nYear: {2}\nRate: {3}\nEnding Balance: ${4:.2f}".format(initBankBalance, monthlyDeposit, year, rate, endingBalance))
print("Year: {0}, Final Balance: ${1:.2f}".format(year, endingBalance))
