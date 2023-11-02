import random

monstersAvailable = [1, 2, 3] # Which monsters can the player fight?
playerHealth = 100 # Init player health.
playerDamageMin = 10 # Init minium amount of damage that player can do.

monstersInfo = {
    "Frostclaw": {
        "damage": 10,
        "health": 90
    },
    "Venomspine": {
        "damage": 20,
        "health": 100
    },
    "Billy": {
        "damage": 30,
        "health": 120
    }
}

def Fight(monsterNumber, monsterName):
    monsterHealth = monstersInfo[monsterName]["health"] # Gets the current monster's health from the dictionary.
    monsterDamage = monstersInfo[monsterName]["damage"] # Gets the current monster's health from the dictionary.

    while playerHealth > 0:
        while monsterHealth > 0 :
            playerDamage = random.randint(playerDamageMin, playerDamageMin + 10)
            print(f"{name} hit the {monsterName} for {playerDamage}!")
            monsterHealth -= playerDamage

            monsterDamage = random.randint(monsterDamage, monsterDamage + 10)
            print(f"The {monsterName} hit {name} for {monsterDamage}!")
            playerHealth -= monsterDamage

    print("Uh-Oh! You died. Very sad.")

    print()

    playAgain = input("Would you like to try again? (yes/no): ")

    if playAgain.lower() == "yes": # Play again sequence logic.
        # Resets original variables.
        monstersAvailable = [1, 2, 3]
        playerHealth = 100
        playerDamageMin = 10
        FightNewMonster()
    else:
        print()
        print("Thank you for playing.")
        

def FightNewMonster():
    # List monster stats for player.
    print(f"There are {len(monstersAvailable)} that you can fight.")
    print(f"\tFrostclaw:\n\t\tMinimum Damage: 10\n\t\tHealth: 90")
    print(f"\tVenomspine:\n\t\tMinimum Damage: 20\n\t\tHealth: 100")
    print(f"\tBilly:\n\t\tMinimum Damage: 30\n\t\tHealth: 120")

    print()

    monsterToFight = input("Which monster would you like to fight?\n\tA: Frostclaw\n\tB:Venomspine\n\tC:Billy\nLetter: ") # Let player pick which monter they would like to fight.

    while not monsterToFight.lower() == "a" and not monsterToFight.lower() == "b" and not monsterToFight.lower() == "c": # Exception handling.
        monsterToFight = input("Which monster would you like to fight?\n\tA: Frostclaw\n\tB:Venomspine\n\tC:Billy\nLetter: ")
    
    if monsterToFight.lower() == "a": # If player picks option a.
        Fight(1, "Frostclaw")
    elif monsterToFight.lower() == "b": # If player picks option b.
        Fight(2, "Venomspine")
    else: # If player picks option c.
        Fight(3, "Billy")

name = input("Please enter your player name: ") # Stores player's name.
FightNewMonster()
