from functools import wraps
from config import *
from flask import session , render_template, redirect, url_for


def login_required(my_func):
    @wraps(my_func)
    def wrapper():
        if not 'user_role' in session:
            return "Unauthorize Login first"
            # return redirect(url_for('login_view'))
        else: 
            return my_func()

    return wrapper


def authorize(my_roles=[]):
    def decorator(my_func):
        @wraps(my_func)
        def wrapper():
            if session['allowed'] in my_roles:
                return my_func()
            # if my_roles in session['allowed']:
            #     return my_func()
            else:
                return "You are Unauthorize to access this route"

        return wrapper
    return decorator




def login_required_with_param(my_func):
    @wraps(my_func)
    def wrapper(id):
        if not 'user_role' in session:
            return "Unauthorize Login first"
            # return redirect(url_for('login_view'))
        else: 
            return my_func(id)

    return wrapper


def authorize_with_param(my_roles=[]):
    def decorator(my_func):
        @wraps(my_func)
        def wrapper(id):
            if session['allowed'] in my_roles:
                return my_func(id)
            # if my_roles in session['allowed']:
            #     return my_func()
            else:
                return "You are Unauthorize to access this route"

        return wrapper
    return decorator