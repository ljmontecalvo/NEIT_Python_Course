"""
Name: Landon Montecalvo
Lab #: Lab 1B
Date: 10.12.2023
Course: Programming Essentials with Python; SE116.11

Program Prompt: You want to develop a program that gathers the user’s hourly pay (use $14.50), hours worked (32/week),
and tax rate for a two-week period. Once you have this informa5on, you want to display the user’s Gross
Pay, Uncle Sam’s Share (the amount to be removed for taxes), and the User’s Net Pay. All calcula5ons should
be limited to run once, rather than numerous 5mes. Include in your flowchart the use of variables and print
statements. Use 20% for the tax rate.

Variable Dictionary:

hourlyPay: $/hour
hoursPerWeek: number of hours worked per week
grossPay: total untouched pay for 2 weeks
samsShare: the amount of tax for the grossPay
netPay: grossPay after samsShare tax deduction

"""
#-----------------------------------------------------------
# Vars
hourlyPay = 14.5
hoursPerWeek = 32
taxRate = 0.2

# Calculations
grossPay = 2 * (hoursPerWeek * hourlyPay) # Total untouched pay.
samsShare = grossPay * taxRate # Total tax for gross pay.
netPay = grossPay - samsShare # Total pay including tax deduction.

print("Your gross pay is: ${0:.2f}\nYour tax deduction is: ${1:.2f}\nYour net pay is: ${2:.2f}.".format(grossPay, samsShare, netPay)) # Console ouput.
print()
print("Thank you. Goodbye.") # Goodbye message.