from rpsgame import RPS
from choose_number import choosenumber
import sys
from termcolor import colored

def arcade(name = 'PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            wbmsg = str.title(f"\nWelcome back to the Arcade {name}")
            print(colored(wbmsg,'green', attrs=['bold']))
      
        userchoice = input("\nPlease Select the Game You Wish to Play:\n1 = Rock, Paper Scissors\n2 = Guess the Number\n\nOr Select E to exit\n")

        if userchoice not in ['1','2','E']:
            errormsg = str.capitalize("Error: Please enter a correct input\n")
            print(colored(errormsg, 'red', attrs = ['bold']))
            return arcade(name)

        welcome_back = True

        if userchoice == '1':
            RPS()
        elif userchoice == '2':
            choosenumber()
        else:
            sys.exit (f"See You Next Time {name}! 👋")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = 'Personalized Game Experience'
    )

    parser.add_argument(
        '-n', '--name', metavar= 'name', required=True, help= 'Input your name'
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")

    arcade(args.name)