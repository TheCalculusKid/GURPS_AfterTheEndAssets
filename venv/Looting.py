import random

def twodice():
    results = random.randint(1, 6) + random.randint(1, 6)
    return results
def threedice():
    results = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    return results
def randomindexer():
    randomvalue=threedice()
    if randomvalue <=5:
        index = 0
    if 5 < randomvalue <= 8:
        index = 1
    if 8 < randomvalue <= 11:
        index = 2
    if 11 < randomvalue <= 14:
        index = 3
    if 14 < randomvalue <= 16:
        index = 4
    if 16 < randomvalue <= 18:
        index = 5
    return index
minorFind = [
    'Ammo worth $' + str(twodice() * 20),
    'Miscellaneous gear worth $' + str(twodice() * 20),
    'Junk worth $' + str(twodice() * 20),
    'Location-specific stuff worth $' + str(twodice() * 20),
    'Consumables worth $' + str(twodice() * 20),
    'A weapon or armor worth approximately $' + str(twodice() * 50)
]
majorFind = [
    'Consumables worth $' + str(twodice() * 200),
    'Junk worth $' + str(twodice() * 50),
    'Location-specific stuff worth $' + str(twodice() * 50),
    'Ammo worth $' + str(twodice() * 50),
    'Miscellaneous gear worth $' + str(twodice() * 100),
    'A weapon or armor worth approximately $' + str(twodice() * 200)
]
amazingFind = [
    'Miscellaneous gear worth $' + str(twodice() * 1000),
    'Consumables worth $' + str(twodice() * 500),
    'Location-specific stuff worth $' + str(twodice() * 250),
    'Ammo worth $' + str(twodice() * 500),
    'A weapon or armor worth approximately $' + str(twodice() * 100),
    'A vehicle worth approximately $' + str(threedice()*threedice() * 200)
]
print('''
Commercial:             1
Corporate/Trade:        2
Encampment:             3
Food:                   4
Industrial/Research:    5
Medical:                6
Military/Police         7
Residental:             8
Transport:              9
''')
location = int(input("Input the number that corresponds to the looting location: "))

print('''
Unlooted:               1
Semi-Looted:            2
Looted:                 3
''')
level = int(input("Input the number that corresponds to the looting location: "))


Array = [
    [0, 3, 5, "Stash on 6 or less", "Location Specific Stuff: Miscellaneous equipment"],
    [2, 4, 5, "Stash on 6 or less", "Location Specific Stuff: Computers; tools"],
    [0, 2, 4, "Stash on 5 or less", "Location Specific Stuff: Rations; ammo; weapons"],
    [1, 3, 5, "Stash on 5 or less", "Location Specific Stuff: Canned food; common drugs"],
    [2, 4, 6, "Stash on 7 or less", "Location Specific Stuff: Tools; scientific gear; computers"],
    [1, 4, 6, "Stash on 6 or less", "Location Specific Stuff: Medical supplies; experimental consumables"],
    [0, 3, 6, "Stash on 5 or less", "Location Specific Stuff: Ammo; weapons; law-enforcement gear"],
    [0, 2, 4, "Stash on 7 or less", "Location Specific Stuff: Junk"],
    [0, 3, 6, "Stash on 5 or less", "Location Specific Stuff: Vehicular parts (for repair); fuel"]
]
running = True
while running:
    successes = int(input("input scavenging successess (or 50 for critical success): "))
    try:
        modSuccess = successes - Array[location - 1][level - 1]
    except:
        modSuccess = successes
    print('######################################################################################')
    index = int(randomindexer())
    if modSuccess >= 45:
        print("amazing find: ",amazingFind[index])
        print('('+Array[location - 1][3]+')')
        print('('+Array[location - 1][4]+')')
    elif modSuccess >= 5:
        print("major find: ",majorFind[index])
        print('('+Array[location - 1][3]+')')
        print('('+Array[location - 1][4]+')')
    elif modSuccess >= 0:
        print("minor find: ",minorFind[index])
        print('('+Array[location - 1][3]+')')
        print('('+Array[location - 1][4]+')')
    else:
        print("Failed Check due to mods")
        print('Total Number of Successes: ', modSuccess)
    print('######################################################################################')
    runagain=input('Do you want to run again? [y/n]: ')
    if runagain == 'n':
        running = False