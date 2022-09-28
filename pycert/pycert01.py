#!/usr/bin/env python3

""" Python Project Grade """

# The Idea is to take a user's input of favorite game and comparing it to what list has stored.
ninten = ["Super Mario 64","Banjo Kazzoie","Mario Kart", "Paper Mario","Godzilla","Pikmin"]

xbox = ["Halo", "Gears", "Call of Duty","Borderlands"]

playsta = ["God of War","Little Big Planet","Ni no Kuni","Ni no Kuni 2"]

choice = " "

def main():
    #This is code will take user perfernce of the three and provide from the list above
    print("Hello and Welcome to a store of top three consoles!")
    round = 0 # This is a counter of # of times the user put's in

    while True and (choice != 'Nintendo' and choice != 'Xbox' and choice != 'Playstation'):
        round = round + 1 #For everytime the user enters a nonvalid choice, it will increase
        answer = input('Which is your favoite Console? Your answer: ')

        if answer == "Nintendo":
            print('Nice choice. Here are the games that are available below:  ')
            for x in ninten:
                print(x)
            break
        elif answer == "Xbox":
            print('Nice choice. Here are the games that are available below:  ')
            for x in xbox:
                print(x)
            break
        elif answer == "Playstation":
            print('Nice choice. Here are the games that are available below:  ')
            for x in playsta:
                print(x)
            break
        elif round == 5:
            print('Out of times you can answer. Come again later!') # If the count reachs 5, user will get this answer
            break
        else:
            print('Not a valid answer. Try again!') # The user will get another chance


if __name__ == "__main__":
    main()
