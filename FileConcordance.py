'''
Author....: Matt Verini
Assignment: Lab05 
Date......: 3/04/2020
Program...: Program to track unique words in a file
            and the frequency in which they appear
            in alphabetical order
'''

'''
A file concordance tracks the unique words in a file and their
frequencies. Write a program that displays a concordance for a
text file. The program should output the unique words and their
frequencies in alphabetical order. Variations are to track
sequences of two words and their frequencies, or n words and
their frequencies.
'''

fileName = input("\nEnter the file you would like to access: ")

print(" ")

words = {}

f1 = open(fileName, "r")

f1Content = f1.readlines()

for lines in f1Content:
    for word in lines.split():
        word = word.upper()
        if word not in words:
            words[word] = 1
        else:
            words[word] +=1
            
itemsOfword = list(words.items())
itemsOfword.sort()


for i, j in itemsOfword:
    print(i, ": ", j)

f1.close()

