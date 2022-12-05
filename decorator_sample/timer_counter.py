from time import perf_counter
from functools import wraps


def timer_counter(fun):
    @wraps(fun)
    def inner(*args, **kwargs):
        start_time = perf_counter()
        value = fun(*args, **kwargs)
        end_time = perf_counter()
        print(f"function : {fun.__name__}\t time of running :{end_time - start_time} ")
        return value

    return inner


@timer_counter
def factorial(x):
    sum = 1
    for i in range(x):
        sum += i * (i + 1)
    return sum


print(factorial(200000000))
