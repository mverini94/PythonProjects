'''
Author....: Matt Verini
Assignment: Lab05 
Date......: 3/04/2020
Program...: Program that allows the user to navigate
            the lines of text in a file
'''

'''
Write a program that allows the user to navigate the lines of text in a file.
The program should prompt the user for a fileName and input the lines of text
into a list. The program then enters a loop in which it prints the number of
lines in the file and prompts the user for a line number (line numbers range
from 0 to the number of lines in the file). If the input is 0, the program
quits. Otherwise the program prints the line associated with that number.
'''


fileName = input("\nEnter the file you would like to access: ")

print(" ")

f1 = open(fileName, "r")

f1Content = f1.readlines()

lineList = []

lineCount = 0

for line in f1Content:
    lineCount += 1
    lineList.append(line)


while True:
    print("This file has ", str(lineCount), " lines of text.\n")
    numOfLine = int(input("Enter a line number within range of total lines" \
                          "(Enter 0 to quit): "))
    if numOfLine == 0:
        exit
    elif numOfLine > lineCount:
        print("\nError: Your input is too large for the amount of lines in this file!!!!\n")
        continue
    else:
        print("\n", numOfLine, ": ", lineList[numOfLine - 1])
        continue
    break

f1.close()
