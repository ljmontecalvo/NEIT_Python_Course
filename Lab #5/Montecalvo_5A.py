"""
Name: Landon Montecalvo
Lab #: Lab 5A
Date: 11.16.2023
Course: Programming Essentials with Python; SE116.11

Program Prompt: Construct a program that will analyze potential voters. The program should generate the following
totals:
1. Number of individuals not eligible to register.
2. Number of individuals who are old enough to vote but have not registered.
3. Number of individuals who are eligible to vote but did not vote.
4. Number of individuals who did vote.
5. Number of records processed.
The program must prompt the user for the ID number, age, if the person is registered to vote, and
if the person voted. You will also have to prompt to see if the user has more data to enter.
All test values from the text table below should be entered by the user [ID, age, registered, voted]

Variable Dictionary:

userIDs: list of user ids
ages: list of ages
registeredStatus: list of the statuses of registration
votedStatus: list of votes
userId: user input id
age: user input age
registered: user input registration
voted: user input vote status
response: loop question
underAge: list of users not eligible to vote
notRegistered: list of users that are not registered to vote.
registeredDidNotVote: list of users that are registered but did not vote
voted: list of users that did vote
count: number of users

"""
#-----------------------------------------------------------

# Declare lists.
userIDs = []
ages = []
registeredStatus = []
votedStatus = []

while True:
    # Get account info.
    userId = input("User ID: ")
    age = int(input("Age: "))
    registered = input("Are you registered to vote? (y/n): ")
    voted = input("Did you vote? (y/n): ")

    # Append account info to corresponding list.
    userIDs.append(userId)
    ages.append(age)
    registeredStatus.append(registered.lower())
    votedStatus.append(voted.lower())

    # Loop statement.
    response = input("Would you like to enter more data? (y/n): ")

    if response.lower() != "y":
        break

# Prepare vars for output.
underAge = 0
notRegistered = 0
registeredDidNotVote = 0
voted = 0
count = 0

for i in range(0, len(userIDs)): # Loop the same amount of times as the account count.
    count += 1

    if ages[i] <= 18:
        underAge += 1 # If account is too young add one to under age.
    elif registeredStatus[i] == "n":
        notRegistered += 1 # If account is not registered add one to corresponding var.
    elif votedStatus[i] == "n":
        registeredDidNotVote += 1 # If account didn't vote add one to corresponding var.
    else:
        voted += 1 # If account voted add one to voted var.

print(f"Count of accounts not eligible for registration: {underAge}\nCount of accounts that are not registered: {notRegistered}\nCount of accounts that did not vote: {registeredDidNotVote}\nCount of accounts that voted: {voted}")
