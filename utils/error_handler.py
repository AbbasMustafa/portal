from functools import wraps
from config import *

def try_except(my_func):
    @wraps(my_func)
    def wrapper(**kwargs):
        try:
            return my_func(**kwargs)
        except Exception as e:
            # return str(e)
            raise
    return wrapper




