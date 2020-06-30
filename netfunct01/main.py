#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# function to push commands
def commandpush(devicecmd): # devicecmd==list

    for coffeetime in devicecmd.keys():
        print(f'Handshaking. .. ... connecting with {coffeetime}\n')
        # we'll learn to write code that connects to devices here

        for mycmds in devicecmd[coffeetime]:
            print(f'Attempting to sending command --> {mycmds}\n')
            # we'll learn to write code that sends cmds to device here

# function to reboot via IPs
def devicerboot(ipAddresses):
    for ip in ipAddresses.keys():
        print(f"Connecting to.. {ip}. REBOOTING NOW!\n")


def main():

    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1": 
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print("Welcome to the network device command pusher\n") # welcome message

    ## get data set
    print("Data set found\n") # replace with function call that reads in data from file
    
    ## run
    commandpush(work2do) # call function to push commands to devices
    devicerboot(work2do) # passing in work2do as arg

# call our main function
main()

