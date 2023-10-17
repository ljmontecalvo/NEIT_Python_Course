"""
Name: Landon Montecalvo
Lab #: PRACTICE
Date: 10.17.23
Course: Programming Essentials with Python

Prompt: Create an address label for a user.  Ask the user for: their first name, their last name, their street address, their current city, their current state abbreviated (Rhode Island -- RI), and their zip code.  Print the data they have given you in only 3 printed lines: Name (first + last), Address Line 1 (# and street), City Info (City, State and zip code).

Variable Dictionary:

firstName: first name
lastName: last name
address: address
city: city
state: state
zipCode: zip code
name: joined string first and last name
fullAddress: All vars joined into one big var.

"""
# Inputs
firstName = input("Please enter first name: ")
lastName = input("Please enter last name: ")

address = input("Please enter street address: ")
city = input("Please enter city: ")
state = input("Please enter state: ")
zipCode = input("Please enter zip code: ")

# String Concat.
name = firstName + " " + lastName

# Ouput
print(f"{name}\n{address}\n{city}, {state} {zipCode}")

# String Concat.
fullAddress = name + "\n" + address + "\n" + city + ", " + state + " " + zipCode

# Output
print(fullAddress)
