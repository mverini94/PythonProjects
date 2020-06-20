
import pickle

class Automobile(object):

    def __init__(self, color = 'Grey', make = 'Ford', model = 'Saleen', year = 2008, sellingPrice = 30000.00, mileage = 40000, msrp = 35000.00):
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.sellingPrice = sellingPrice
        self.mileage = mileage
        self.msrp = msrp


    def __str__(self):
        return "Color : " + self.color + "\nMake : " + self.make + "\nModel : " + self.model + "\nYear : " + str(self.year) + \
               "\nSelling Price : " + str(self.sellingPrice) + "\nMiles/Gallon : " + str(self.mileage) + \
               "\nManufacturer Suggested Retail Price : " + str(self.msrp)


menu = '''
       1.) Add a new vehicle
       2.) Remove a vehicle
       3.) List all vehicles
       4.) List undervalued vehicles
       5.) Exit
       '''


def main():
    sampleCar = Automobile()
    print(sampleCar)
    
    

if __name__ == "__main__":
    main()
    
