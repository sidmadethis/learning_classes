class Car():
    """a simple attempt to model a car"""

    def __init__(self, make, model, year):
        """initialize attributes for a car"""
        self.make = make
        self.model = model
        self.year = year
        # you can put an initial value on an attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return neatly formatted name"""
        long_name = str(self.year)+ ' '  +self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """print statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading)+ " miles on it")

    def update_odometer(self, mileage):
        """set the odometer reading to the given value."""
        self.odometer_reading = mileage


class ElectricCar(Car):
    """represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """initialize attributes of the parent class"""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# note this doesn't work on python2.7, but on python3 it is fine to have super without any arguments.

# this is what it would be in python2.7
# class Car(object)
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super(ElectricCar,self).__init__(make, model, year)

# the super function is a special function that helps python make connections between parent and child classes
