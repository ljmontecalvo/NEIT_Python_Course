#W2D1 - Introduction to Python
#Documentation/Comments are NOT read by the comp

#Required Documentaiton for Lab Files:
#      *Name: Landon Montecalvo
#      *Lab: Demo W2
#      *Date: 10.10.23
#      *Problem Prompt/Explanation: Trip Cost Calculator
#      *Variable Dictionary:
#            distance - Distance traveled one way.
#            tolls - Cost of tolls.
#            gasPerGallon - Miles per gallon.
#            stops - Amount of stops for the trip.
#            hotelCost - Cost of hotels.
#            milesPerGallon - Miles per gallon.
#VARIABLES
#a friendly name for data within our code
#assignment of data to a variable is done using a = (assignment/storage) once done, the comp recognizes the name but will replace with data

name = "Landon"
#storage occurs from right to left
#string value of "Corey" stored/assigned to variable called 'name'

#Variable Naming Conventions (Rules)
#  *names are descriptive
#  1. Corey's RULE --> must start with a lowercase letter
#  2. can contain upper/lower alpha chars
#  3. can contain digits 0 - 9
#  4. can contain '_' underscore (only valid special char)
#  5. names are cAsE sEnSiTiVe; name != Name != NAME
#  6. one variable -> one value

#MATH PROCESSING
#      +      Addition
#      -      Subtraction
#      *      Multiplication
#      /      Division

#Order of Operations: PEMDAS
#                    Parenthesis
#                    Exponents
#                    Multiplication
#                    Division
#                    Addition
#                    Subtraction

#DATA TYPES - different types of data (info)
#two main groups - numbers and non-numbers

#NUMBER DATA TYPES
#    integer (int) - whole numbers
#    float (float) - any number, can contain decimals

#NON-NUMBER DATA TYPE
#    string (str) - any characters, held in ""

#----------------------------------------------

# Output - Display data OUT of the program.
print("Hello, World")
print(name)

#Display stored value of name + label.
print(f"Hi there, {name}.")
print(f"{name} is my name.")

#Display blank line.
print()
print("This is after a one line spacing.")

#----------Cross Country Trip-------------------

distance = 3158
mpg = 32
tolls = 23
gasPerGallon = 1.8
hotelPrice = 120
stops = 3

# Step 2: Data Manipulation

totalGallons = distance / mpg
costOfGas = totalGallons * gasPerGallon
hotelCost = stops * hotelPrice

onewayCost = costOfGas + hotelCost + tolls
roundTripCost = onewayCost * 2

print("The one way cost is ${:.2f}".format(onewayCost))
print("The round trip cost is ${:.2f}".format(roundTripCost))

print()

print("Another way to write this is:")
print("\tThe oneway cost is ${0:.2f}.\n\tThe round trip cost is ${1:.2f}.".format(onewayCost, roundTripCost))
