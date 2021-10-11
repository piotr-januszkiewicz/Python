import json

print("isn't it")
print('isn\'t it')      # using '\' allows you to use single quote here

print("C:\some\name")
print(r"C:\some\name")  # adding 'r' before string will disable the special character '\'
print("""HE\
RE
IS
A
FANCY
WAY
TO
PASS
STRING""")

string = "un"
print(string*3 + "ium")

print("putting several strings within same parentheses" " makes it glued together")     # doesn't work with variables

# string can be indexed
Python = "Python"
print(Python[0])
print(Python[-0])   # -0 == 0
print(Python[1])
print(Python[-1])

# slicing (slicing string into substrings)
print(Python[1:4])  # yth
print(Python[:5])   # Pytho
print(Python[-4:])  # Py
print(Python[:])    # Python

a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a+b

# string modifying

# upper case
x = "    Random string    "
print(x.upper())

# lower case
print(x.lower())

# removing whitespaces
print(x.strip())

# replacing string
print(x.replace("r", ''))

# split string
print(x.split('r'))


# string format
age = 15
height = 180
color = "Brown"

sentence = "A man, age {}, {} tall and with {} hair"
print(sentence.format(age, height, color))

sentence = "A man, age {2}, {1} tall and with {0} hair"
print(sentence.format(color, height, age))              # same as above but with arguments placed

# JSON - used for storing data (don't have to do strange convertions: int->str then str->int)

x = ["simple", "list", 'a', 12.22, 188]

f = open("f.txt", "w")
json.dump(x, f)
f.close()

f = open("f.txt", "r")
print(json.load(f))
f.close()

# LAMBDA - anonymous function, unlimited arguments, one expression
# lambda [arguments] : [expression]

def my_func(a):
    return lambda b: b*a

expr = my_func(2)
print(expr(3))  # 6

