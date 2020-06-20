'''
Author....: Matt Verini
Assignment: HW06 Add a Command
File......: AddCommanyProgram.py
Date......: 4/04/2020
Program...: Program that allows user to view contents
            of a file in a current working directory
            using a command.
'''

'''
Add a command to this chapter's case study program that allows
the user to view the contents of a file in the current working
directory. When the command is selected, the program should
display a list of filenames and a prompt for the name of the
file to be viewed. Be sure to include error recovery.
'''

import os, os.path

COMMANDS = ('1', '2', '3', '4' ,'5', '6', '7', '8')

MENU = '''
       1.) List the current Directory
       2.) Move up
       3.) Move down
       4.) Number of files in the directory
       5.) Size of the directory in bytes
       6.) Search for a filename
       7.) View the contents of a file
       8.) Quit the program
       '''

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == '8': #8
            print("Have a nice day!")
            break


def acceptCommand():
    '''Inputs and returns a legitimate command number.'''
    command = input("Enter a number: ")
    if command in COMMANDS:
        return command
    else:
        print("Error: command not recognized")
        return acceptCommand()


def runCommand(command):
    '''Selects and runs a command.'''
    if command == '1':
        listCurrentDir(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown(os.getcwd())
    elif command == '4':
        print("The total number of files is", \
              countFiles(os.getcwd()))
    elif command == '5':
        print("The total number of bytes is", \
              countBytes(os.getcwd()))
    elif command == '6':
        target = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found!")
        else:
            for fileObject in fileList:
                print(fileObject)
    elif command == '7':
        viewFileContent(os.getcwd())
    elif command == '8':
        exit


def listCurrentDir(dirname): #1
    '''Prints a list of the cwd's contents.'''
    directoryList = os.listdir(dirname)
    for element in directoryList:
        print(element)


def moveUp(): #2
    '''Moves up to the parent directory.'''
    os.chdir("..")


def moveDown(currentDir): #3
    '''Moves down to the named subdirectory if it exists.'''
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and \
       os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("ERROR: no such name")
        

def countFiles(path): #4
    '''Returns the number of files in the cwd
       and all its subdirectories.'''
    count = 0
    directoryList = os.listdir(path)
    for element in directoryList:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    return count


def countBytes(path): #5
    '''Returns the number of bytes in the cwd
       and all its subdirectories.'''
    count = 0
    directoryList = os.listdir(path)
    for element in directoryList:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count


def findFiles(target, path): #6
    '''Returns a list of the filenames that contain
       the target string in the cwd and all its
       subdirectories.'''
    files = []
    directoryList = os.listdir(path)
    for element in directoryList:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
            else:
                os.chdir(element)
                files.extend(findFiles(target, os.getcwd()))
                os.chdir("..")
    return files


def viewFileContent(dirname): #7
    '''Allows user to view the contents of a file in the
    current working directory.'''
    directoryList = list(filter(os.path.isfile, os.listdir(dirname)))
    if len(directoryList) == 0:
        print("No files exist inside this directory")
    else:
        while True:
            print("Files that exist inside ", dirname, ": ")
            for element in directoryList:
                print(element)
            fileName = input("Please enter the name of a file from the list provided: ")
            if not fileName in directoryList:
                print("ERROR: That is not one of the file names listed.")
            else:
                fileObject = open(fileName, 'r')
                print(fileObject.read())
            break                


if __name__ == "__main__":
    main()
