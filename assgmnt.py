#circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        self.area = 3.14 * self.radius * self.radius
        print("Area =", self.area)
    def circumference(self):
        self.circumference = 2 * 3.14 * self.radius
        print("Circumference =", self.circumference)
    def diameter(self):
        self.diameter=2*self.radius
        print("diameter= ",self.diameter)
c1 = Circle(5)
c1.area()
c1.circumference()
c1.diameter()

