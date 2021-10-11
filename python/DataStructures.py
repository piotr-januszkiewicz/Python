from collections import deque

List = [1, 2, "a"]
List2 = ["whaaat", 1.22, "smack", True]
# add new element
List.append("b")
print(List)
List[len(List):] = ["c"]    # same as append but fancy
print(List)

# insert new element into position
List.insert(2, 3)
print(List)

# extend a list by another list
List.extend(List2)
print(List)

# remove first element that matches argument
List.remove("b")
print(List)

# remove element by given index
del List[1]
print(List)

# pop element from given position. If blank returns last item
x = List.pop(2)
y = List.pop()
print("x: ", x, " y: ", y)
print(List)

# clear whole list
List.clear()
print(List)
List.append(3)
print(List)
del List[:]     # Fancy clear()
print(List)

# return index of first value that is equal to argument list.index(x[, start[, end]])
# start and end are optional and meant to search in a subsequence
List = [1, 2, 2, 2, 1, 0]
print(List.index(2))

# return number of items equal to argument
print(List.count(2))

# sort a list. Doesn't work with mixed str and int
print(List)
List.sort()
print(List)

# sort descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# reverse order
List.reverse()
print(List)

# Lists can be used as Stack by using methods append() and pop() (LIFO)
Stack = [1, 2, 3]
Stack.append(4)
Stack.append(5)
Stack.pop()

# Lists can be used as Queues (FIFO)
Queue = deque(["Eric", "John"])

Queue.append("Terry")
Queue.append("Serge")
Queue.popleft()     # Eric left
Queue.popleft()     # John left

# Lists Comprehensions
# newlist = [expression for item in iterable if condition == True]
# 1. Square roots
SquareRoots = []
for i in range(10):
    SquareRoots.append(i**2)
print(SquareRoots)
SquareRoots.clear()

SquareRoots = [i**2 for i in range(10)]  # Same effect
print(SquareRoots)
SquareRoots.clear()

SquareRoots = list(map(lambda i: i**2, range(10)))  # Same effect
print(SquareRoots)
SquareRoots.clear()

# 2. Combine elements of two lists if they are not equal
n = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(n)

# 3. Tuple made of number and its square
n = [(x, x**2) for x in range(10)]
print(n)

# 4. calling a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
n = [XDDD.strip() for XDDD in freshfruit]
print(n)

# 5. Flatten a list
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [variable for element in vec for variable in element]
print(n)

# Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# 1. Matrix transposition
n = [[row[i]for row in matrix] for i in range(4)]
print(n)

print(list(zip(*matrix)))   # same as above but easier

# del function
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]        # [1, 66.25, 333, 333, 1234.5]
del a[2:4]      # [1, 66.25, 1234.5]
del a[:]        # []

##########################################################################################
# Tuples
# ordered, unchangeable, allow duplicates
t1 = 1, 191.333, "mf"
t2 = t1, (111, 222, 432)
print(t2)       # ((1, 33, 45, 191.333, 'mf'), (111, 222, 432))

x, y, z = t1
print(x, y, z, " == ", t1)  # 1 191.333 mf  ==  (1, 191.333, 'mf')

tup1 = 1, 2, 3, 4, 5, 6
# tup1[2] = 8         # tuple doesn't support item assignment
print(tup1)

tup2 = ([1, 2, 3], [4, 5, 6])   # but you can modify e.g. a list in tuple
tup2[0][1] = 5
print(tup2)

# unpacking tuples using asterisk *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

(blue, *numb, brown) = fruits
print(blue)
print(numb)
print(brown)

# multiplying tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

##########################################################################################
# Sets
# duplicates not allowed, unchangeable(but you can add items), unordered

newSet = set(("apple", "banana", "mango"))  # set constructor
anotherSet = {"pomegranate", }

# adding new element

newSet.update(anotherSet)
print(newSet)
newSet.add("orange")
print(newSet)

# deleting methods
newSet.remove("banana")     # if there is no 'banana' in set error will be raised
newSet.discard("banana")    # no errors, even if 'banana' isn't in set
print(newSet.pop())
newSet.clear()              # empties the set
del newSet                  # delete the set completely

for x in anotherSet:
    print(x)

# joining items
otherSet = {1, 2, 3, 444.7, "apple", "pomegranate"}

set1 = otherSet.union(anotherSet)
otherSet.update(anotherSet)
print(set1)
print(otherSet)

otherSet.intersection_update(anotherSet)    # keeping only duplicate elements
print(otherSet)

otherSet.symmetric_difference_update(anotherSet)    # keeping elements not present in both sets
print(otherSet)


# Dictionary
dick = {
"model" : "ford mustang",
"color" : "red",
"year"  : 1964
}

# show dictionary keys and values
print(dick.keys())
print(dick.values())

# adding new item

dick["engine"] = "V8"
print(dick)

# check if key exists

if "year" in dick:
    print("yes, it is there")

# extend dictionary by another dictionary using update() method

dick.update({"petrol" : "pb95"})
print(dick)

# pop _ element from dictionary

print(dick.popitem())       # _ = last inserted
print(dick.pop("color"))    # _ = given

# for loop

for x in dick:      # print keys
    print(x)

for x in dick:      # print values
    print(dick[x])

for x in dick.values():  # print values
    print(x)

for x,y in dick.items():    # print key and value
    print(x, y)

# nested dictionaries

child1 = {
    "name" : "tobias",
    "age" : 10
}

child2 = {
    "name" : "Lindsey",
    "age" : 12
}

children = {
    "member1" : child1,
    "member2" : child2
}

print(children)