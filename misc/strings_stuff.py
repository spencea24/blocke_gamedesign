# Ava Spence
# 01/31/22
# Strings array of characters
# --> has many functions

# while loop --> condition
# for loop --> counting.

import os, random
from random import random
os.system('cls')

myName= "Maria Suarez"
    # name:  M a r i a   S u a r e z 
    # index: 0 1 2 3 4 5 6 7 8 9 10 11

myStatement= """My name is so nice because
blah blah blah 

what ever
ever"""
    # """...""" = used for paragraph 
    # --> prints exactly as written
for elem in myName:
    print(elem, end=" ")
guess=random.choice(myName)
print(guess)
words= "Radio", "Clues", "Suite", "Robot",
word=random.choice(words)
print(word)

check=True
while check:
    letter=input("Dear user, please give us a nice letter: ")
    if len(letter)>1 or not letter.isalpha():
        print("BAD")
    else:
        check=False

print("ready to play the game?")


#print("My last name begins with " + myName[6])
    # the [6] = "print _______, but only position 6"
    # --> 6th character in "myName" = "S", so only "S" is printed
#print(myStatement)

#if 'blah' in myStatement:
#    print('true')
        # this means that if the word "blah" is present, a "true" will be printed
#print('expert' not in myStatement)
    # this means that myStatement will print as "true"

#INDEX= myName.find("a")
    # find() will return the index of the character u are looking for (first instance)
#print(INDEX)

# finding the length of your word
#wordLen=len(myName)
#print(wordLen)
    # last index is wordlen - 1
        # wordLen = 12, but index = 11 because it started at 0

#for loop in range 0 to limit
#for i in range(wordLen-1):
    #the i is just a "counter" --> will change to numbers 0 - 11, one by one
    #if "a" in myName[i]:
        # print(i, end=", ")
#print("")
# print("done")

#myStatement=myStatement.upper()
    # makes all letters uppercase
# print(myStatement)

#check=True
# while check:
    # letter=input("Dear user, please give us a nice letter: ")
    #if len(letter)>1 or not letter.isalpha():
        #print("BAD")
    #else:
        #check=False
#print("ready to play the game?")






greenhill: 10
portal: 5.33
totalstudents: 240
boys: 120
print(greenhill, portal, totalstudents, boys)
print("031")
print("3.561E + 02")

print ("Welcome to")
print("\nGreenhill School")