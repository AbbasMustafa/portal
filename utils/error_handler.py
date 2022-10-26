from functools import wraps
from config import *

def try_except(my_func):
    @wraps(my_func)
    def wrapper():
        try:
            return my_func()
        except Exception as e:
            # return str(e)
            raise
    return wrapper



def try_except_with_param(my_func):
    @wraps(my_func)
    def wrapper(id):
        try:
            return my_func(id)
        except Exception as e:
            # return str(e)
            raise
    return wrapper

