'''
Author: Matt Verini
Review for Selection Statement Quiz
'''

import math

area = float(input("Enter the area: "))


if area > 0:
    radius = (area/math.pi)
    print("The radius is, ", round(radius, 2))
else:
    print("Error. The area must be a positive number.")


print(" \n")


numGrade = int(input("Enter a numeric grade for the student being assessed: "))

if numGrade > 89:
    letter = 'A'
    print(letter)
elif numGrade > 79:
    letter = 'B'
    print(letter)
elif numGrade > 69:
    letter = 'C'
    print(letter)
else:
    letter = 'F'
    print("You failed with an ", letter)


'''
Sometimes code will have multiple conditions on a single line. If we take the
same example, we can make sure the user is within a number grade of 0-100
by checking to make sure they do not enter a number under 0 or over 100
'''

numberGrade = int(input("Enter a numeric grade between 0 and 100: "))

if numberGrade > 100 or numberGrade < 0:
    print("Error. Grade must be between 0 and 100.")

print(" \n")

'''
In this part of the code, we will be examining the while loop selection statement
in Python.
In a while loop, the condition is tested at the top of the loop to see if we can
enter the loop to test other conditions specified within. If you do not break
out of a while loop properly, you can get yourself stuck in an infinite loop.
'''


theSum = 0.0

data = input("Enter a number or just enter to quit: ")

while data != "":
    number = float(data)
    theSum = theSum + number
    data = input("Enter a number or just enter to quit: ")
    print("The sum is ", theSum)
































