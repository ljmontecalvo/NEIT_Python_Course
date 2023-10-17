"""
Name: Landon Montecalvo
Lab #: PRACTICE
Date: 10.17.23
Course: Programming Essentials with Python

Prompt: Write a program that determines a user's monthly budget.  Ask the user for the following data: monthly wage, monthly rent/mortgage payment, monthly food cost, monthly total bills.  Based on the user's monthly wage, determine what money they have "leftover" each month based on their rent, food, and bill monthly totals. Reprint all of the data from the user (with labels!) along with their money coming in (monthly wage), the total of their 3 big monthly costs, and the difference between the two ("leftover" money).

Variable Dictionary:

monthlyWage: monthly wage
monthlyRent: monthly rent
monthlyFood: monthly food cost
monthlyCost: monthly bills cost
expenses: total expenses for the month
leftover: leftover money after expenses

"""

# Input Variable Declaration
monthlyWage = float(input("Please enter monthly wage: $"))
monthlyRent = float(input("Please enter monthly rent: $"))
monthlyFood = float(input("Please enter monthly food: $"))
monthlyCost = float(input("Please enter monthly cost: $"))

# Calculations
expenses = monthlyRent + monthlyFood + monthlyCost
leftover = monthlyWage - expenses

# Outputs
print(f"Your monthly wage is ${monthlyWage}.")
print(f"Your monthly rent is ${monthlyRent}.")
print(f"Your monthly food is ${monthlyFood}.")
print(f"Your monthly cost is ${monthlyCost}.")

print(f"Your total expenses are ${expenses}.")
print(f"Your leftover money is ${leftover}.")
