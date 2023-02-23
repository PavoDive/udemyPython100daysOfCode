# it is possible to have functions with arguments decorated. To do it, use *args:

def decorator(function):
    def wrapper(*args):
        return f"Half is {args[0]/2}, input was {args[0]} and double is {args[0] * 2}."
    return wrapper

@decorator
def get_number(number):
    return number

get_number(3)

# it is also possible to use **kwargs:
# this doesn't work:
# def decorator_2(function):
#     def wrapper(**kwargs):
#         print(kwargs)
#         # return f"input was {kwargs}, base is {kwargs['base']} and exponent is {kwargs['exponent']}."
#     return wrapper


# @decorator_2
# def get_power(base, exponent):
#     return base**exponent

# get_number(base = 2, exponent = 3)


def decorator_2(function):
    def wrapper2(**kwargs):
        return f"{kwargs['base']} to the power of {kwargs['exponent']} is {function(**kwargs)}."
    return wrapper2


@decorator_2
def get_power(base, exponent):
    return base**exponent

get_power(base = 2, exponent = 3)
