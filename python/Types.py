'''
DATA TYPES:
    int
    str
    float
    bool
    complex
    list
    tuple
    dictionary
    set
    frozen set
    range

    bytes
    bytearray
    memory view
'''

#INT
x=15
print(x)
print(type(x))

#STR
x="hello there"
print(x)
print(type(x))

#FLOAT
x=1.154
print(x)
print(type(x))

#BOOL
x=True
print(x)
print(type(x))

#COMPLEX
x=3j
print(x)
print(type(x))

#LIST
x = ["i", "don\'t", "know"]
print(x)
print(type(x))

#TUPLE
x = ("simple", "Tuple")
print(x)
print(type(x))

#DICTIONARY
x = { 1: "general", 2: "Kenobi"}
print(x)
print(type(x))

#SET
x = {3, "heyy"}
print(x)
print(type(x))

#FROZENSET
x = frozenset({111,222,"hola todos!"})
print(x)
print(type(x))

#RANGE
x = range(100)
print(x)
print(type(x))

#BYTES
x = b"wilkommen sie bitte!"
print(x)
print(type(x))

#BYTEARRAY
x = bytearray(3)
print(x)
print(type(x))

#MEMORYVIEW
x = memoryview(b"Where am I?")
print(x)
print(type(x))