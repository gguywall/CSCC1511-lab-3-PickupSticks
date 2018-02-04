#Program Name: PickUpSticks.py
#Author: Gary Wallace
#February 1, 2018

#import random

maxSticks = 4
minSticks = 1
totalSticks = 13
currentPlayer = "Player 1"
sticksLeft = totalSticks
sticksTaken = 0

print("\tWelcome to Pick Up Sticks.")
print("\nEach player takes turns picking up from 1")
print("to 4 sticks from a pile of 13 sticks.")
print("Whoever picks up the last stick wins.")

print("\nThere are ", sticksLeft, "stick(s) left.")

while sticksLeft:
    print("\n", currentPlayer)
    sticksTaken = int(input("- how many sticks will you take? "))
    while (sticksTaken > maxSticks) or (sticksTaken < minSticks):
        print("You can't take ", sticksTaken, " sticks.")
        sticksTaken = int(input("- how many sticks will you take? "))
    #Sticks taken are between min and max sticks. 
    #Check to see if new total is less than zero
    if(sticksLeft - sticksTaken) < 0:
        print("You can't take that many sticks")
    else:    
        sticksLeft = sticksLeft - sticksTaken
        #print("\nThere are", sticksLeft, "stick(s) left.")
    #check for zero sticks
    if sticksLeft == 0:
        print(currentPlayer, "wins.")
    else:
            #Next player
            if currentPlayer == "Player 1":
                currentPlayer = "Player 2"
            else:
                currentPlayer = "Player 1"
    
    
