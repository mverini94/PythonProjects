'''
Author....: Matt Verini
Assignment: HW04 Flesch Text Analysis
Date......: 2/29/2020
Program...: Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
'''

# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, "r")
text = inputFile.read()


# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    # for vowel in vowels:
    '''
    Use the list provided by word = text.split()
    check if the items in word are in the sequence
    of the vowels
    '''
    if word[0] in vowels:
        # syllables += word.count(vowel)
        '''
        To prevent the counting of consecutive vowels
        as multiple syllables
        '''
        syllables += 1
    '''
    Iterate through the range of items in word
    '''
    for i in range(1, len(word)):
        if word[i] in vowels and word[i - 1] not in vowels:
            syllables += 1
    for ending in ['es', 'ed', 'e',]:
        if word.endswith(ending):
            syllables -= 1
        if word.endswith('le'):
            syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)

level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is ", index)
print("The Grade Level Equivalent is ", level)
print(sentences, " sentences")
print(words, " words")
print(syllables, " syllables")



