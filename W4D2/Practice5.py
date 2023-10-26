drinkingAge = 21
drivingAge = 16
votingAge = 18

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
