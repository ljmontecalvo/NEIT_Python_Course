drinkingAge = 21
drivingAge = 16
votingAge = 18

ages = 0
count = 0

def AgeThing():
    age = int(input("How old are you?: "))

    ages += age

    if (age >= 16):
        print("You are old enough to drive.")
        if (age >= 18):
            print("You are old enough to vote.")
            if (age >= 21):
                print("You are old enough to drink.")
            else:
                print("You are not old enough to drink.")
        else:
            print("You are not old enough to vote.")
    else:
        print("You are not old enough to drive.")

AgeThing()

response = input("Would you like to go again? (yes/no): ")

while (response.lower() == "yes"):
    count += 1
    AgeThing()
    response = input("Would you like to go again? (yes/no): ")

print(f"The avergae age of the people entered was {ages / count} and there were {count} entries.")
