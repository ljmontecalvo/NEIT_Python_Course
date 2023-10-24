"""
Name: Landon Montecalvo
Lab #: Lab 2A
Date: 10.24.2023
Course: Programming Essentials with Python; SE116.11

Program Prompt: You are currently working for a small start-up company that produces short “How-to” videos. The company is currently
producing videos for customers who need to know how to fix common networking problems. You oversee the company’s
network and the owner of the company has just informed you that the company will also be producing “How-to” videos
on how to install, configure and manage a Linux OS. You need to let the owner of the company know if you will have
enough storage on your current NAS (Network Attached Storage). You currently have 250 videos stored on your NAS
which occupy 1.4 TB of disk space. Your NAS has 8 TB of storage. The company is currently producing 15 videos a week
with an average file size of 5.6 GB. The company expects to triple that average once they start producing videos for the
OS. If the average file size of each video is 5.6 GB how long will it be before you run out of storage space? Tell the user
how many days left of storage are available just by making their current How-To videos, as well as how many days are left
if they started their How-To videos today (which increases the videos being produced weekly 3x). Every output value
should be format rounded to the 1st decimal place. Write a program that will determine how many days of storage is left
on the NAS. [Note: this means you will have two possibilities for days left of storage]

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
videoCount = 520
usedSpace = 1.4
totalSpace = 8
videosPerWeek = 15
avgVideoSpace = 5.6 / 1000 

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