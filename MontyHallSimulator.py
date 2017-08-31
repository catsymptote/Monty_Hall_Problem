import random


# Variables you should change as you please.
#----------------------------
# How many times the simulation runs.
runs = 100000

# Strategy for choosing doors (0 == stay, 1 == change).
strategy = 1
#----------------------------


# Cars are good, goats are bad.
goat    = 0
car     = 1

# Amount of doors -1 (3-1 == 3 doors).
doorCount = 3-1

# List of doors (0 == goat, 1 == car).
#doors   = genDoors(doorCount)

chosenDoor = 0
finalDoor = 0


# Generate the empty list of goats (0)
#----------------------------
def genDoors (doorCount):
    doors = []
    for i in range(doorCount + 1):
        doors.append(0)

    #print ("doors \t" + str(doors))
    return doors


# Creates the list aka. decides where the goats (0) and the car (1) are.
#----------------------------
def doorListGen (doors):
    global chosenDoor
    #print (doors[0])
    door = random.randint(0, 2)

    if (    door == 0):
        doors[0] = car
        #print ("door == 0")
        #chosenDoor = 0
    elif (  door == 1):
        doors[1] = car
        #print ("door == 1")
        #chosenDoor = 1
    elif (  door == 2):
        doors[2]  = car
        #chosenDoor = 2
        #print ("door == 2")

    return doors


# Picks a random door (not currently used)
#----------------------------
def pickRandDoor ():
    door = random.randint(0, doorCount)
    #doors[door] = 1
    #print ("chosenDoor \t" + str(door))
    return door


# Openes a random goat-door
#----------------------------
def openDoor (doors):
    global chosenDoor
    #print (doors)
    goatDoors = []
    #print (doors)
    for i in range(doorCount + 1):
        if (doors[i] == goat and i != chosenDoor):
            goatDoors.append(i)

    randDoor = 0
    if (len(goatDoors) > 1):
        randDoor = random.randint(0, doorCount - 1)
        #print ("it's a list")
    #print ("randDoor \t" + str(randDoor))
    #print (goatDoors)
    #print (goatDoors[randDoor])
    return goatDoors[randDoor]

# Follows whichever strategy you have chosen, to pick a door (stay or change).
# chosenDoor is not currently used (associated with pickRandDoor())
#----------------------------
def doorStategy (doors, strategy, openedDoor):
    global chosenDoor
    #print (doors)
    #print ("openedDoor \t" + str(openedDoor))
    #print (chosenDoor)
    #print (openedDoor)

    availableDoors = []

    if (strategy == 0):
        return chosenDoor

    elif (strategy == 1):
        for i in range(doorCount + 1):
            if (i != openedDoor and i != chosenDoor):
                availableDoors.append(i)
        #print (availableDoors)
        randDoor = random.randint(0, doorCount - 2)
        return availableDoors[randDoor]


# Has the program loop ++.
#----------------------------
def runnerFunc ():
    global runs
    global chosenDoor
    global finalDoor
    #global doors
    wins = 0
    loss = 0

    for i in range(runs):
        doors = genDoors(doorCount)
        doorListGen (doors)
        #print(doors)
        chosenDoor = pickRandDoor()
        #print(doors)
        finalDoor = doorStategy (doors, strategy, openDoor(doors))
        #print (finalDoor)
        #print(doors)

        if (doors[finalDoor] == car):
            wins += 1
        elif (doors[finalDoor] == goat):
            loss += 1

        chosenDoor = 0
        finalDoor = 0
        #print ("---------------")

    if (strategy == 0):
        print ("Strat:\tstay")
    elif (strategy == 1):
        print ("Strat:\tchange")

    print ("wins: \t" + str(wins))
    print ("loss: \t" + str(loss))
    if (loss != 0):
        print ("ratio: \t" + str(100 * wins / runs) + "%")
    else:
        print ("ratio:\tundef")

    #print (doors)
    #print (chosenDoor)
    #print ("finalDoor \t" + str(finalDoor))
    #openDoor ()

# Starts the program
runnerFunc()






"""
# Testing of random ints and such
testSize = 1000000
test = []

count0 = 0
count1 = 0
count2 = 0

for i in range(testSize):
    test.append( random.randint(0, 2) )

for j in range (testSize):
    if (test[j] == 0):
        count0 += 1
    elif (test[j] == 1):
        count1 += 1
    elif (test[j] == 2):
        count2 += 1
    else:
        print ("dafuq just happened!? o_O")

print (count0)
print (count1)
print (count2)
"""


#random.randint(0, 2)
