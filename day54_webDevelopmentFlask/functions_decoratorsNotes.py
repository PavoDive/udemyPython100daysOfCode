import time

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 / n2


# Functions are first-class objects which can be passed around as arguments:

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


print(calculate(add, 2, 3))
print(calculate(subtract, 2, 3))

# Functions can be nested:

def outer_function():
    print("I'm outer")

    def inner_function():
        print("I'm inner")

    inner_function()

    
outer_function()

# Functions can be returned from other functions:

def external_function():
    print("I'm external")

    def internal_function():
        print("I'm internal")

    return internal_function


int_func = external_function() # this should only print external
print("----- separator line to make it evident -----")
int_func()

#--------- DECORATORS ----------

#imagine I want to add a delay of two seconds to SEVERAL functions. One way would be to add time.sleep(2) inside each one of them. The other one is using a decorator:

def delay_decorator(function):
    def wrapper_function():
        # do something before
        time.sleep(2)
        function()
        # do something after
        print(f"function name is: {function}")
    return wrapper_function

# by adding the following line in front of the function definition, the decorator "is applied" to the function:

@delay_decorator
def say_hello():
    print("hello")

@delay_decorator
def say_bye():
    print("say bye")


say_hello()

say_bye()
