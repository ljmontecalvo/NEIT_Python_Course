bigMacCount = int(input("How many Big Macs did you eat: "))
friesCount = int(input("How many Medium Shakes did you eat: "))
shakesCount = int(input("How many Small Shakes did you eat: "))

bigMacCals = bigMacCount * 563
friesCals = friesCount * 378
shakesCals = shakesCount * 530

totalCals = bigMacCals + friesCals + shakesCals

hoursToBurnJogging = totalCals / 398
hoursToBurnRunning = totalCals / 557

print("It will take {0:.1f} of jogging to burn off {1} calories.".format(hoursToBurnJogging, totalCals))
print("It will take {0:.1f} of running to burn off {1} calories.".format(hoursToBurnRunning, totalCals))