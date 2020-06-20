'''
Author....: Matt Verini
Assignment: HW04 Payroll Department
Date......: 2/29/2020
Program...: Program that keeps a list of employee information
            for each pay period in a text file
'''

fileName = input("\nEnter the file you would like to access: ")

print(" ")

print("{:<10}{:<10}{:<10}".format("Name", "Hours", "Pay"))

print("-" * 30)

f1 = open(fileName, "r")

f1Content = f1.readlines()

totalWagesPaid = 0

for line in f1Content:
    lineItems = line.split(",")

    name = str(lineItems[0])
    hoursWorked = float(lineItems[1])
    hourlyWage = float(lineItems[2])
    pay = hourlyWage * hoursWorked
    print("{:<10}{:<10.2f}{:<10.2f}".format(name, hoursWorked, pay))
    totalWagesPaid = totalWagesPaid + pay

print("-" * 30)
print("{:<20}{:<30.2f}".format("Total: ", totalWagesPaid))

f1.close()
