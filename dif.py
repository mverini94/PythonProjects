'''
Author....: Matt Verini
Assignment: Lab 04 dif.py
Date......: 2/24/2020
Program...: Program to compare content of two text files
'''

file1 = input("Enter the name of the first file you would like to compare: ")
file2 = input("\nEnter the name of the second file you would like to compare: ")

f1 = open(file1, "r")
f2 = open(file2, "r")


infoFile1 = f1.readlines()
infoFile2 = f2.readlines()


if infoFile1 == infoFile2:
    print("Yes")
    exit

for lines in range(0, min(len(infoFile1), len(infoFile2))):
    if infoFile1[lines] != infoFile2[lines]:
        print("\nNo:\n")
        print("Lines that do not match: ")
        print(infoFile1[lines], "/", infoFile2[lines])
