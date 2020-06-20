'''
Author....: Matt Verini
Assignment: HW 03
Date......: 2/12/2020
Program...: Program to predict population growth
'''

organisms = int(input("\nEnter the initial number of organisms: "))
growthRate = float(input("\nEnter the rate of growth (a number > 0): "))

while growthRate < 1:
    print("\nPlease enter a number greater than 0.")
    growthRate = int(input("\nEnter the rate of growth (a number > 0): "))
else:
    pass

hoursToAchieveGR = int(input("\nEnter the number of hours it takes to achieve this rate of growth: "))
totalHours = int(input("\nEnter how many hours total of growth: "))
    
population = organisms
hours = 0

while (hours < totalHours):
    population = population * growthRate
    hours = hours + hoursToAchieveGR
print("\nThe total population is ", population)
