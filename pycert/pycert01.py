#!/usr/bin/env python3

""" Python Project Grade """

# The Idea is to take a user's input of favorite console and see what characters they can meet.
import crayons #To distingush the user interactions

ninten = ["Mario","Link","Pikachu", "Peach","Marth","Fox"]

xbox = ["John", "Jack", "Price","Liz"]

playsta = ["Kratos","Snake","Drake","Evan"]

choice = " "

def main():
    #This is code will take user perfernce of the three and provide from the list above
    print("Hello and Welcome to a store of top three consoles!")
    round = 0 # This is a counter of # of times the user put's in

    while True and (choice != 'Nintendo' and choice != 'Xbox' and choice != 'Playstation'):
        round = round + 1 #For everytime the user enters a nonvalid choice, it will increase
        answer = input('Which is your favoite Console? Your answer: ')
        answer = answer.capitalize() # this line will make user input first letter start with an uppercase

        if answer == "Nintendo":
            print(crayons.cyan('Nice choice. Here are the characters that are available below:  '))
            for x in ninten:
                print(x)
            ans = input('Which character you want to meet? Your answer: ')
            ans = ans.capitalize()
            if ans in ninten: #This will check the list to see if the user input a game from the list
                print(crayons.magenta(ans), '- have fun meeting them!')
                break
            else:
                print('Character  not a choice, try again')
                round = round +1
        elif answer == "Xbox":
            print(crayons.cyan('Nice choice. Here are the characters that are available below:  '))
            for x in xbox:
                print(x)
            ans = input('Which character  do you want to meet? Your answer: ')
            ans = ans.capitalize()
            if ans in xbox:#This will check the list to see if the user input a game from the list
                print(crayons.green(ans), '- have fun meeting them!')
                break
            else:
                print('character not a choice, try again')
                round = round +1
        elif answer == "Playstation":
            print(crayons.cyan('Nice choice. Here are the games that are available below:  '))
            for x in playsta:
                print(x)
            ans = input('Which character do you want to meet? Your answer: ')
            ans = ans.capitalize()
            if ans in playsta:#This will check the list to see if the user input a game from the list
                print(crayons.blue(ans), '- have meeting them!')
                break
            else:
                print(crayons.yellow('character  not a choice, try again')) # User will get a max of 5 chances to input
                round = round +1
        elif round == 5:
            print(crayons.red('Out of times you can answer. Come again later!')) # If the count reachs 5, user will get this answer
            break
        else:
            print(crayons.yellow('Not a valid answer. Try again!')) # The user will get another chance


if __name__ == "__main__":
    main()
