import sys
import random
from termcolor import colored

def choosenumber():
    title = str.title("\nWelcome to the Choose Numbers Game!\n===================================\n")
    print(colored(title,'green', attrs=['bold']))

    gamecount = 0
    userwins = 0
    winpcnt = 0

    def CNgame():
        nonlocal winpcnt, userwins, gamecount
        userchoice = input("Please input 1, 2 or 3: \n")

        if userchoice != '1' and userchoice != '2' and userchoice !='3':
            errormsg = str.capitalize("Error: Please enter 1, 2, or 3\n")
            print(colored(errormsg, 'red', attrs = ['bold']))
            return CNgame()
        
        choices = ['1', '2','3']
        cpuchoice = random.choice(choices)

        print(f"\nPython was thinking about {cpuchoice}.\nYou have selected {userchoice}.")
              
        if cpuchoice == userchoice:
            print('\nYou have won... 😊\n') 
            userwins += 1 
            gamecount += 1
            winpcnt = userwins/gamecount
            print (f"Game Count: {gamecount}\nYour Wins: {userwins}\nYour Win Rate: {winpcnt:2%}")
        else:
            print("\nYou have lost! 🥲\n")
            gamecount += 1
            winpcnt = userwins/gamecount
            print (f"Game Count: {gamecount}\nYour Wins: {userwins}\nYour Win Rate: {winpcnt:2%}")

        playagain = input("Input E to exit the game or C keep playing\n").upper()
        if playagain == 'C':
            return CNgame()
        else:
            if __name__ == "__main__":
                sys.exit("Thank you for Playing, Bye! 👋")
            else:
                return

    return CNgame()

if __name__ == "__main__":
    choosenumber()
