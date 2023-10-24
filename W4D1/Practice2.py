name = input("Please enter your name: ")

print(f"Hello, {name}.")
response = input("Would you like to see this message again? (yes/no): ")

count = 0

while (response.lower() == "yes"):
    count += 1
    print(f"Hello, {name}.")
    response = input("Would you like to see this message again? (yes/no): ")

print(f"Goodbye, count was {count}.")
