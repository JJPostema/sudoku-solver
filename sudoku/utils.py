# Sudoku solver v0.1.0
# Written by J.J. Postema

import ast
import time
from functools import wraps

def pull(name, filename = "puzzles/9x9.txt"):
    with open(filename) as f:
        puzzles = ast.literal_eval(f.read())
    return puzzles[name]

def timer(enabled = True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not enabled:
                return func(*args, **kwargs)

            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()

            print(f"{func.__name__} took {end-start:.2f} seconds")
            return result

        return wrapper
    return decorator