from scipy import constants
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(self.make, self.model, self.year, end=" ")

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(self.doors)

class Truck(Vehicle):
    def __init__(self, make, model, year, bed_length):
        super().__init__(make, model, year)

        if bed_length < 0:
            raise ValueError("Bed length for truck cannot be negative")
        self.bed_length = bed_length

    def display_info(self):
        super().display_info()
        print(self.bed_length)

bmw = Car('BMW', 'i213', '2015', 5)
bmw.display_info()

iveco = Truck('Iveco', 'alabala', '2020', 2.3)
iveco.display_info()