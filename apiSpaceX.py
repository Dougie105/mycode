#!/usr/bin/python3
"""
Author: RZFeeser
This program harvests SpaceX data avail from https://api.spacexdata.com/v3/cores using the Python Standard Library methods
"""

# using std library method for getting at API data
import urllib.request 
import json

# GOBAL / CONSTANT of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    coreData = urllib.request.urlopen(SPACEXURI)

    # pull STRING data off of the 200 response (even tho it's JSON!)
    xString = coreData.read().decode()
    print(type(xString))

    # convert STRING data into Python Lists and Dictionaries
    listOfCores = json.loads(xString)
    print(type(listOfCores))

    for core in listOfCores:
        print(f"SERIAL: {core['core_serial']} , LAUNCH DATE: {core['original_launch']}, MISSIONS: {core['missions']}", end="\n")
        
        if (len(core['missions']) > 3):
            print('Over Achiver', end='\n\n')

#        if (len(core['missions']) == 3):
#            print(f"Mission Total for SERIAL: {core['core_serial']} is {len(core['missions'])}", end="\n\n")
        elif (len(core['missions']) < 3):
            print('Step it up slacker...', end="\n\n")

        elif (len(core['missions']) == 0):
            print('Why are you even here...', end="\n\n")

if __name__ == "__main__":
    main()
