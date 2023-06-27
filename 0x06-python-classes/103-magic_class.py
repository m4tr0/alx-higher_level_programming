import math

class MagicClass:
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = value
