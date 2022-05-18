#here's what ms. suarez wrote lol:

#user='paper'
#computer = 1
#if 'paper' in user:
#    user=int(1)
#    print("paper"+str(user))
#elif 'r' in user:
#    user=int(2)
#elif 's' in user:
#    user=int(3)



#make a menu
import os, random
import time
os.system('cls')
def menu():
    print(' __________________________________________________________________________________________ ')
    print('|                                                                                          |')
    print('|            █▀█ █▀█ █▀▀ █▄▀   █▀█ ▄▀█ █▀█ █▀▀ █▀█   █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀             |')
    print('|            █▀▄ █▄█ █▄▄ █ █   █▀▀ █▀█ █▀▀ ██▄ █▀▄   ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█             |')
    print('|                                                                                          |')
    print('|                                 #####################                                    |')
    print("|            _.-._                |    ACTION KEY:    |                  .-.               |")
    print('|          _| | | |               #####################                  | |    / )        |')
    print('|         | | | | |                                                      | |   / /         |')
    print('|         | | | | |      1- paper        2- rock       3- scissors       | |  / /          |')
    print("|         | i ' i | ,-,                _.-.-.-.                       _.-| |_/ /           |")
    print('|         |       |/ /                ; | |_|_|_                     ; \( \   /            |')
    print("|         |     ,-' /                 |_|_|\__  |                    |\_)\ \  |            |")
    print("|         |    ;    |                 |    . '  |                    |    ) \ |            |")
    print('|         |        /                  |   (    /                     |   (    /            |')
    print('|          \______/                    \______/                       \______/             |')
    print('|                                                                                          |')
    print('|     █▀█ ▄▀█ █▀█ █▀▀ █▀█           █▀█ █▀█ █▀▀ █▄▀          █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀     |')
    print('|     █▀▀ █▀█ █▀▀ ██▄ █▀▄           █▀▄ █▄█ █▄▄ █ █          ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█     |')
    print('|                                                                                          |')
    print('|__________________________________________________________________________________________|')

menu()

#define variables
paper=1
rock=2
scissors=3

guess=0
level=0
gameType=""

#checking for correct user input
check=True
while check:
    gameType=input("\n                               What's your move?\n                                   SELECT: ")
    try:
        gameType=int(gameType)
        if gameType >0 and gameType <4:
            check=False
        else:
            print("                 XX ERROR XX - Please use a number between 1 and 3.")
    except ValueError:
        print("         XX ERROR XX - That's not a number... Please use a number between 1 and 3.")

# selections
if gameType==1:
    print("                              You selected: PAPER!")
    time.sleep(1)
    print("\n                             Ready to show your hand?"),time.sleep(1)
    print("\n                                     Rock...",end=''),time.sleep(0.5)
    print("\n                                     paper...",end=''),time.sleep(0.5)
    print("\n                                   scissors..."),time.sleep(0.5)
    print("")
    print("                              █▀ █ █ █▀█ █▀█ ▀█▀ █")
    print("                              ▄█ █▀█ █▄█ █▄█  █  ▄")


if gameType==2:
    print("You selected: ROCK!")

if gameType==3:
    print("You selected: SCISSORS!")
    print("\nRock, paper, scissors... SHOOT!")
    print("\n")





#EX: while paper... blah blah 

#establish that one will beat the other (rock > scissors, scissors > paper, paper > rock)

#randomize the opponent's plays (rock, paper, or scissors)

#loop game for if the player wins

#loop game for if the player loses