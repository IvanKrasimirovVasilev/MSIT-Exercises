class Car:
    def __init__(self, id_number, brand, car_type, hp, color, fuel_usage):
        self.id_number = id_number
        self.brand = brand
        self.car_type = car_type
        self.hp = hp
        self.color = color
        self.fuel_usage = fuel_usage
        self._values = {}

    def __str__(self):
        return f"STR: {self.id_number}, {self.brand}, {self.car_type}, {self.hp}, {self.color}"

    def __repr__(self):
        return f"REPR: {self.id_number}, {self.brand}, {self.car_type}, {self.hp}, {self.color}"

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.id_number == other.id_number
        elif isinstance(other, int):
            return self.id_number == other

    def __gt__(self, other):
        return self.hp > other.hp

    def __lt__(self, other):
        return self.hp < other.hp

    def __add__(self, other):
        if isinstance(other, Car):
            return self.fuel_usage + other.fuel_usage
        raise TypeError

    def __setitem__(self, key, value):
        self._values[key] = value

    def __getitem__(self, item):
        return self._values[item]


my_car = Car(1, "Mercedes", "C-Klasse", "105", "Blue", 6)
my_car_2 = Car(1, "Audi", "A4", "100", "Blue", 5)
my_car_string = str(my_car)
#print([my_car])
#print(my_car)
#print(my_car_string)

print(1 == my_car)  # my_car.__eq__(my_car_2)
print(my_car < my_car_2)
print(my_car > my_car_2)
# print(my_car)

my_car["tires"] = "winter"   # my_car.__setitem__("tires", "winter")
print(my_car["tires"])       # my_car.__getitem__("tires")