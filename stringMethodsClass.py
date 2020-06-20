
import random

sentence = "This sentence has no long words."

print(len(sentence))

listOfWords = sentence.split()

print(listOfWords)

f = open("practiceFile.txt", 'w')

for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + '\n')

f.close()

