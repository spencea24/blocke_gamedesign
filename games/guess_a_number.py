#Ava Spence
#1/27/22
#Guessing game

import os, random
os.system('cls')

# Define menu
def menu():
    print('#########################################          ////\\\\\\\   Welcome to my carnival booth!')
    print('|     !!    GUESS A NUMBER       !!     |          ///  \\\\\\      I have a jar full of mysterious numbers here...')            
    print('|                                       |         @/ ^  ^  @                  Follow the prompts to train your 3rd eye!')
    print('|   Test your psychic ability 4 free!   |          |  ~   |        _  ////')
    print('|      ~ g a m e  o p t i o n s ~       |           \ O  /         ||////')
    print('|                                       |)        ___|  |___       (   /')
    print('|      1 - Beginners luck (1-5)         | \      /   \__/   \      / /')   
    print('|      2 - Budding medium (1-15)        |\ \    /__        __\    / /')
    print('|      3 - SUPER psychic!!! (1-25)      | \ \  /  /|      |\  \  / /')
    print('|                                       |  \ \/  / |      | \  \/ /')
    print('#########################################   \   /  |      |  \   /')
menu()

#Declare all variables
guess=0
level=0
gameType=""

#Checking for correct user input
check=True
while check:
    gameType=input("\nPick a level:\n    Level: ")
    try:
        gameType=int(gameType)
        if gameType >0 and gameType <4:
            check=False
        else:  
            print("CARNIVAL MAN: Hey >:( That's not an option!!! Pick a level between 1 and 3, please!")
    except ValueError:
        print("CARNIVAL MAN: Um... I didn't understand that...")

# Level selection
def randomNum():
    global guess
    global level
    if gameType==1:
        guess=random.randint(1,5)
        level=5
    if gameType==2:
        guess=random.randint(1,15)
        level=15
    if gameType==3:
        guess=random.randint(1,25)
        level=25
randomNum()

# Game start!
print("\nThe Carnival Man takes a slip of paper from out of the jar. You can't get a very good look, but think you can make out a number... It looks like " + str(guess))
GameOn=True
counter=0
while GameOn:
    print("CARNIVAL MAN: Any guesses?")
    userGuess=int(input("What is your intuition telling you?\n    Guess: "))
    if guess==userGuess:
        print("\nCARNIVAL MAN: WOW!!!! You got it!!!!!! Great job :) You're a natural psychic!!!")
        #add an option to say "do you want to play again?" ---> if the user says no, then close the system... if the user says yes, then carry on as normal
        GameOn=False
    else:
        print("CARNIVAL MAN: Aw, sorry, you guessed wrong... :( Try again!\n")
print("The Carnival Man shows you the paper. It says: " + str(guess))

# Play again
print("\nCARNIVAL MAN: So, do you want to play again?")
print(' ___________________')
print('|                   |')
print('|    PLAY AGAIN?    |')
print('|                   |')
print('|    1 = yes!!!     |')
print('|    2 = no :(      |')
print('|___________________|')

while True:
    answer=input("Answer: ")
    if answer=='1':
        GameOn=True
    elif answer=='2':
        print("\nCARNIVAL MAN: Okay... Well, remember to keep your psychic powers trained and healthy by coming back to my booth! See you soon!!!! Bye!!!!!")
        print("\n***GAME OVER***")
        break
    else:
        print("CARNIVAL MAN: I don't understand...")

