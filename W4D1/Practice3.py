def NumberCheck():
    number = int(input("Please enter an integer: "))

    if (number > 0):
        print("Your number is positive.")

        if (number % 2 == 0):
            print("Your number is even.")
        else:
            print("Your number is odd.")
    elif (number < 0):
        print("Your number is negative.")

        if (number % 2 == 0):
            print("Your number is even.")
        else:
            print("Your number is odd.")
    else:
        print("Your number is neither positive or negative.")

NumberCheck()

response = input("Would you like to check another number? (yes/no): ")

while (response.lower() == "yes"):
    NumberCheck()
    response = input("Would you like to check another number? (yes/no): ")

print("Goodbye")
