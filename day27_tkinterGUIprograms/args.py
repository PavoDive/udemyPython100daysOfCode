# use of *args to take in an unlimited number of arguments:
# the function
def add(n1, n2):
    return n1 + n2
# can only take 2 arguments. But the function
def add2(*args):
    val = 0
    for i in args:
        val += i
    return val
# can take an infinite number of arguments
# the value at *args is replaced by a **tuple**, so it could be
# accessed by indexes:
def test(*args):
    print(args[0])
    # any other actions

test(1, 3, 5, "hello")

# --------------------- *kwargs -----------------------
# keyword arguments: **kwargs inputs to the function a dictionary
# of keyword:values. For example:
def whatever(**kwargs): # notice the double *
    print(kwargs)
    print(type(kwargs))

whatever(add = 3, multiply = 4, divide = 2)

# example of use of **kwargs in class definition:

class Car:
    def __init__(self, **kw):
        self.make = kw["make"] # this will fail if not provided
        self.model = kw["model"]

car = Car(make = "nissan", model = "sentra") # doesn't fail
car_2 = Car(make = "toyota") # fails because didn't find model
# to avoid the previous failure the method get() is used:
class Car2:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

car_ = Car2(make = "nissan", model = "sentra")
car_2 = Car2(make = "toyota") # doesn't fail
        

