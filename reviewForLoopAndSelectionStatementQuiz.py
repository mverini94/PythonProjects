'''
Author: Matt Verini
Review for the quiz on for loops and selection statements
'''

for eachPass in range(4):
    print("It's alive!", end = " ")

print(" \n")

number = 2
exponent = 3
product = 1

# This will print 2 4 8 because it prints the 3 values specified by exponent
# It starts with product which is originally set to 1 but then multiplied by 2
# This loop passes 3 times so the next time it passes through the number is 2
for thisPass in range(exponent):
    product = product * number
    print(product, end = " ")

print(" \n")

for count in range(1, 5):
    product = product * count
    print(product, end = " ")

print(" \n")


lowerBound = int(input("Enter the lower bound number here: "))

upperBound = int(input("Enter the higher bound number here: "))

theSum = 0

# This is an example to show how the lowerBound always gets taken but
# The upperBound does not. We add 1 so the upperBound gets included
'''
In this example, number starts out as 1 because that is the lowerbound that is entered.
Then, it goes to 2 which gets added to 1 which was the first initial theSum that was
calculated
'''
for number in range(lowerBound, upperBound + 1):
    theSum = theSum + number
    print(theSum)

print(" \n")

'''
An important thing to understand about the range() function is that it returns a list.
You can even use a for loop to iterate over a list of characters such as a string.
For Example:

'''

# Puts a space at the end of every character of the string
for character in "Hi There":
    print(character, end = " ")

print(" \n")

'''
Range can also take a third argument after the actual range you are counting through is
specified so the program knows how many places you would like to jump in between values
For Example:

'''

# Prints every 3rd value between 1 and 29
print(list(range(1, 30, 3)))


# Will print all the values from 10 down to 1 not including 0
# takes the lower bound of 10 in this case and not the upper bound of 0
# -1 specifies that we are counting backwards
for value in range(10, 0, -1):
    print(value, end = " ")

print(" ")

for exponent in range(7, 11):
    print(exponent, 10 ** exponent)



































