#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  help (will display controls)
  stats (to get your room and inventory)
  go [direction]
  go back if necessary
  get [item]
  view [item]
''')


def showStatus():


# # print the player's current status
# print('---------------------------')
# print('You are in the ' + currentRoom)
#
# # print the current inventory
# print('Inventory : ' + str(inventory))
# # print an item if there is one
# if "item" in rooms[currentRoom]:
#     print('You see a ' + rooms[currentRoom]['item'])
# print("---------------------------")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Vault',
        'item': 'key'
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': "paper",
    },

    'Kitchen': {
        'north': 'Hall',
        'east': 'Garden',
        'item': 'hornet',
    },
    'Garden': {
        'west': 'Kitchen',
        'north': 'Dining Room',
        'south': 'Portal'
    },
    'Portal': {
        'north': 'Hall',
        'south': 'Hall',
        'west': 'Dining Room',
        'east': 'Kitchen',
        'item': 'raid'
    },
    'Vault': {
        'back': 'Hall',
    },
    'OpenVault': {
        'item': 'superRaid',
        'back': 'Vault'
    }
}

murderHornetDemention = {

    'murderHornetNest': {
        'item': 'A large colony of Murder Hornets',
    }

}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    showStatus()

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

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
            inventory.pop('superRaid')

    if move[0] == 'stats':
        # print the player's current status
        print('---------------------------')
        print('You are in the ' + currentRoom)

        # print the current inventory
        print('Inventory : ' + str(inventory))
        # print an item if there is one
        if "item" in rooms[currentRoom]:
            print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")

    if move[0] == 'help':
        print('''
        RPG Game
        ========
        Commands:
          help (displays game controls)
          stats (to get your room and inventory)
          go [direction]
          go back if necessary
          get [item]
          read [item]
        ''')

    # if they type view first
    if move[0] == 'read':
        if "paper" in inventory:
            print('7ThreefIv3s3v3n')
        else:
            print('Nothing to see here...')

    if move[0] == '7357' and currentRoom == 'Vault':

    if currentRoom == 'Portal':
        print('You see the faint numbers 7357 in the portal lights')

    if currentRoom == 'Kitchen' and 'raid' in inventory:
        print('The hornet curled up and died. You dont have to burn down your home after all!')
        break

        ## If a player enters a room with the hornet
    if 'item' in rooms[currentRoom] and 'hornet' in rooms[currentRoom]['item']:
        print('A hornet has got you... GAME OVER!')
        break

    ## If a player enters a room with the hornet
    if 'item' in rooms[currentRoom] and 'A large colony of Murder Hornets' in rooms[currentRoom]['item']:
        print('You didnt stand a chance against all of them... GAME OVER!')
        break

        ## Define how a player can win
    if currentRoom == 'Kitchen' and 'raid' in inventory:
        print('The hornet curled up and died. You need to stop the others!')
        del inventory['raid']
        del rooms[currentRoom['item']]

    if currentRoom == 'murderHornetNest' and 'superRaid' in inventory:
        del inventory['superRaid']
        del rooms[currentRoom['item']]
        print('The hornet curled up and died. You dont have to burn down your home after all!')
