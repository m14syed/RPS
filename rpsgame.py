import sys
import random

print(title("Welcome to the RockPaperScissors Game!"))


userchoice = input("Please input Rock, Paper or, Scissors: \n")

if userchoice != 'Rock' and userchoice != 'Paper' and userchoice !='Scissors':
    sys.exit("Error: Please enter one of the available choices\n")
print("\nYou have selected " + userchoice + ".")

choices = ['Rock', 'Paper','Scissors']
cpuchoice = random.choice(choices)
print("Computer has chosen " + cpuchoice + ".")

if cpuchoice == 'Paper' and userchoice == 'Rock':
    print('\nYou have lost... 🥲')
elif cpuchoice == 'Rock' and userchoice == 'Scissors':
    print('\nYou have lost... 🥲')
elif cpuchoice == 'Scissors' and userchoice == 'Paper':
    print('\nYou have lost... 🥲')
elif cpuchoice == userchoice:
    print('\nYou have tied 😒')
else:
    print("\nYou have won! 😊")