"""
Name: Landon Montecalvo
Lab #: Lab 6
Date: 11.28.2023
Course: Programming Essentials with Python; SE116.11

Program Prompt: Write a program that gives the user the following options:
My Basic Calculator
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers
5. Exit

Variable Dictionary:

num1: local 1st number var.
num2: local 2nd number var.
mode: local var that dicates which calculation is preformed.
response: input var for mode choice.
number1: input var for 1st number.
number2: input var for 2nd number.

"""
#-----------------------------------------------------------

# Functions
def Calculate(num1, num2, mode):
    """Calculates two numbers based on the mode input."""
    if mode == 1:
        number1 = float(input("Please enter the first number: "))
        number2 = float(input("Please enter the first number: "))   
        return number1 + number2
    elif mode == 2:
        number1 = float(input("Please enter the first number: "))
        number2 = float(input("Please enter the first number: "))   
        return number1 - number2
    elif mode == 3:
        print(num1 * num2)
    elif mode == 4:
        number1 = float(input("Please enter the first number: "))
        number2 = float(input("Please enter the first number: "))   
        return number1 / number2

# Print title and options.
print("Welcome to the Simple Calculator!\n")
print("Which calculation would you like to preform?:")
print("[1] Add two numbers.")
print("[2] Subtract two numbers.")
print("[3] Multiply two numbers.")
print("[4] Divide two numbers.")
print("[5] End.")

while True:
    response = int(input("Number: ")) # Get number input from user.

    if response == 1:
        Calculate(0, 0, 1) # Calculate with addition.
    elif response == 2:
        Calculate(0, 0, 2) # Calculate with subtraction.
    elif response == 3:
        number1 = float(input("Please enter the first number: ")) # Get number 1.
        number2 = float(input("Please enter the first number: ")) # Get number 2.
        Calculate(number1, number2, 3) # Calculate with multiplication.
    elif response == 4:
        Calculate(0, 0, 4) # Calculate with division.
    elif response == 5:
        break # End program.
