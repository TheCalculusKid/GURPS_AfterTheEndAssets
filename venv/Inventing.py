import random

## User-input authenticators##########################################
##
def inputyn(string):  ##
    invalidInput = True  ##
    while invalidInput:  ##
        try:  ##
            userinput = str(input(string))  ##
            if userinput == 'y' or userinput == 'n':  ##
                invalidInput = False  ##
            else:  ##
                print("Invalid input: Not in the form of y or n!")  ##
        except:  ##
            print("Invalid input: Not a string")  ##
    return userinput  ##

######################################################################
def inputint(string):  ##
    invalidInput = True  ##
    while invalidInput:  ##
        try:  ##
            userinput = int(input(string))  ##
            invalidInput = False  ##
        except:  ##
            print("Invalid input: Not a integer")  ##
    return userinput  ##

######################################################################
def inputstr(string):  ##
    invalidInput = True  ##
    while invalidInput:  ##
        try:  ##
            userinput = str(input(string))  ##
            invalidInput = False  ##
        except:  ##
            print("Invalid input: Not a string")  ##
    return userinput  ##


######################################################################
def dice(numberOfRolls):
    diceSum = 0
    for i in range(numberOfRolls):
        die = random.randint(1, 6)
        diceSum = diceSum + die
    return diceSum


inventor = {
    "$10": [-2, -7, (dice(2) + 2), ' hrs.'],
    "$100": [-4, -9, (dice(1) * 10), ' hrs.'],
    "$1,000": [-6, -11, (dice(1)), ' days.'],
    "$10,000": [-8, -13, (dice(2)), ' days.'],
    "$100,000": [-10, -15, (dice(2) * 4), ' days.'],
    "$1,000,000": [-12, -17, (dice(4)), ' weeks.'],
    "$2,000,000": [-14, -19, (dice(6)), ' weeks.'],
    "$3,000,000": [-16, -21, (dice(4) * 2), ' weeks.'],
}
gadgeteer = {
    "$10": [2, -2, (dice(2) * 5), ' min.'],
    "$100": [1, -3, (dice(4) * 10), ' min.'],
    "$1,000": [-1, -5, (dice(2)), ' hrs.'],
    "$10,000": [-2, -6, (dice(4)), ' hrs.'],
    "$100,000": [-4, -8, (dice(2) * dice(5)), ' hrs.'],
    "$1,000,000": [-5, -9, (dice(1)), ' days.'],
    "$2,000,000": [-7, -11, (dice(2) - 1), ' days.'],
    "$3,000,000": [-8, -12, (dice(3) - 2), ' days.'],
}
print('''
########################################################################################################################
####################################WELCOME TO THE GURPS INVENTION CALCULATOR v3000#####################################
########################################################################################################################

This program will allow you to calculate the cost, time and the modifier to your invention roll required to create or
modify equipment. Please follow input prompts and if you have any questions please consult readme for insights into the 
code or your GM with questions about the GURPS rules.

To "invent" and item the character must have the appropriate "design" skill such as the appropriate Engineering skill,
Bioengineering (for biotech), Computer Programming (For computer programs) or Pharmacy (for drugs)

For modifications, repairs, or if the character has a blueprint "repair" skills like: Armoury, Electrician, Electronics
Repair, Machinist, and Mechanic can be used to make the item.

For extremely simple modifications i.e. bolting on a scope to a rifle that has the right rail system, 'use" skills like:
Explosives, Computer Operation, Guns(Rifles), etc.. can be used.


Enjoy (;

''')
gadgeteerSelector = inputyn("Is the character a gadgeteer? [y/n]: ")
if gadgeteerSelector == 'y':
    dictable = gadgeteer
    gadgeteerIndex = 0
if gadgeteerSelector == 'n':
    dictable = inventor
    gadgeteerIndex = 1
nameOfInventionSelector = inputstr("Input name of Invention or Modification: ")
costOfInventionSelector = inputint("Input cost of invention or modification in an integer number: ")
tracker = []
tracker.append(nameOfInventionSelector)  # Index: 0
tracker.append(costOfInventionSelector)  # Index: 1
#print(tracker)
if costOfInventionSelector >= 10:
    table = dictable["$10"]
elif 10 < costOfInventionSelector < 100:
    table = dictable["$100"]
elif 100 < costOfInventionSelector < 1000:
    table = dictable["$1,000"]
elif 100 < costOfInventionSelector < 10000:
    table = dictable["$10,000"]
