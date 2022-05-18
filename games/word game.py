# Ava Spence
# 2/8/22
# Word game w/ 3 levels
    # 1. fruits
    # 2. animals
    # 3. computer parts

# Create word lists

import os, random
os.system('cls')

word=""
guess=""
def selectword():
    global word
    fruits=["banana","grape", "watermelon", "papaya", "orange", "tomato", "mango", "kiwi", "apple", "strawberry", "blackberry", "raspberry", "blueberry"]

#size= len(fruits)
# randy=random.randint(0,size)
# print(randy)
# word=fruits[randy]
# print(word)
    word=random.choice(fruits)

def menu():
    print(" ################################################## ")
    print(" |                                                | ")
    print(" |                                                | ")
    print(" |                 word game menu                 | ")
    print(" |                  (placeholder)                 | ")
    print(" |                                                | ")
    print(" |    1. fruits   2. animals   3. computer parts  | ")
    print(" |                                                | ")
    print(" |                                                | ")
    print(" ##################################################" )
                                                                                       
menu()                                                                                       

# checking for correct user input
check=True
while check:
    gameType=input("\npick a category: ") 
    try:
        gameType=int(gameType)  
        if gameType >0 and gameType <4:
            check=False
        else:
            print("you can only pick a category betwwen 1 - 3...")    
    except ValueError:
        print("xx error xx : incorrect input")

def randomNum():
    global guess
    global level
    if gameType==1:
        selectword
    if gameType==2:
        selectword
    if gameType==3:
        selectword
                                                                                  
def guessfunction():
    global guess
    check=True
    while check:
        try:
            guess=input("\nenter a letter: ")
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                print("only one letter please!")
        except ValueError:
            print("xx error xx")

# if choice == 1:
    # word=random.choice(fruits)
# elif choice == 2:
    # word=random.choice(animals)
# elif choice == 3:
    # word=random.choice(computerparts)

# def Game():
    # tries=0
    #guess=random.choice
    # GameOn = True
    # while GameOn:
        # guessfunction()
        # guess += guess



GameOn=True
tries=0
letterGuessed=""
selectword()
while GameOn:
    guessfunction()
    letterGuessed += guess # letterGuessed=letterguessed + guess
    if guess not in word:
        tries +=1
        print(tries) #for testing-- delete when game is ready!!!!!!!!
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    if tries>6:
        print("\ngame over")
        #playGame() ask if they want to play again
    if countLetter == len(word):
        print ("\nyou guessed the word yaaaaay")

