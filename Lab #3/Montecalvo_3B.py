"""
Name: Landon Montecalvo
Lab #: Lab 3B
Date: 10.26.2023
Course: Programming Essentials with Python; SE116.11

Program Prompt: Write a program that will determine the change a user will receive
based on the total cost of all items purchased. The user should be
allowed to enter as many items as they want. When the user has finished
entering all of their items the program should display the total amount
for all items entered, then prompt the user for amount tendered (how
much money they will be paying with; assume they have enough money).
Print out the total cost of all items, amount tendered and the change
the user will receive. The total and change must be formatted to 2
decimal places.

Variable Dictionary:



"""
#-----------------------------------------------------------

items = []

def CreateItem():
    itemCost = float(input("Please enter item cost: $"))
    items.append(itemCost)

CreateItem()

response = input("Would you like to add another item? (yes/no): ")

while (response.lower() == "yes"):
    CreateItem()
    response = input("Would you like to add another item? (yes/no): ")

total = 0

for item in items:
    total += item

print("Your total is ${0:.2f}".format(total))

money = float(input("How much money will you be paying with? $"))

change = money - total

print("You purhcased {0} items, and your change is ${1:.2f}, have a nice day.".format(len(items), change))
