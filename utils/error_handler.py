def try_except(my_func):
    def wrap():
        try:
            my_func()
        except Exception as e:
            raise
    return wrap

