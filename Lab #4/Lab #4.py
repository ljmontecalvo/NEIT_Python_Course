"""
Name: Landon Montecalvo
Lab #: Lab 4
Date: 11.14.2023
Course: Programming Essentials with Python; SE116.11

Program Prompt: Write a program that will determine the change a user will receive based on the total cost of all
items they want to purchase. The user should be able to enter as many items as they want. After a user enters
an item’s cost, also ask them if this item will be taxed. If the item will be taxed, calculate the taxable amount.
The user should be able to use either a y or a Y to re-enter the loop and add another item cost as well as to
signal that the current item they have entered is taxable. When the user has finished entering all of their items
the program should display: the total number of items purchased, the total cost of all items, the total taxable
amount of taxed items, and the final total due (cost + tax). Once all of the values are printed, prompt the user
for the amount tendered (money they are paying with). Then, redisplay the final total cost of all items, the
amount tendered, and the change the user will receive. All monetary values must be formatted to display to
the 2nd decimal place and all decimals should align on top of one another when displayed (following the
format of a physical receipt).

Variable Dictionary:

items: list that holds the price of all the items.
tax: total tax for purchases.
taxRate: rate of tax.
priceResponse: price for current item.
taxResponse: yes or no if tax applies to item
repeatResponse: yes or no if user wants to add more items.
subtotal: subtotal.
finalCost: total cost after tax.
money: how much money the user is paying with.
change: the change that the program returns.

"""
#-----------------------------------------------------------

# Vars
items = []
tax = 0
taxRate = 0.07

while True:
    priceResponse = float(input(f"Please enter the price of item {len(items) + 1}: $")) # Gets price input.
    items.append(priceResponse) # Adds price to list.

    taxResponse = input("Will this item be taxed at checkout? (y/n): ")
    if taxResponse.lower() == "y":
        tax += (taxRate * priceResponse) # Adds tax to a total value.

    repeatResponse = input("Would you like to add another item to your cart? (y/n): ")
    if repeatResponse.lower() != "y":
        break # Continue if user is done.

subtotal = 0

for item in items:
    subtotal += item # Add subtotal for all values in list.

finalCost = subtotal + tax # Calculates total with tax.

# Prints out info.
print("You purchased {0} items.".format(len(items)))
print("Your subtotal is:\t${0:.2f}".format(subtotal))
print("Your tax due is:\t${0:.2f}".format(tax))
print("Your total cost is:\t${0:.2f}".format(finalCost))

money = float(input("Please enter the the amount of money you will be using to pay: $"))
change = money - finalCost # Calculates change.

# Prints out info.
print("Your total cost is:\t${0:.2f}".format(finalCost))
print("You paid with:\t\t${0:.2f}".format(money))
print("Your change is:\t\t${0:.2f}".format(change))