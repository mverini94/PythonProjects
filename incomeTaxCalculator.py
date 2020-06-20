'''
Author....: Matt Verini
Assignment: Homework 02
Date......: 2/05/2020
Program...: This program is designed to calculate income tax
'''

stanDeduction = 10000.0
depenDeduction = 3000.0
taxRate = .20

grossIncome = float(input("Please enter your gross income: "))
numOfDependents = int(input("Please enter your number of dependents: "))

income = grossIncome - stanDeduction - (depenDeduction * numOfDependents)

incomeTax = income * taxRate

print("Your income tax is $", round(incomeTax, 2))
