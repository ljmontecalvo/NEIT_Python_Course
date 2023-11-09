"""
Name: Landon Montecalvo
Midterm Project
Date: 11.07.2023
Course: Programming Essentials with Python; SE116.11

Program Prompt: Make a project using the skills that we have cover in this class.

Variable Dictionary:
- `monsterHealth`: The current health of the monster in the fight.
- `monsterDamageMin`: The minimum damage that the monster can deal in the fight.
- `playerDamage`: The calculated player's attack damage for the current round.
- `playerHealth`: The player's health in the game.
- `monsterName`: The name of the monster in the fight.
- `playAgain`: User input for playing the game again.
- `frostclaw`: A boolean indicating if the player can fight the monster named "Frostclaw."
- `venomspine`: A boolean indicating if the player can fight the monster named "Venomspine."
- `billy`: A boolean indicating if the player can fight the monster named "Billy."
- `inputs`: A string used to prompt the player for input.
- `monsterToFight`: User input for selecting a monster to fight.
"""
#-----------------------------------------------------------

# Imports for utilities.
import random
import sys

# Import for the external variables script.
import vars

# Imports for colored console text.
from colorama import *
from termcolor import colored

init() # Function to initiate the library that does the console text coloring.

# Fight runs the main part of the game that allows the player to attack the monster and the monster to attack the player.
def Fight(monsterName):
    monsterHealth = vars.monstersInfo[monsterName]["health"] # Gets the current monster's health from the dictionary.
    monsterDamageMin = vars.monstersInfo[monsterName]["damage"] # Gets the current monster's health from the dictionary.

    while True: # Loops through the player and monster attack sequences.
        # Player Attack Sequence
        if vars.playerHealth > 0:
            if monsterHealth > 0:
                playerDamage = random.randint(vars.playerDamageMin, vars.playerDamageMin + 10) # Calculates the player's attack damage for this round.
                monsterHealth -= playerDamage   
                print(f"\n{name} hit the {monsterName} for {playerDamage}!")

                print(colored("\nScores:", "green"))
                print(colored(f"\t{name} - {vars.playerHealth}", "blue"))
                print(colored(f"\t{monsterName} - {monsterHealth}\n", "red"))

                input("Press [ENTER] to continue.")
            else:
                print(f"Wow! {name} killed the {monsterName}!")
                print(f"\n{name}'s health and attack damage has been upgraded by 10 points.")
                input("Press [ENTER] to continue.\n")
                vars.monstersAvailable.remove(monsterName) # Remove the monster name from the available list of monsters that the player is able to fight.
                vars.playerHealth = 100
                vars.playerDamageMin += 10
                FightNewMonster() # Let the player pick a new monster.
        else:
            print(f"Uh-Oh! {name} died. Very sad.\n")

            playAgain = input("Would you like to try again? (yes/no): ")

            if playAgain.lower() == "yes": # Play again sequence logic.
                # Resets original variables.
                vars.monstersAvailable = ["Frostclaw", "Venomspine", "Billy"]
                vars.playerHealth = 100
                vars.playerDamageMin = 10
                FightNewMonster() # Let the player pick a new monster.
            else:
                print("\nThank you for playing.")
                sys.exit() # Exits the script in a lazy way.

        # Monster Attack Sequence
        if vars.playerHealth > 0:
            if monsterHealth > 0:
                monsterDamage = random.randint(monsterDamageMin, (monsterDamageMin + 10)) # Calculates the monster's attack damage for this round.
                vars.playerHealth -= monsterDamage
                print(f"\nThe {monsterName} hit {name} for {monsterDamage}!")

                print(colored("\nScores:", "green"))
                print(colored(f"\t{name} - {vars.playerHealth}", "blue"))
                print(colored(f"\t{monsterName} - {monsterHealth}\n", "red"))

                input("Press [ENTER] to continue.")
            else:
                print(f"Wow! {name} killed the {monsterName}!")
                print(f"\n{name}'s health and attack damage has been upgraded by 10 points.")
                input("Press [ENTER] to continue.\n")
                vars.monstersAvailable.remove(monsterName)
                vars.playerHealth = 100
                vars.playerDamageMin += 10
                FightNewMonster()
        else:
            print(f"Uh-Oh! {name} died. Very sad.\n")

            playAgain = input("Would you like to try again? (yes/no): ")

            if playAgain.lower() == "yes": # Play again sequence logic.
                # Resets original variables.
                vars.monstersAvailable = ["Frostclaw", "Venomspine", "Billy"]
                vars.playerHealth = 100
                vars.playerDamageMin = 10
                FightNewMonster()
            else:
                print("\nThank you for playing.")
                return

def FightNewMonster():
    if len(vars.monstersAvailable) == 0:
        print("Amazing, you completed the game.")
        sys.exit()

    # List monster stats for player.
    print(f"There are {len(vars.monstersAvailable)} monsters that you can fight.")

    # This section is the logic for which monsters to show in the menu based on what monsters the player has already fought.
    frostclaw = False
    venomspine = False
    billy = False

    for monster in vars.monstersAvailable:
        if monster == "Frostclaw":
            frostclaw = True
        if monster == "Venomspine":
            venomspine = True
        if monster == "Billy":
            billy = True

    inputs = ""

    # Concatenates a string to ask for input based on the monsters that list above.
    if frostclaw:
        print(f"\tFrostclaw (Easy):\n\t\tMinimum Damage: 10\n\t\tHealth: 90")
        inputs += "\n\tA: Frostclaw"
    if venomspine:
        print(f"\tVenomspine (Medium):\n\t\tMinimum Damage: 20\n\t\tHealth: 100")
        inputs += "\n\tB: Venomspine"
    if billy:
        print(f"\tBilly (Difficult):\n\t\tMinimum Damage: 30\n\t\tHealth: 120")
        inputs += "\n\tC: Billy"

    inputs += "\nLetter: "

    print()

    monsterToFight = input(colored(inputs, "blue")) # Let player pick which monter they would like to fight.

    while not monsterToFight.lower() == "a" and not monsterToFight.lower() == "b" and not monsterToFight.lower() == "c": # Exception handling.
        monsterToFight = input(colored(inputs, "blue"))
    
    if monsterToFight.lower() == "a": # If player picks option a.
        Fight("Frostclaw")
    elif monsterToFight.lower() == "b": # If player picks option b.
        Fight("Venomspine")
    else: # If player picks option c.
        Fight("Billy")

name = input(colored("Please enter your player name: ", "red")) # Stores player's name.
FightNewMonster()
