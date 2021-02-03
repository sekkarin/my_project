class Car:
    # attributes
    color = "No brand yet"
    brand = "No brand yet"
    number_of_seats = 4
    number_of_wheels = 1
    maxSpeed = 0
    registration_number = 0

    def __init__(self, color, brand, number_of_seats, number_of_wheels, maxSpeed):
        self.color = color
        self.brand = brand
        self.number_of_seats = number_of_seats
        self.number_of_wheels = number_of_wheels
        self.maxSpeed = maxSpeed
        self.registration_number += 1
    # method

    def setColor(self, x):
        self.color = x
    def setBrand(self,x):
        self.brand = x
    def setNumberOfseats (self,x):
        self.number_of_seats = x
    def setNumberOfwheels (self,x):
        self.number_of_wheels = x
    def setRegistration (self,x):
        self.registration_number = registration_number
    def setMaxSpeed (self,x):
        self.maxSpeed = maxSpeed
    def printData (self):
        print("The color of this car is : ",self.color)
        print("The car was manufactured by : ",self.brand)
        print("The number of seats is : ",self.number_of_seats)
        print("The number of wheels is : ",self.number_of_wheels)
        print("The maxiumum speed is : ",self.maxSpeed)
        print("The regitration numer : ",self.registration_number)

#Creating instance and use it
car1 = Car('red','Toyota',4,4,150)
car1.printData()
print('\n')
car1.color = ("blue")
car1.printData()
print("Car 2")
car2 = Car('yello','Honda',4,4,180)
car2.printData()
