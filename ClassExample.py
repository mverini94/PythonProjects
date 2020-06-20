'''
Class Example
'''


class Student(object):
    '''Represents a Student'''

    def __init__(self, name, number):
        '''All scores are initially 0'''
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        '''Returns the student's name'''
        return self.name

    def setScore(self, index, score):
        '''Resets the ith score, counting from 1.'''
        self.scores[index - 1] = score

    def getScore(self, index):
        '''Returns the ith score, counting from 1.'''
        return self.scores[index - 1]

    def getAverage(self):
        '''Returns the average score.'''
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        '''Returns the highest score.'''
        return max(self.scores)

    def __str__(self):
        '''Returns the string representation of the student.'''
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    '''A simple test.'''
    student1 = Student("Ken", 5)
    print(student1)
    for index in range(1, 6):
        student1.setScore(index, 100)
    print(student1)

if __name__ == "__main__":
    main()








    
