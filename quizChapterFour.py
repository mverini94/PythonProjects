

'''
len function returns the strings length which is the number of characters it contains
'''

print(len("Hi There!"))

data = "Hi There!"

for index in range(len(data)):
    print(index, data[index])

'''
- Python's subscript operator can be used to obtain a substring through a process
  called slicing
- Place a colon (:) in the subscript; an integer value can appear on either side
  of the colon
'''

name = "myfile.txt"

# This prints 'myfile.txt'
print(name[0:])

# This prints 'm'
print(name[0:1])

# This prints 'my'
print(name[0:2])

# This prints 'txt'
print(name[-3:])

# This prints 't'
print(name[-1:])

'''
something important to note is that this will print (file).
that is because in myfile.txt it starts from the second character
which is (y) and grabs everything after that including the 6th character
'''
print(name[2:6])
print(name[-8:])

fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]

# Grabs the files that end in .txt from the array
for fileName in fileList:
    if ".txt" in fileName:
        print(fileName)

'''
Data Encryption can be used to protect information transmitted on networks
One or more keys are used to Encrypt messages to produce cipher text, and
to decrypt cipher text back to its original plain text form
'''

# Caesar cipher replaces each character in plain text with a character given
# a distance away


'''
The ord function returns the ordinal position in the ASCII sequence
The chr is the inverse function
'''


plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the disance value: "))

code = " "

for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
                      (ord('z') - ordValue + 1)
        code += chr(cipherValue)
    print(code)

code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))

plainText = " "















