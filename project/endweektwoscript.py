#!/usr/bin/python3

import json
import pyfiglet
from termcolor import colored, cprint

# Lambda function to change the color of the text
print_grey_on_white = lambda x: cprint(x, 'blue')
titleAndEnding = lambda  x: colored(pyfiglet.figlet_format(x, font="standard"), 'red', attrs=['bold'])

print(titleAndEnding('ESCAPE'))


def objective():
    print_grey_on_white(
        "The objective of this game is to stop the Murder Hornets from another dimension.\nBut be careful...\nThe hornets know your plan and are trying to stop you!\nStop the colony from finding their way into this universe and don't get murdered.\n...\nTo get a list of commands type 'help' to see the controls.")


def showInstructions():
    """Prints list of commands that can be used"""
    print('''
    RPG Game
    ========
    Commands:
      help (will display controls)
      stats (to get your room and inventory)
      go north, south, east, west, back
      inventory
      browse (look around room)
      inspect [item]
      get [item]
      view [item]
      * if you have a code to enter, go to a room and enter just the code to activate its effect.
    ''')


def showStatus():
    """print the player's current location"""
    cprint('You are in the ' + currentroom, 'green')
    if "item" in rooms[currentroom]:
        cprint('You see a ' + rooms[currentroom]['item'], 'magenta', attrs=['blink'])
    print("---------------------------")


def showDepth():
    if "item" in rooms[currentroom]:
        print('You see a ' + rooms[currentroom][inspect]['picture']['item'])
    print("---------------------------")

def gameOver():
    print(titleAndEnding('GAME OVER'))

def gameWin():
    print(titleAndEnding('CONGRATS!'))

# Start with an empty inventory.
inventory = []

# Open the json file that contains the worldMap
with open("rooms.json", "r") as worldMap:
    rooms = json.load(worldMap)

# start the player in the Hall
currentroom = 'Hall'
inspect = 'inspect'
item = 'item'
crowbar = rooms[currentroom][inspect]['picture']['item']

objective()
showStatus()

############################################################################################################
############################################################################################################
############################################ Start Gameplay ################################################
############################################################################################################
############################################################################################################

while True:

    ############################################################################################################
    ############################################################################################################
    ########################################### Type Tracking ##################################################
    ############################################################################################################
    ############################################################################################################

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)



    ############################################################################################################
    ############################################################################################################
    ########################################### Browse the Room ################################################
    ############################################################################################################
    # TODO: want to inspect rug and find a loose tile. Then use loose tile with crowbar and find a blacklight ##

    if move[0] == 'browse':
        # for items in 'inspect', print to screen
        print('You see a ', end='')
        for items in rooms[currentroom][inspect]:
            # should print chair, rug, and picture
            print(items, end=', ')


    ############################################################################################################
    ############################################################################################################
    ################################################ Inspection ################################################
    ############################################################################################################
    # TODO: inspecting rug #####################################################################################

    if move[0] == 'inspect':
        if len(move) < 2:
            print('No value entered...')
            continue
        elif len(move) == 2:
            if move[1] in rooms[currentroom][inspect]:
                if rooms[currentroom][inspect][move[1]] == 'nothing':
                    print(f'Nothing behind that')
                elif 'item' in rooms[currentroom][inspect][move[1]]:
                    print(f'You found a {rooms[currentroom][inspect][move[1]][item]}')
                elif 'item' in rooms[currentroom][inspect][move[1]]['loose tile']:
                    print(f'You found a {rooms[currentroom][inspect][move[1]]["loose tile"][item]}')
            else:
                print('Nothing to see here.')

    ############################################################################################################
    ############################################################################################################
    ########################################### Player Movement ################################################
    ############################################################################################################
    ############################################################################################################

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentroom]:
            # set the current room to the new room
            currentroom = rooms[currentroom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')


    ############################################################################################################
    ############################################################################################################
    ######################################### Getting Items ####################################################
    ############################################################################################################
    ############################################################################################################

    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if move[1] == crowbar and item in rooms[currentroom][inspect]['picture']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentroom][inspect]['picture'][item]
        elif move[1] in rooms[currentroom]['item'] and "item" in rooms[currentroom]:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentroom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ############################################################################################################
    ############################################################################################################
    ####################################### Inventory and Help #################################################
    ############################################################################################################
    ############################################################################################################

    if move[0] == 'inventory':
        # print the current inventory
        print('Inventory : ' + str(inventory))

    if move[0] == 'help':
        showInstructions()

    ############################################################################################################
    ############################################################################################################
    ################################### Reading ################################################################
    ############################################################################################################
    ############################################################################################################

    # if they type view first
    if move[0] == 'read' and move[1] == 'paper' and 'paper' in inventory:
        print('7ThreefIv3s3v3n')
    elif move[0] == 'read' and move[1] != 'paper':
        print('Nothing to see here...')


    ############################################################################################################
    ############################################################################################################
    ################################## Open Vault ##############################################################
    ############################################################################################################
    ############################################################################################################

    if move[0] == '7357' and currentroom == 'Vault':
        currentroom = 'OpenVault'

    ############################################################################################################
    ############################################################################################################
    ########################################## Various Wasps ###################################################
    ############################################################################################################
    ############################################################################################################

    if currentroom == 'murderHornetNest' and 'super_raid' in inventory:
        print('The hornet curled up and died. You dont have to burn down your home after all!')
        break

    ############################################################################################################
    ############################################################################################################
    ################################# Good Ending ##############################################################
    ############################################################################################################
    ############################################################################################################

    # TODO: cannot delete items from inventory yet

    if currentroom == 'Kitchen' and 'raid' in inventory:
        print('The hornet curled up and died. You need to stop the others!')
        # del inventory['raid']
        # del rooms[currentroom['item']]


    ############################################################################################################
    ############################################################################################################
    ################################# Game Over ################################################################
    ############################################################################################################
    ############################################################################################################

    if 'item' in rooms[currentroom] and 'hornet' in rooms[currentroom]['item']:
        """If a player enters a room with the hornet"""
        gameOver()
        print('A hornet has got you...')
        break

    if 'item' in rooms[currentroom] and 'A large colony of Murder Hornets' in rooms[currentroom]['item']:
        """If a player enters a room with the hornet"""
        gameOver()
        print('You didnt stand a chance against all of them... GAME OVER!')
        break

    if currentroom == 'murderHornetNest' and 'super_raid' in inventory:
        """If the player destroys the nest without getting killed"""
        gameWin()
        print('They wont be hurting anyone anymore. You dont have to burn down your home after all!')
        break

