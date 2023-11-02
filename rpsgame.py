import sys
import random

print(str.title("\nWelcome to the RockPaperScissors Game!\n\n"))

playagain = True

while playagain:
    userchoice = input("Please input Rock, Paper or, Scissors: \n")

    if userchoice != 'Rock' and userchoice != 'Paper' and userchoice !='Scissors':
        sys.exit("Error: Please enter one of the available choices\n")
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
    
    playagain = input("Input stop to exit the game or press any key to keep playing\n")
    if playagain == 'stop':
        playagain = False