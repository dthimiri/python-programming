"""Vehicles Inheritance"""

class Vehicle():

    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4 # full tank gas

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print("The {} {} goes VROOOM!" .format(self.color, self.manuf))
        else:
            print("The {} {} is out of gas :(" .format(self.color, self.manuf))

class Car(Vehicle): # Inherits from Vehicle class

    # turn on radio
    def radio(self):
        print("Music is on !")

    # rollover the window
    def window(self):
        print('The window is down, enjoy the cool breeze!')

class Motorcycle(Vehicle):

    # put on the helmet
    def helmet(self):
        print('Safety first, helmet on !')

class Ecar(Car):

    # override the inherited drive method from the Vehicle class as Car class inherits from Vehicel class
    def drive(self):
        print("The {} {} goes sssshhh!" .format(self.color, self.manuf))

my_car = Car('red', 'Mercedes')
my_mc = Motorcycle('black', 'Harley Davidson')

my_car.drive()
my_car.radio()
my_car.window()

my_mc.helmet()
my_mc.drive()
my_mc.drive()
my_mc.drive()
my_mc.drive()
my_mc.drive()
#my_mc.window()

my_ecar = Ecar('white', 'Nissan')
my_ecar.drive()
print(my_ecar.gas)