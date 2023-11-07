from rpsgame import RPS
from choose_number import choosenumber
import sys

def arcade():
    userchoice = input("\nPlease Select the Game You Wish to Play:\n1 = Rock, Paper Scissors\n2 = Guess the Number\n\nOr Select 9 to exit\n")

    uint = int(userchoice)

    if uint == 1:
        RPS()
    elif uint == 2:
        choosenumber()
    else:
        sys.exit ("See You Next Time! 👋")
arcade()