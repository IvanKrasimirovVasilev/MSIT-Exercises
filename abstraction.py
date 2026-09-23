from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, id_number):
        self.name = name
        self.__id_number = id_number

    def __str__(self):
        return f"{self.name}, {self.__id_number}"

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, new_id_number):
        if isinstance(new_id_number, int) and new_id_number > 0:
            self.__id_number = new_id_number

    @abstractmethod
    def make_noise(self):
        print("The Animal makes a noise")

class Lion(Animal):
    def make_noise(self):
        print("GROOOOOOWL")

class Zebra(Animal):
    def make_noise(self):
        super().make_noise()
        # print(f"Hello, I am {self.name}")

class Elephant(Animal):
    def make_noise(self):
        print("TÖRÖÖÖÖÖÖ")

my_lion = Lion("Simba", 1)

my_zebra = Zebra("George", 2)

my_elephant = Elephant("Benjamin", 3)

my_zebra.make_noise()
my_lion.make_noise()
my_elephant.make_noise()

print(my_lion)
my_lion.id_number = "test"
print(my_lion.id_number)
print(my_lion)