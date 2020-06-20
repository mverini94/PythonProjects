'''
Author....: Matt Verini
Assignment: Lab09 Student Class
Date......: 04/11/2020
Program...: Student Class with Methods
'''

'''
Add three methods to the Student class that compare two objects.
One method should test for equality. A second method should test
less than. The third method should test for greater than or equal
to. In each case, the method returns the result of the comparison
of the two student's names. Include a main function that test all
restrictedsavingsaccount.py
'''

'''
This project assumes that you have completed assignment 9.1. Place
several Student objects into a list and shuffle it. Then run the
sort method with this list and display all of the student's info.
'''

import random

class Student(object):
    """Represents a student."""

    def __init__(self, m_name, number):
        """All scores are initially 0."""
        self.name = m_name
        self.scores = []
        for count in range(number):
            self.scores.append(0)


    def getName(self):
        """Returns the student's name."""
        return self.name

  
    def setScore(self, index, score):
        """Resets the ith score, counting from 1."""
        self.scores[index - 1] = score


    def getScore(self, index):
        """Returns the ith score, counting from 1."""
        return self.scores[index - 1]

   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)


        """Checks to see if two objects are equal"""
    def __eq__(self, student):
        if self is student:
            return True
        elif type(self) != type(student):
            return False
        return self.name == student.name


        """Checks to see if an object is less than another."""
    def __lt__(self, student):
        return self.name < student.name


        """Checks to see if an object is Greater than or Equal
        to another."""
    def __ge__(self, student):
        return self.name > student.name or self.name == student.name

 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    

def main():
    """A simple test."""
    print("\nFirst Student: ")
    student1 = Student("Ken", 5)
    for index in range(1, 6):
        student1.setScore(index, 100)
    print(student1)

    print("\nSecond Student:")
    student2 = Student("Ken", 5)
    print(student2)

    print("\nThird Student:")
    student3 = Student("Matthew", 5)
    print(student3)

    print("\nRunning a check to see if student1 " + \
          "and student 2 are equal: ")
    print(student1.__eq__(student2))

    print("\nRunning a check to see if student1 " + \
          "and student 3 are equal: ")
    print(student1.__eq__(student3))

    print("\nRunning a check to see if student1 " + \
          "is greater than or equal to student3: ")
    print(student1.__ge__(student3))

    print("\nRunning a check to see if student1 " + \
          "is less than student3: ")
    print(student1.__lt__(student3))

    print()

    studentObjList = []
    for counter in range(8):
        students = Student(str(counter + 1), 5)
        studentObjList.append(students)

    random.shuffle(studentObjList)
    studentObjList.sort()

    for studentObj in studentObjList:
        print(studentObj)


        
if __name__ == "__main__":
    main()
        
