import sys
import random

def RPSgame():
    print(str.title("\nWelcome to the RockPaperScissors Game!\n======================================\n"))
    
    userchoice = input("Please input Rock, Paper or, Scissors: \n")

    if userchoice != 'Rock' and userchoice != 'Paper' and userchoice !='Scissors':
        print("Error: Please enter one of the available choices\n")
        return RPSgame()
    
    print("\nYou have selected " + userchoice + ".")

    choices = ['Rock', 'Paper','Scissors']
    cpuchoice = random.choice(choices)
    print("Computer has chosen " + cpuchoice + ".")

    if cpuchoice == 'Paper' and userchoice == 'Rock':
        print('\nYou have lost... 🥲\n')
    elif cpuchoice == 'Rock' and userchoice == 'Scissors':
        print('\nYou have lost... 🥲\n')
    elif cpuchoice == 'Scissors' and userchoice == 'Paper':
        print('\nYou have lost... 🥲\n')
    elif cpuchoice == userchoice:
        print('\nYou have tied 😒\n')
    else:
        print("\nYou have won! 😊\n")

    playagain = input("Input E to exit the game or C keep playing\n").upper()
    if playagain == 'E':
        sys.exit("Thank you for Playing, Bye! 👋")
    else:
        return RPSgame()
    
RPSgame()
