"""
Name: Landon Montecalvo
Lab #: Lab 5B
Date: 11.16.2023
Course: Programming Essentials with Python; SE116.11

Program Prompt: Write a program that will allow the user to enter as many IP addresses that they want (loop!) and
print out the IP address and its class. See KT's notes on .split() (posted in W7 “Notes”) on how to
break the IP address into its 4 octets. The IP address, when printed, should appear exactly as it did
when entered by the user. If the IP address is not a Class A, B, or C, the user should also be alerted
and the IP address should still be reprinted. The user should be able to enter either a y or Y to
continue the loop.

Variable Dictionary:

address: user input address
splitAddres: address split by "."
response: loop variable

"""
#-----------------------------------------------------------

while True:
    address = input("Please enter an IP address: ") # Get IP address from user.

    splitAddress = address.split(".")

    if int(splitAddress[0]) > 191 and int(splitAddress[0]) <= 223: # If address is 192 - 223.
        print(f"Address, {address} is class C.")
    elif int(splitAddress[0]) > 127: # If address is 128 - 191.
        print(f"Address, {address} is class B.")
    elif int(splitAddress[0] >= 1): # If address is 1 - 127.
        print(f"Address, {address} is class A.")
    else:
        print(f"Address, {address} does not fit into a class.")

    response = input("Would you like to enter more data? (y/n): ") # Loop statement.

    if response.lower() != "y":
        break

print("\nGoodbye!") # Goodbye message.
