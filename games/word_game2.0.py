# if choice == 1:
    # word=random.choice(fruits)
# elif choice == 2:
    # word=random.choice(animals)
# elif choice == 3:
    # word=random.choice(computerparts)

# def LevelChoice():
    # global word
    # levelchoice = input("what level do you want?")
    # levelchoice= (int(levelchoice)):
    # if levelchoice==1:
        # word=random.choice(fruits)
    # elif levelchoice==2:
        # word=random.choice(animals)
    # elif levelchoice==3:
        # word=random.choice(computerparts)

# def Game():
    # tries=0
    #guess=random.choice
    # GameOn = True
    # while GameOn:
        # guessfunction()
        # guess += guess

import os, random
while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
# **************************************************************