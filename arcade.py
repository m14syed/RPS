from rpsgame import RPS
from choose_number import choosenumber
import sys

def arcade():
    welcome_back = False

    while True:
        if welcome_back == True:
            wbmsg = str.title("Welcome back to the Arcade")
            print(wbmsg)

        userchoice = input("\nPlease Select the Game You Wish to Play:\n1 = Rock, Paper Scissors\n2 = Guess the Number\n\nOr Select E to exit\n")

        welcome_back == True

        if userchoice == '1':
            RPS()
        elif userchoice == '2':
            choosenumber()
        else:
            sys.exit ("See You Next Time! 👋")

if __name__ == "__main__":
    arcade()