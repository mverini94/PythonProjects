'''
Author....: Matt Verini
Assignment: HW05 
Date......: 3/23/2020
Program...: Notes from Chapter 6 on Design With Functions
'''

'''
Objectives for this Chapter

1.) Explain why functions are useful in structuring code in a program
2.) Employ a top-down design design to assign tasks to functions
3.) Define a recursive function
4.) Explain the use of the namespace in a program and exploit it effectively
5.) Define a function with required and optional parameters
6.) Use higher-order fuctions for mapping, filtering, and reducing

- A function packages an algorithm in a chunk of code that you can call by name
- A function can be called from anywhere in a program's code, including code
  within other functions
- A function can receive data from its caller via arguments
- When a function is called, any expression supplied as arguments are first
  evaluated
- A function may have one or more return statements
'''


def summation(lower, upper):
    result = 0
    while lower <= upper:
        result += lower #result = result + lower
        lower += 1 #lower = lower + 1
        print(result)

summation(1, 4)

'''
- An algorithm is a general method for solving a class of problems
- The individual problems that make up a class of problems are known
  as problem instances
  - What are the problem instances of our summation algorithm?
- Algorithms should be general enough to provide a solution to many
  problem instances
  - A function should provide a general method with systematic variations
- Each function should perform a single coherent task
- Such as how we just computed a summation
'''


'''
TOP-DOWN Design starts with a global view of the entire problem and
breaks the problem into smaller, more manageable subproblems
- Process known as problem decomposition
- As each subproblem is isolated, its solution is assigned to a function
- As functions are developed to solve subproblems, the solution to the
  overall problem is gradually filled ot.
- Process is also called STEPWISE REFINEMENT
- STRUCTURE CHART - A diagram that shows the relationship among a
  program's functions and the passage of data between them.
- Each box in the structure is labeled with a function name
  - The main function at the top is where the design begins
  - Lines connecting the boxes are labeled with data type names
  - Arrows indicate the flow of data between them
'''

























