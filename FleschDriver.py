'''
Author....: Matt Verini
Assignment: HW04 Flesch Text Analysis
Date......: 2/29/2020
Program...: Program to compare content of two text files
'''

sentences = int(input("Sentences: "))
words = int(input("Words: "))
syllables = int(input("Syllables: "))

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)

print("Flesch Index: ", index)

level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

print("Grade Level: ", level)

