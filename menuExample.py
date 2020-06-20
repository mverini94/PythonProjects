'''
Author:....Matt Verini
Date:......02/03/2020
'''

def menu():
    print("1.) Add user information")
    print("2.) Calculate tax return")
    print("3.) Print a tax return")
    print("4.) Save to file")
    print("5.) Exit")
    response = int(input("\nMake a selection: "))
    return response


while True: #while True keeps something going forever as long as it's true
    returnVal = menu()

    if returnVal == 1:
        print("\nYou pressed 1.")
    elif returnVal == 2:
        print("\nYou pressed 2.")
    elif returnVal == 3:
        print("\nYou pressed 3.")
    elif returnVal == 4:
        print("\nYou pressed 4.")
    elif returnVal == 5:
        print("\nYou pressed 5.")
        break
    else:
        print("\nInvalid entry. Please try again.\n")


input("\nPress any key to continue...")


