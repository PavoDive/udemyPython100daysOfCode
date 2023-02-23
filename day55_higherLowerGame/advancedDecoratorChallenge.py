# from coding rooms

# Create the logging_decorator() function 👇

def a_decorator(function):
    def wrapper(*args):
        z = function(*args)
        print(f"You called {function.__name__}{args}\nIt returned {z}")
    return wrapper


# Use the decorator 👇

@a_decorator
def sum_numbers(*args):
    return sum(args)

sum_numbers(1, 23, 12, 14)
