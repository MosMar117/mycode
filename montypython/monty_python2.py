#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game using a while True loop."""

round = 0

while True:
    round = round + 1
    print('Finish the moive title, "Monty Python\'s The life of ____"')
    answer = input("Your guess--> ")
    if answer == 'Brian':
        print('Correct')
        break
    elif round== 3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try Again!")
