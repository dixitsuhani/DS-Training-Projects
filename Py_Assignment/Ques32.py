# Write a Python decorator to print the execution time of a function.

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Execution time:", time.time() - start)
        return result
    return wrapper
@timer
def example():
    time.sleep(1)
    print("Function finished")
example()