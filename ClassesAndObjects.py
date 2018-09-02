class MyClass:
    a = 0
    # def __init__(self):
    #     print("init")

    def __init__(self, a):
        self.a = a
    
    def display(self, b):
        print("Codekul - {} {}".format(self.a,b))


obj = MyClass(10)
obj.display(40)

class MyAnotherClass:
    def __init__(self):
        print("init")


obj1 = MyAnotherClass()

