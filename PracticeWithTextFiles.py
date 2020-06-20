'''
Author....: Matt Verini
Assignment: HW05 
Date......: 3/23/2020
Program...: Notes from Chapter 6 on Design With Functions
'''

file = input("\nEnter the name of the file you would like to access: ")


# Actions you can take with text files
# r is the Read
# w is to Write
# a is to Append
# r+ is to read and write
f1 = open(file, "r")

fileContent = f1.readlines()

for line in fileContent:
    size_to_read = 10
    lines = line.split("\n")
    print(lines[0])

# This prints out the mode you chose which is r
# print(f1.mode)

f1.close()


