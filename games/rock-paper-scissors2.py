# Ava Spence
# 1/28/22

import os, random
os.system('cls')

# Menu
def menu():
    print(' __________________________________________________________________________________________ ')
    print('|                                                                                          |')
    print('|            █▀█ █▀█ █▀▀ █▄▀   █▀█ ▄▀█ █▀█ █▀▀ █▀█   █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀             |')
    print('|            █▀▄ █▄█ █▄▄ █ █   █▀▀ █▀█ █▀▀ ██▄ █▀▄   ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█             |')
    print('|                                                                                          |')
    print('|__________________________________________________________________________________________|')
menu()

# Variables
gameType=""

# Checking for correct user input
check=True
while check:
    userhand=gameType=input("Choose your move: ")
    try:
        gameType=int(gameType)
        if gameType >0 and gameType <4:
            check=False
        else:
            print("Not an option, try again")
    except ValueError:
        print("Value error, try again")

if gameType==1:
    print("You chose: rock")
elif gameType==2:
    print("You chose: paper")
elif gameType==3:
    print("You chose: scissors")

#run = True
#while run:
randhand=random.randint(1,3)
if randhand==userhand:
    print(randhand)
    print("Tie")
elif randhand==1:
    if userhand==2:
        print(randhand)
        print("You win")
    else:
        print(randhand)
        print("You lose")
elif randhand==2:
    if userhand==1:
        print(randhand)
        print("You lose")
    else:
        print(randhand)
        print("You win")
elif randhand==3:
    if userhand==1:
        print(randhand)
        print("You win")
    else:
        print(randhand)
        print("You lose")





