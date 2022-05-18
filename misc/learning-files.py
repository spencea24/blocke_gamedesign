# Ava Spence
# Learning files:
    # a) open/create a file
    # b) write 'w'
    # c) append 'a'
    # d) read 'r'
    # e) close file

import pygame, os, datetime
os.system('cls')
date = datetime.datetime.now()
score = 123
name = 'Jesse'
print(date.strftime('%m/%d/%Y')) # "strftime" makes it a string... can't send anything to file w/out making it a string
scoreLine=str(score) + " " + name + " " + date.strftime('%m/%d/%Y' + '\n')
print(scoreLine)

# Open a file and write stuff in it
# when you write it erases the previous
myFile = open('misc\sce.txt', 'w')
myFile.write(scoreLine)
myFile.close()

score = 123
name = 'Felicia'
print(date.strftime('%m/%d/%Y'))
scoreLine = str(score) + " " + name + " " + date.strftime('%m/%d/%Y' + '\n')
myFile = open('misc\sce.txt', 'a')
myFile.write(scoreLine)
myFile.close()
myFile = open('misc\sce.txt', 'r')
lines = myFile.readline()
print(lines)
lines = myFile.readline()
print(lines)
myFile.close()

