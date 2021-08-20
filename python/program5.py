#KLASY
import math

class Orange:
    def __init__ (self, w, c):            #self - zmienna instancyjna
        self.weight = w             #__init__ - metoda magiczna (__[nazwa]__) - inicjowanie obiektu
        self.color = c
        self.mold = 0                                                                                             
        print("Hello, Orange!")
        
    def rot (self, days, temperature):
        self.mold = days*temperature


def show(param1, param2):
    print(param1)
    print(param2)

orange = Orange(256, "pomarańczowy")
print(orange)

show(orange.weight, orange.color)

orange.weight = 420
orange.color = "like a weed bruh"

show(orange.weight, orange.color)

orange.rot(10, 13)
print(orange.mold)

#R12
#Z1
class Apple:
    def __init__(self,a,b,c):
        self.color = a
        self.weight = b
        self.price = c
        self.mold = 5
        print("new apple appeared.")

newApple = Apple(3,6,9)

#Z2
class Circle:
    def __init__(self, a):
        Circle.radius = a
        print("new circle applied.")
    def area(self):
        a = self.radius**2
        a = a*math.pi
        return a

circ = Circle(4)
print(circ.area())

#Z3
class Triangle:
    def __init__(self, a, h):
        Triangle.base = a
        Triangle.height = h
        print("ther iz a new triangl")

    def area(self):
        return self.base*self.height/2

triangl = Triangle(10,5)
print(triangl.area())

#Z4
class Hexagon:
    def __init__(self, a):
        Hexagon.base = a
        print("His dad gon")
    def calculate_perimeter(self):
        return 6*Hexagon.base


Hexa = Hexagon(5)
print(Hexa.calculate_perimeter())
    
    
class NewClass:
    def __init__(self):
        self.x = "Hello"

    def this_method_can_be_used_publicly(self):
        print(self.x)
        self._this_method_cant()
    def _this_method_cant(self):
        self.x = "modification inside class"

cl = NewClass()
cl.this_method_can_be_used_publicly()
cl.this_method_can_be_used_publicly()


#Dziedziczenie
class Shape:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def shape_size(self):
        print("{} x {}".format(self.length, self.length))

class Rectangle(Shape):
    def area(self):
        return self.length*self.width
    def shape_size(self):       #Przesłanianie metod
        print("prostokąt: {} x {}".format(self.length, self.length))
        
class Triangle(Shape):
    def area(self):
        return self.length*self.width/2

    
shape = Shape(10,10)
rectangle = Rectangle(15,15)
triangle = Triangle(20,20)

shape.shape_size()
rectangle.shape_size()
print(rectangle.area())
print(triangle.area())


#Kompozycja
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Owner:
    def __init__(self, name):
        self.name = name

micc = Owner("Mick Jagger")
dog = Dog("pimpek","Bulldog",micc)

print(dog.name)
print(dog.breed)
print(dog.owner.name)

#zmienne klasowe i instancyjne
class Animal:
    def __init__(self, color, age):
        self.color = color          #to są zmienne instancyjne
        self.age = age
    def print(self):
        print(self.color, self.age)

class Cat:
    cats = []                       #a to jest zmienna klasowa
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.cats.append((self.color,self.age))

animal1 = Animal("blue", 1)
animal2 = Animal("red",5)
cat1 = Cat("white",2)
cat2 = Cat("grey", 10)
cat3 = Cat("black", 8)

animal1.print()
print(Cat.cats)

#metody magiczne (__[metoda]__)
class Car:
    def __init__(self, color, Type):
        self.color = color
        self.type = Type
    def __repr__(self):                     #__repr__
        return self.color + " " + self.type

class Number:
    def __init__(self, x):
        self.number = x
    def __add__(self, other):               #__add__ 
        return self.number - other.number   #TROLOLOLO

car1 = Car("blue", "hatchback")
car2 = car1
car3 = Car("red", "kombi")
print(car1)

num1=Number(10)
num2=Number(20)
print(num1+num2)

#is - identyfikuje czy 2 obiekty są tym samym obiektem
print(car1 is car2)
print(car2 is car3)

x = 10
y = None

if x is None:
    print("non")
else:
    print("not non")

if y is None:
    print("non")
else:
    print("not non")
















    


