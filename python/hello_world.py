#R3
#Z1
print("Trzy")
print("różne")
print("łańcuchy")
#Z2
x=100
if x==10:
    print("x jest równe 10")
else:
    print("x nie jest równe 10")
#Z3
if x<=10:
    print("x<=10")
elif x<=25 and x>10:
    print("x>10 & x<=25")
else:
    print("x>25")
#Z4
print(24//10)
#Z5
print(24/10)
#Z6
age=28
for i in range(100):
    if i == age:
        print(i)
        break

def function_py(x):
    return 2*x

print(function_py(2))
print(function_py(3))
print("////////////////////////////")
print(len("Python is good")) #zwraca ilość znaków
print(str(155)) #zwraca 155 typu string
print(int(1.57)) #zwraca obiekt typu int
print(float(100))#zwraca obiekt typu float
def potęga(x=1): #funkcja z parametrem opcjonalnym
    return x**x
print(potęga(4))

def function():
    global age
    age+=5
    return age

print("///////////////////////////////")
print(age)
print(function())
print(age)#przekazanie zmiennej globalnej powoduje modyfikację oryginału

#mechanizm wyjątków
try:
    a= input("podaj liczbę a: ")
    b= input("podaj liczbę b: ")
    a=int(a)
    b=int(b)
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("podaj prawidłowe liczby")

#łańcuchy dokumentujące
def f(x=1,y=1):
    """function adds 2 elements
    :param x: int
    :param y: int
    :return: sum x+y"""
    return x+y

print(f())

#R4
#Z1
def square_root(x):
    return x**2
print(square_root(4))

#Z2
def string_str():
    return input("napisz coś: ")
print(string_str())

#Z3
def function(a,b,c,x=1,y=5):
    return a+b+c+x+y
print(function(1,1,1,2))

#Z4
def func1():
    try:
        a=input("number 1: ")
        a=int(a)
        return a/2
    except ValueError:
        print("not a valid number")

def func2(a):
    try:
        return a*4
    except (ValueError, TypeError):
        print("not a valid number")
a=func1()
b=func2(a)
if(b):
    print(b)
#Z5
def convert(x):
    try:
        a=float(x)
        return a
    except ValueError:
        print("sorry, couldn't convert")
print(convert("hello"))

