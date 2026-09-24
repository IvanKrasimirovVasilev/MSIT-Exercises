class Galaxy():
    def __init__(self, name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years, number_of_stars, number_of_planets):
        self.name = name
        self.radius_in_m = radius_in_m
        self.mass_in_kg = mass_in_kg
        self.mean_temperature_in_celsius = mean_temperature_in_celsius
        self.age_in_years = age_in_years
        self.number_of_stars = number_of_stars
        self.number_of_planets = number_of_planets

    @property
    def radius_in_m(self):
        return self.__radius_in_m

    @radius_in_m.setter
    def radius_in_m(self, new_radius_in_m):
        if not isinstance(new_radius_in_m, (int, float)):
            raise TypeError("radius_in_m must be a number")

        if new_radius_in_m <= 0:
            raise ValueError("radius_in_m must be greater than 0")

        self.__radius_in_m = new_radius_in_m

    @property
    def mass_in_kg(self):
        return self.__mass_in_kg

    @mass_in_kg.setter
    def mass_in_kg(self, new_mass_in_kg):
        if not isinstance(new_mass_in_kg, (int, float)):
            raise TypeError("mass_in_kg must be a number")
        if new_mass_in_kg <= 0:
            raise ValueError("mass_in_kg must be greater than 0")
        self.__mass_in_kg = new_mass_in_kg

    @property
    def mean_temperature_in_celsius(self):
        return self.__mean_temperature_in_celsius

    @mean_temperature_in_celsius.setter
    def mean_temperature_in_celsius(self, new_mean_temperature_in_celsius):
        if not isinstance(new_mean_temperature_in_celsius, (int, float)):
            raise TypeError("mean_temperature_in_celsius must be a number")
        self.__mean_temperature_in_celsius = new_mean_temperature_in_celsius

    @property
    def age_in_years(self):
        return self.__age_in_years

    @age_in_years.setter
    def age_in_years(self, new_age_in_years):
        if not isinstance(new_age_in_years, (int, float)):
            raise TypeError("age_in_years must be a number")
        if new_age_in_years <= 0:
            raise ValueError("age_in_years must be greater than 0")
        self.__age_in_years = new_age_in_years

    @property
    def number_of_stars(self):
        return self.__number_of_stars

    @number_of_stars.setter
    def number_of_stars(self, new_number_of_stars):
        if not isinstance(new_number_of_stars, int):
            raise TypeError("number_of_stars must be a integer")
        if new_number_of_stars <= 0:
            raise ValueError("number_of_stars must be greater than 0")
        self.__number_of_stars = new_number_of_stars

    @property
    def number_of_planets(self):
        return self.__number_of_planets

    @number_of_planets.setter
    def number_of_planets(self, new_number_of_planets):
        if not isinstance(new_number_of_planets, int):
            raise TypeError("number_of_planets must be a integer")
        if new_number_of_planets <= 0:
            raise ValueError("number_of_planets must be greater than 0")
        self.__number_of_planets = new_number_of_planets


    def summary(self):
        return f"Galaxy {self.name} has a radius: {self.radius_in_m} m, mass: {self.mass_in_kg} kg, temperature: {self.mean_temperature_in_celsius} gradC, age: {self.age_in_years} years, stars: {self.number_of_stars}, planets: {self.number_of_planets} "



milky_way = Galaxy ("milkiway", 11, 22,33,44,55,66)

print(milky_way.summary())
