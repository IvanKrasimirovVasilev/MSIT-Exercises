class Animal:
    def __init__(self, name, id_number, race):
        self.name = name
        self.__id_number = id_number
        self.race = race

    def __str__(self):
        return f"{self.name}, {self.__id_number}, {self.race}"

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, new_id_number):
        if isinstance(new_id_number, int) and new_id_number > 0:
            self.__id_number = new_id_number


my_lion = Animal("Simba", 1, "Lion")

print(my_lion)
my_lion.id_number = "test"
print(my_lion.id_number)
print(my_lion)

# da pregoworq _id_num __id_num