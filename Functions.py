def display():
    print("codekul")

display()

def displayWithParam(param1, param2=10):
    print(param1)
    print(param2)

displayWithParam("Codekul", 30)


def changeThis(myList):
    myList = [10,20,30,40,50]
    print(myList)

myList = [1,2,3,4,5]
changeThis(myList)
print(myList)

def functionWithReturning():
    print("This function will return string")
    return "Codekul"

print(functionWithReturning())

def mutiplication(a,b,c=0):
    c += (a*b)

c = 0
mutiplication(10,20,c)
print(c)

def myFunc(str, int = 10):
    print("str: ",str)
    print("int", int)

myFunc(int = 30, str = "Codekul")

square = lambda a: a**2

print(square(15))

sum = lambda a,b,c,d,e: a + b + c + d + e

print(sum(10, 20, 30, 40, 50))


def function1(a, b):
    print(a)
    print(b)

def function2(function1, t):
    function1(*t)

function2(function1,(10,20))


