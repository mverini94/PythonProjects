
import datetime

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return '__str__ for Car'


myCar = Car('red', 37281)
print(myCar)

'{}'.format(myCar)

print(str([myCar]))

print(repr(myCar))

today = datetime.date.today()
print()
'''str is used for clear representation for someone to read'''
print(str(today))
print()
'''repr is used for debugging for developers'''
print(repr(today))
