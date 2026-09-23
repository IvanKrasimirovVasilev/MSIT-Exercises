from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def move(self):
        print("The car is driving")

    def stop(self):
        print("The car stopped")

vw = Car("VW")
vw.move()
vw.stop()