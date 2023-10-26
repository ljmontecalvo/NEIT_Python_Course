number = int(input("Please enter an integer: "))

if (number < 0):
    print("Number is negative.")
elif (number > 100):
    print("Number is greater than 100.")
elif (number == 7):
    print("This is possibly Corey's favorite number.")
else:
    print(f"Number is {number}.")