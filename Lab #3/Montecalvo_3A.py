"""
Name: Landon Montecalvo
Lab #: Lab 3A
Date: 10.25.2023
Course: Programming Essentials with Python; SE116.11

Program Prompt: This program will be similar to W3 in class lab (Lab 1B with
input()), but you will also include a loop, totaling variables, and a
counter. This program should ask an employer (the user of the
program) to enter an employee’s name, hours worked in a week, and
hourly wage. After this data has been input into the program, print
to the user the employee’s name, gross pay for one week, taxes due
for one week (use 20%), and this employee’s net pay. Then, allow the
user to enter a new employee’s information by asking if they would
like to. If the user does have another employee to enter, repeat the
processes again: ask for data, run calculations, and display
individual employee’s information. When the user decides they no
longer have data to enter, display to them the total number of
employees entered during the program session and the totals of gross
pay, tax amount, and net across all employees entered.
All money should be format rounded to the second decimal place and
clearly labeled. All money should have decimals in alignment with
one another.

Variable Dictionary:

totalGrossPay: total gross pay for all employees
totalTaxShare: total tax share for all employees
totalEmployess: number of employees
name: name of employee
hoursPerWeek: hours per week the employee worked
hourlyWage: amount of money the employee makes per hour
grossPay: gross pay for an employee
taxShare: tax share for an employee
netPay: net pay for an employee
response: user input to continue while loop

"""
#-----------------------------------------------------------

# Vars
totalGrossPay = 0
totalTaxShare = 0
totalNetPay = 0
totalEmployees = 0

def PaymentCalculations():
    global totalGrossPay
    global totalTaxShare
    global totalNetPay
    global totalEmployees

    name = input("Enter name: ")
    hoursPerWeek = float(input("Enter hours worked per week: "))
    hourlyWage = float(input("Enter hourly wage: $"))
    print()

    grossPay = hoursPerWeek * hourlyWage
    taxShare = grossPay * 0.2
    netPay = grossPay - taxShare

    totalGrossPay += grossPay
    totalTaxShare += taxShare
    totalNetPay += netPay
    totalEmployees += 1

    print("Employee Name: {0}; Gross Pay: {1:.2f}; Tax Share: {2:.2f}; Net Pay: {3:.2f}.".format(name, grossPay, taxShare, netPay))
    print()

PaymentCalculations()

response = input("Would you like to enter another employee's information? (yes/no): ")

while (response.lower() == "yes"):
    PaymentCalculations()
    response = input("Would you like to enter another employee's information? (yes/no): ")

print("Total Employees:  {0}\nTotal Gross Pay: ${1:.2f}\nTotal Tax Share: ${2:.2f}\nTotal Net Pay:   ${3:.2f}".format(totalEmployees, totalGrossPay, totalTaxShare, totalNetPay))
