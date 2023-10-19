"""
Name: Landon Montecalvo
Lab #: Lab 1B
Date: 10.12.2023
Course: Programming Essentials with Python; SE116.11

Program Prompt: This is the same as Lab 1B except instead of using assignment statements for hours worked, hourly rate,
and tax rate, use the input statement to assign values to variables. Ask the user to input their hourly
rate and their hours worked in a week, as well as the number of weeks for this pay period. You may still
use 20% for the tax rate or ask the user for their tax rate as a whole number percentage (including this
additional input statement, if calculations and final values are correct, will award you +5 bonus points on
this in-class lab!). Once you have this information, you want to display the user’s Gross Pay, Uncle Sam’s
Share, and the User’s Net Pay. All calculations should be limited to run once, rather than numerous
times. Include in both your pseudocode and flowchart the use of variables and print statements.

Variable Dictionary:

hourlyPay: $/hour
hoursPerWeek: number of hours worked per week
grossPay: total untouched pay for 2 weeks
samsShare: the amount of tax for the grossPay
netPay: grossPay after samsShare tax deduction

"""
#-----------------------------------------------------------

# Vars
hourlyPay = float(input("Please enter hourly pay: $"))
hoursPerWeek = float(input("Please enter the number of hours you work in a week: "))
taxRate = int(input("Please enter your area's income tax (without % sign): "))

# Calculations
taxRate = taxRate / 100 # Convert whole number percent to deciemal.
grossPay = 2 * (hoursPerWeek * hourlyPay) # Total untouched pay.
samsShare = grossPay * taxRate # Total tax for gross pay.
netPay = grossPay - samsShare # Total pay including tax deduction.

print("Your gross pay is: ${0:.2f}\nYour tax deduction is: ${1:.2f}\nYour net pay is: ${2:.2f}.".format(grossPay, samsShare, netPay)) # Console ouput.
print()
print("Thank you. Goodbye.") # Goodbye message.