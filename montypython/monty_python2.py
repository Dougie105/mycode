#!/usr/bin/env python3

#Initialize a counter for the number of guesses
counter = 0

while True:
    counter = counter + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    if answer == 'Brian':
        print('Correct')
        break
    elif counter==3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")

