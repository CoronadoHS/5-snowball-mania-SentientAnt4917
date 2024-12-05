''' 
    Name: Snowball-Mania
    Author: Ethan York
    Date: 12.3.24
    Class: AP Computer Science Principles
    Python: 
'''
import random
def main():
    # the main runner of the game
	  # welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    name = input ("What is your name?")
    opponent = input ("Who do you wanna fight?")
    print (name + " v.s " + opponent)
    
    players = []
    players.append(name)
    players.append(opponent)

    nextPlayer = ""
    while(nextPlayer != "DONE"):
        nextPlayer = input("Are there any more opponents?  If so, type them one at a time")
        players.append(nextPlayer)
    players.remove("DONE")

    choice = input("Do you want to choose who to throw the snowball at? (yes or no)")

    gameplay(name,players, choice)

def gameplay(name, players, manual):
    



    thrower = random.choice(players)
    target = thrower
    while(thrower == target):
        target = random.choice(players)
        if (thrower == name):
            if (manual == "yes"):
                target = input("You are up! Who do you want to throw the snowball at?  ")
            else: 
                 target = random.choice(players)
                 while(thrower == target):
                    target = random.choice(players)

    
    print (thrower + " is throwing a snowball at " + target)
    hitnum = random.radint(1,5)
    success = hitResult(hitnum)
    if (success == True):
        print("It's a hit! " + target + " is down!")
        players.remove(target)
    else:
        print("Unfortunately, " + thrower + " has very bad aim")
    print(players[0] + " is the best snowballer in all the land!!")

def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if (hitNum == 3):
        return True
    return False

main()
