#!/usr/bin/env python3
"""
Jeopardy Game
"""

import requests

def main():
    # prompt user for initials
    player = input('Type in your initials...')
    rounds = input('How many rounds would you like to play?')
    playerscore = 0

    # make a request to jservice.io/random
    resp = requests.get(f'http://jservice.io/api/random?count={rounds}')

    # according to docs, ?count=10 appended to the URI will return 10 results
    listofquestions = resp.json()

    #Run for 10 rounds by looping over the results

    # each time through the loop pose the question to the player
    for jquestion in listofquestions:
        print(f"Alex says: {jquestion['question']}")

        playeranswer = input(f"\tType your Answer --> ({jquestion['answer']}")

        # user can response by typing the input be sure to normalize to lowercase
        if playeranswer.lower() == jquestion['answer'].lower():
            print('Alex Says: Thats Correct!')
            playerscore = playerscore + jquestion['value']

        else:
            print('Alex Says: That is Incorrect.')
            playerscore = playerscore - jquestion['value']
    print('Alex Says: Okay lets see how you did!\n Player Score: {playerscore}')

    #Keep track of highscores
    with open('jeopardyhighscores.txt') as jhs:
        highscorelist = jhs.readlines()
        highscorelist.sort()

        for score in highscorelist:
            print('Looks like a new High Score!')
            if playerscore > int(score):
                highscorelist.pop(score)
                highscorelist.append(playerscore)
                break

if __name__ == "__main__":
    main()
