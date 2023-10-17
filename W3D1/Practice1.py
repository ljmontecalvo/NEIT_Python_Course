"""
Name: Landon Montecalvo
Lab #: PRACTICE
Date: 10.17.23
Course: Programming Essentials with Python

Prompt: Follow each flowchart to write a program in Python. Make sure to document your code as you go.

Variable Dictionary:

f_name: first name
l_name: last name
full_name: first and last name

tempF: input temp in F
tempC: output temp in C

tax: tax %
items: item count
item1: cost of item1
item2: cost of item2
item3: cost of item3
total_cost: subtotal
total_tax: total tax
total_final: total
money = amount of money the customer is paying with
change = change amount

"""

# ---------------------------------------------- #

# Input Variables
f_name = input("First Name: ")
l_name = input("Last Name: ")

# Join String
full_name = f_name + " " + l_name

# Output to Console
print("Your full name is {0}".format(full_name))

# ---------------------------------------------- #

tempF = float(input("Enter temperature in F: "))

tempC = (tempF - 32) * (5/9)

print("Your temperature in F was {0} and your temperature in C was {1}".format(tempF, tempC))

# ---------------------------------------------- #

# Constant Variables
tax = 0.07
items = 0

# Item Cost Calculations
item1 = float(input("Enter cost for Item 1: $"))
items =+ 1

item2 = float(input("Enter cost for Item 2: $"))
items += 1

item3 = float(input("Enter cost for Item 3: $"))
items += 1

# Processing
total_cost = item1 + item2 + item3
total_tax = total_cost * tax
total_final = total_cost + total_tax

# Ouput Info
print("You have {0} items. Your subtotal is ${1:.2f}. Your tax is ${2:.2f}. Your total is ${3:.2f}".format(items, total_cost, total_tax, total_final))

# Calculate Change
money = float(input("Please enter the amount of money you have: $"))

change = money - total_final

# Change Ouput
print("Your change is ${0:.2f}".format(change))
