'''
Author....: Matt Verini
Assignment: Lab 03 Second Part
Date......: 2/12/2020
Program...: Program to determine a Teachers Salary percentage increase up to 10 years
'''


salary = float(input("\nEnter your starting salary: "))

percIncrease = float(input("\nEnter the percentage that your pay increases per year: "))

numYearsTeaching = int(input("\nEnter the number of years you've been teaching: "))

if numYearsTeaching <= 10:
    print("\nYear\t\t  Salary")
    print("---------------------------")
    for years in range(1, numYearsTeaching + 1):
        print("{:>2}".format(years), "{:>22.2f}".format(round(salary, 2)))
        salary = (salary * percIncrease + salary)
else:
    print("\nYou are only eligible to receive a raise up to 10 years.")

    
