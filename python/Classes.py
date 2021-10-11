# local, nonlocal and global

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)      # After local assignment: test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)   # After nonlocal assignment: nonlocal spam
    do_global()
    print("After global assignment:", spam)     # After global assignment: nonlocal spam

scope_test()
print("In global scope:", spam)                 # In global scope: global spam

# basic class
class First:
    """That's one of my first classes"""
    i = 123222          # value shared with all instances
    def __init__(self):
        self.i = 123
    def show(self):
        print("I love you", self.i)

x = First()
x.show()        # I love you 123

# self - don't need to be exact name 'self', but it has to be the first argument
class Class:
    def __init__(AnotherSillyObject, x):
        AnotherSillyObject.x = x

obj = Class(3)

print(obj.x)

# deleting objects
del obj

# inheritance
#if we define method __init__ in this class it will overwrite __init__ from parent's class
#so we can do it in other way
class Second(First):
    def __init__(self):
        #First.__init__(self)    # inherit only __init__
        super().__init__()  # inherit all methods and properties from parent
        self.x = 2021

obj1 = Second()
obj1.show()
print(obj1.x)





