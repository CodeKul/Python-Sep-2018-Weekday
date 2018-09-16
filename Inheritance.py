"""
class A:
    def __init__(self):
        self.n = 0
        print("init A")
    def display(self):
        print("Class A")

class B:
    def __init__(self):
        self.m = 0
        print("init B")
    def display(self):
        print("Class B")

# objB = B()
# objB.m

# objA = A()
# objA.n

class C(A,B):
    def __init__(self):
        self.o = 0
        print("init C")
        A.__init__(self)
        B.__init__(self)

    def display(self):
        print("Class C")
        B.display(self)
        A.display(self)

c = C()
c.display()


class Polygon:
    sides = []
    def __init__(self,n):
        super().__init__()
        self.n = n

    def inputSides(self):
        for n in range(self.n):
            side = input("Enter {} side: ".format(n))
            self.sides.append(side)

    def displaySides(self):
        for side in self.sides:
            print(side)

# p = Polygon(3)
# p.inputSides()
# p.displaySides()

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)


# t = Triangle()
# t.inputSides()
# t.displaySides()

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)


class Square(Rectangle):
    # def __init__(self):
    #     super().__init__()

    def inputSides(self):
        side = input("Enter side: ")
        for n in range(self.n):
            self.sides.append(side)


s = Square()
s.inputSides()
s.displaySides()

"""


class A:
    def __init__(self):
        self.__private__ = 10
        self._protected_ = 20

    def display(self):
        print(self.__private__)

class B(A):

    def display(self):
        print(self._protected_) 
        print(self.__private__)

class C(B):

    def display(self):
        print(self._protected_)


a = A()

# print(a.__private)
a.display()
print(a._protected_)

b = B()
b.display()

c = C()
c.display()