elif 10000 < costOfInventionSelector < 100000:
    table = dictable["$100,000"]
elif 100000 < costOfInventionSelector < 1000000:
    table = dictable["$1,000,000"]
elif 1000000 < costOfInventionSelector < 2000000:
    table = dictable["$2,000,0000"]
elif 2000000 < costOfInventionSelector < 3000000:
    table = dictable["$3,000,000"]

print('''
i   Workspace
0:  None (wilderness, etc.)                                                             0
1:  Improvised:                                                                         1
2:  Professional but wrong (e.g., an auto shop when making a beam weapon):              2
3:  Professional and right:                                                             3
4:  Above, plus high-quality and in perfect shape:                                      4
5:  Above, but cutting-edge, amazing gear:                                              5
''')
workspace = inputint("Enter 0,1,2,3,4, or 5 for Workspace selection: ")
workspaceTable = [
    [-5, -5],
    [0, 0],
    [2, 0],
    [5, 2],
    [6, 3],
    [7, 4]
]
techlevel = inputint("Enter invention or modification TL(TL* = 4): ")
if techlevel <= 4:
    techModifier = 4
if techlevel == 5:
    techModifier = 3
if techlevel == 6:
    techModifier = 2
if techlevel == 7:
    techModifier = 1
if techlevel == 8:
    techModifier = 0
if techlevel == 9:
    techModifier = -3
if techlevel == 10:
    techModifier = -6
tracker.append(techModifier) # Index: 2 (Modifiers)
tracker.append((table[2]))   # Index: 3 (#'ed Time)
tracker.append((table[3]))   # Index: 3 (Time Units)
modification = inputyn('Is your creation a modification of an existing item? [y/n]: ')
if modification == 'y':
    index = 0
    name = "modification"
if modification == 'n':
    index = 1
    name = "invention"

tracker[2] = tracker[2] + techModifier + workspaceTable[workspace][gadgeteerIndex]
#modifier = techModifier + table[index] + workspaceTable[workspace][gadgeteerIndex]
itemAdder = True
i = 1
dictionary = {}
print('''
########################################################################################################################
###########################################Invention Component Adding System############################################
########################################################################################################################

''')
print("The base modifier for the " + name + ' is: ',tracker[2])
print("For each 10% of the total cost to make the item you are missing you incur a -1")
print('''

Components used to make modification or invention will be added to a dictionary to track the total cost of each 
component. Inventing can be without having enough components but with a -1 penalty per 10% of missing items. Components 
total cost will be summed and returned as a percentage of items required to make the invention.

Certain skills can be used to fabricate/create components for an invention, although doing so takes extra time
Machinist (for mechanical components), Electrician (for electronic components), Chemistry (For synthesizing ingredients),
and Naturalist (to gather natural ingredients)

Using one of these skills to fabricate components doubles your total project time, while using two triples time.

i   Number of fabrication skills used:
0:  No fabrication skills used
1:  One fabrication skill used
2:  Two fabrication skills used
''')

fabricate = inputint("Enter 0,1,2, or 3 for number of fabrication skills used: ")
fabricateWorkspace = [-10, -5, 0]
if fabricate > 0:
    skill1 = inputstr("Input name of fabrication skill used: ")
    tracker[3] = tracker[3]*2
    print('''
i   Workspace(Fabrication Skill)
0:  No Appropriate Equipment
1:  Improvised Equipment
2:  Appropriate Equipment
''')
    fabricateWorkspaceSelect = inputint("Enter 0,1, or 2 for fabrication workspace used: ")
    if tracker[2] < 0:
        fabricatedMod = fabricateWorkspace[fabricateWorkspaceSelect] + tracker[2]
    else:
        fabricatedMod = fabricateWorkspace[fabricateWorkspaceSelect]
    print("Your Total Modifier for your fabrication attempt is: ", fabricatedMod)
    fabricatedSuccesses = inputint("Input number of successes (without equipment modifiers): ")
    if fabricatedSuccesses + fabricatedMod >= 0:
        dictionary[skill1] = ( 1+ fabricatedSuccesses + fabricatedMod) * 0.05 * tracker[1]
    if fabricate == 2:
        fabricateWorkspaceSelect = inputint("Enter 0,1, or 2 for fabrication workspace used: ")
        if tracker[2] < 0:
            fabricatedMod = fabricateWorkspace[fabricateWorkspaceSelect] + tracker[2]
        else:
            fabricatedMod = fabricateWorkspace[fabricateWorkspaceSelect]
        skill2 = inputstr("Input name of second fabrication skill used: ")
        tracker[3] = (tracker[3] / 2) * 3
        fabricatedSuccesses = inputint("Input number of successes (without equipment modifiers): ")
        if fabricatedSuccesses + fabricatedMod >= 0:
            dictionary[skill1] = (1 + fabricatedSuccesses + fabricatedMod) * 0.05 * tracker[1]
    print("Components fabricated so far: ", dictionary)
    itemSum = sum(dictionary.values())
    percentage = itemSum / costOfInventionSelector
    print("So far you have: ", percentage * 100, "% of the total cost of the item")
