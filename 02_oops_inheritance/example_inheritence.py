
from abc import ABC, abstractmethod

class Vehicle(ABC):
    wheels = 4
    terrain = "road"
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):

    def two_door(self):
        print("Year: {}".format(self.year))

    def drive(self):
        print("overridden")

# vehicle = Vehicle("blah", "Blah", "Blah", 2020)


car = Car("red", "Acura", "TL", 2020)


# car.drive()

# print("Is car an instance of Car ? {}".format(isinstance(car, Car)))
# print("Is car an instance of Vehicle ? {}".format(isinstance(car, Vehicle)))
# print("Is car an instance of Object ? {}".format(isinstance(car, object)))


class Motorcycle(Vehicle):
    wheels = 2

    def drive(self):
        """Overriding drive: Same method signature as the base class but different implementation"""
        print("be careful out there")

        # The overridden code can be called using super or using the Base class name
        # Adds reusability. If needed by the overridden method, removes the need to re-write existing code 
        super().drive()
        Vehicle.drive(self)

class Truck(Vehicle):
    wheels = 16

    def honk(self):
        print("Honk Honk")

# truck = Truck("black", "dodge", "durango", 1999 )
# truck.drive()

motorcycle = Motorcycle("black", "Kawasaki", "whatever", 2010)
motorcycle.drive()
