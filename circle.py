import math

class Circle(object):
    def __init__(self, radius=1):
        self._radius = 0.0
        self._diameter = 0.0
        self._area = 0.0
        self.radius = float(radius)

    def __repr__(self):
        return "Circle({})".format(int(self.radius))

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._diameter

    @property
    def area(self):
        return self._area

    @radius.setter
    def radius(self, radius):
        if radius < 0.0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
        self._diameter = self._radius * 2
        self._area = math.pi * self._radius * self._radius

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0.0:
            raise ValueError("Diameter cannot be negative")
        self._diameter = diameter
        self._radius = self.diameter / 2
        self._area = math.pi * self._radius * self._radius

