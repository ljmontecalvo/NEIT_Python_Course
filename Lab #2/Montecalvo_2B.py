"""
Name: Landon Montecalvo
Lab #: Lab 2B
Date: 10.24.2023
Course: Programming Essentials with Python; SE116.11

Program Prompt: Rewrite Lab 2A but use input statements for: the available storage of the NAS in TB, number of
videos weekly, and the average size of each video in GB. Display all input information back to the user
and also include their days remaining of storage at their current rate as well as the storage days
remaining if the rate were to triple.

Variable Dictionary:

videoCount: video count
usedSpace: used space
totalSpace: total space
videosPerWeek: videos per week
avgVideoSpace: average How-To video space
newVideoSpace: average video space of OS videos
availableSpace: space tha isn't used in database
normalVideoSpacePerWeek: how much space do how-to videos take per week
newVideoSpacePerWeek: how much space do OS videos take per week
weeksOfNormalVideosLeft: how many weeks are left of how-to video storage
weeksOfNewVideosLeft: how many weeks are left of OS video storage
daysOfNormalVideosLeft: how many days are left of how-to video storage
daysOfNewVideosLeft: how many days are left of OS video storage

"""
#-----------------------------------------------------------

# Vars
videoCount = int(input("Please enter number of videos already in your database: "))
usedSpace = float(input("Please enter total used space (TB): "))
totalSpace = float(input("Please enter total space (TB): "))
videosPerWeek = int(input("Please enter videos per week: "))
avgVideoSpace = float(input("Please enter average video space (GB): ")) / 1000 

# Calculations
newVideoSpace = avgVideoSpace * 3
availableSpace = totalSpace - usedSpace
normalVideoSpacePerWeek = videosPerWeek * avgVideoSpace
newVideoSpacePerWeek = videosPerWeek * newVideoSpace
weeksOfNormalVideosLeft = availableSpace / normalVideoSpacePerWeek
weeksOfNewVideosLeft = availableSpace / newVideoSpacePerWeek
daysOfNormalVideosLeft = weeksOfNormalVideosLeft * 7
daysOfNewVideosLeft = weeksOfNewVideosLeft * 7

# Outputs
print("You have {0:.1f} days left of How-To Videos.".format(daysOfNormalVideosLeft))
print("You have {0:.1f} days left of OS Videos.".format(daysOfNewVideosLeft))