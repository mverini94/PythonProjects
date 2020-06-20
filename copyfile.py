'''
Author....: Matt Verini
Assignment: Lab 04 copyfile.py
Date......: 2/24/2020
Program...: Program to input from one file and write to another
'''


inputFile = input("Enter the name of the file you will be reading from: ")
outputFile = input("\nEnter the name of the file you will be writing to: ")

file1 = open(inputFile, "r")
file2 = open(outputFile, "w")

info = file1.read()
file2.write(info)

file1.close()
file2.close()

