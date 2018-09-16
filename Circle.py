import math

class Circle:        
    def __init__(self, radius=0):
        self.radius = radius

    def input(self):
        self.radius = int(input("Enter radius: "))

    def display(self):
        print("Circle({})".format(self.radius))
    
    def displayDiameter(self):
        print("Circle diameter: {}".format(self.radius * 2))

    def area(self):
        print("Area: {}".format(math.pi * self.radius * self.radius))

    def __add__(self, other):
        r = other.radius + self.radius
        return Circle(r)

    def __eq__(self, other):
        return other.radius == self.radius

    def compare(self, c):
        if c.radius > self.radius:
            return 1
        else:
            if c.radius == self.radius:
                return 0
            else:
               return -1


circle1 = Circle(10)
circle1.display()
circle1.area()
circle1.displayDiameter()

circle2 = Circle()
circle2.input()

circle3 = circle1 + circle2
print(circle1 == circle2)
circle3.display()