while itemAdder:
    print("Item ", i, ":")
    item = inputstr("Enter components name: ")
    cost = inputint("enter components cost: ")
    print('''
i   Relatedness  
0:  Unrelated
1:  Barely Related
2:  Related(Junk)
3:  Very Closely Related
4:  Same Thing
    ''')
    relatedness = [0.1, 0.5, 1.0, 2.0, 4.0]
    relatedIndex = inputint("Enter 0,1,2,3, or 4 for relatedness of component: ")
    dictionary[item] = cost * relatedness[relatedIndex]
    itemSum = sum(dictionary.values())
    percentage = itemSum / costOfInventionSelector
    print("So far you have: ", percentage * 100, "% of the total cost of the item")
    itemPenalty = int(percentage * 10) - 10
    print("your total penalty with the components currently being used is ", tracker[2] + itemPenalty)
    goAgain = inputyn("do you want to add another component [y/n]: ")
    if goAgain == 'y':
        i = i + 1
    if goAgain == 'n':
        itemAdder = False
        break
print('Components used to make invention: ', dictionary)
tracker[2] = tracker[2] + itemPenalty
print('Total modifier to make your ', name, ' is ', tracker[2])
timedelta1 = inputyn("Do you want to take more time to make the " + name + " to increase your modifier? [y/n]:")
if timedelta1 == 'y':
    print('''
########################################################################################################################
Extra Time
index   time    modifier
0:      x2      +1
1:      x4      +2
2:      x8      +3
3:      x15     +4
        ''')
    extraTime = [
        [2, 1],
        [4, 2],
        [8, 3],
        [15, 4]
    ]
    timeIndex = inputint("Enter index from above list: ")
    tracker[2] = tracker[2] + extraTime[timeIndex][1]
    print('Total modifier to make your ', name, ' is ', tracker[2])
    print('Total time required to make ', name, ' is ', tracker[3] * extraTime[timeIndex][0], " ", tracker[4])

timedelta2 = inputyn("Do you want to rush the " + nameOfInventionSelector + "(-1 modifier per 10% decrease in time)? [y/n]:")
if timedelta2 == 'y':
    print('########################################################################################################################')
    rushpercentage = float(
        input('decimal percentage reduction in time for project(i.e. 0.1 for 10% reduction in project): '))
    tracker[2] = tracker[2] - rushpercentage * 10
    print('Total modifier to make your ', name, ' is ', tracker[2])
    print('Total time required to make ', name, ' is ', tracker[3] * (1 - rushpercentage), " ", tracker[4])
else:
    print('########################################################################################################################')
    print('Total modifier to make your ', name, ' is ', tracker[2])
    print('Total time required to make ', name, ' is ', tracker[3], " ", tracker[4])

print('''
########################################################################################################################
################################################### Invention Roll #####################################################
########################################################################################################################

Once the modifier is decided and is deemed a project wirth pursuing the inventor must work for the requisite amount of
time then roll against their invention skill. Bugs may be present with inventions based on margin of success of the
invention roll. Multiple copies of one shot items can also be made based on margin of success.

''')
bugs = ["1d+2","1d"]
modifiersExtra = inputint("Input any other modifiers for advantages or based on GM's discretion: ")
inventionRoll = inputint("Input number of successes on invention roll without any modifiers: ")
tracker[2] = tracker[2] + modifiersExtra
if inventionRoll + tracker[2] >= 0:
    print("Invention Success! The invention succeeded with: ", inventionRoll+tracker[2], " successes")
    if techlevel <= 8:
        print("The number of bugs is", bugs[gadgeteerIndex], "-", (inventionRoll+tracker[2]) * 2)
    else:
        print("The number of bugs is", bugs[gadgeteerIndex], "-", (inventionRoll+tracker[2]) * 2, "+", abs((8-techlevel)))