from functools import wraps
from time import perf_counter


def logger(fn):
    @wraps
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        perform = end - start
        print(perform)
        return result
    return wrapper