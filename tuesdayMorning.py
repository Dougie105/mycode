#!usr/bin/env python3

import sys
import json
import requests
import webbrowser
  
def main():
    nh1 = requests.get("http://statsapi.web.nhl.com/api/v1/teams")

    if nh1.status_code == 200:
        game = nh1.json()
    else:
        print(f'invalid request - response code {nh1.status_code}')
        sys.exit() #only ditch if the status response is not 200

    #input nhl tteam 3 letter abbreviation
    abrv = input('NHL Team Abbreviation...')

    for team in game['teams']:
        if abrv == team['abbreviation']:
            print('You have a match')
            webbrowser.open(team['officialSiteUrl'])



if __name__ == '__main__':
        main()
