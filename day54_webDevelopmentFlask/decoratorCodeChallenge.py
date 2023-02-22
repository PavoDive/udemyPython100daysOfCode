import time
#current_time = time.time()
#print(current_time)

def speed_calc_decorator(function):
    def time_diference():
        ti = time.time()
        function()
        tf = time.time()
        print(f"{function.__name__} run speed: {tf - ti} seconds.")
    return time_diference

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()

slow_function()
