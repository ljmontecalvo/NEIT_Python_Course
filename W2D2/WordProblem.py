shirt_cost = 14.99
mug_cost = 8.99
shirt_count = 2
tax = 0.05

shirt_total = shirt_cost * shirt_count
subtotal = shirt_total + mug_cost

tax_cost = subtotal * tax
total = subtotal + tax

change = 100 - total

print("Total Cost is: ${:.2f}".format(total))
print("Change is: ${:.2f}".format(change))