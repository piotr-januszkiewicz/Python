x = 20
# if statement
if x < 0:
    x = 0
    print("negative changed to 0")
elif x == 0:
    print("Zero")
elif x == 1:
    print("One")
else:
    print("More...")

# range() function
r = range(6, 15, 3)
for i in r:
    print(i)    # 6 9 12

y = 1
y = sum(range(10))  # 1+2+3+4+5+6+7+8+9+10 = 45
print(y)            # 45

seq = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(seq)):
    print(i, len(seq)-1-i, seq[i])  # 0 4 Mary ...

print(r)    # range(6, 15, 3)

# break, continue and else in loops
for i in range(2, 100):     # actually nice prime numbers algorithm
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

for i in range(1, 10):
    if i % 2 == 0:
        print("found even number ", i)
        continue
    print("found odd number ", i)

# pass statement: used when nothing is meant to happen. Can be used when a part of code is to be written

class EmptyClass:
    pass


# function returns a value
# procedure doesn't
k = 5

def func(arg=k):
    print(arg)

k = 6
func()  # prints 5


# keyword arguments
def myfunc(action, camera = "yes", set = "first"):
    print(set, camera, "aaaand", action)

myfunc(3, camera = "never", set = "second")
myfunc(1, set = "third")


#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#    -----------    ----------     ----------
#    |                   |                   |
#    |                 Positional or keyword |
#    |                                       - Keyword only
#    -- Positional only

def combined_example(pos_only, /, standard, *, kwd_only):
    pass

combined_example(1,2,kwd_only=10)

# argument list
args = [2, 5, 1]
print(list(range(*args)))   # same as print(list(range(2,5,1)))


# lambda functions
def increment(a):
    return lambda z: z+a


z = increment(33)
print(z(1))      # 34
print(z(10))     # 43
print(z(z(10)))  # 76 (because z(10) = 33 + 10 = 43 and z(z(10)) = 33 + z(10) = 33 + 43 = 76


# documentation
def empty_func():
    """This function literaly does nothing
    it even return 'None' you silly
    """
    pass

print(empty_func.__doc__)

# annotations

def anno_func(ham: str, eggs: str = 'eggies' ) -> str:
    print("Here is annotations for this function: ", anno_func.__annotations__)
    return ham + " " + eggs

print(anno_func("cheeese"))