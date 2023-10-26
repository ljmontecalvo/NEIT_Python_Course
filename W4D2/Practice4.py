count = 1

def ColorPick():
    color = input("Please enter your favorite color (this is not case sensitive): ")

    if (color.lower() == "blue"):
        print("The beautiful ocean is blue.")
    elif (color.lower() == "chartreuse"):
        print("Why is chartreuse your favorite color?")
    elif (color.lower() == "green"):
        print("Grass is green.")
    elif (color.lower() == "purple"):
        print("There is nothing I can think of that is purple. And don't say grapes. They are not purple.")
    elif (color.lower() == "orange"):
        print("Oranges are orange.")
    elif (color.lower() == "red"):
        print("Apples are red.")
    else:
        print(f"Your favorite color is {color}. Tremendous.")

ColorPick();

response = input("Would you like to go again? (yes/no): ")

while (response.lower() == "yes"):
    count += 1
    ColorPick()
    response = input("Would you like to go again? (yes/no): ")

print(f"You entered {count} numbers.")
