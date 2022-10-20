from functools import wraps

def try_except(my_func):
    @wraps(my_func)
    def wrapper():
        try:
            return my_func()
        except Exception as e:
            # return str(e)
            raise
    return wrapper

