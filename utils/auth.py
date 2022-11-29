from functools import wraps
from config import *
from flask import session , render_template, redirect, url_for, jsonify, request


def login_required(my_func):
    @wraps(my_func)
    def wrapper(**kwargs):
        if request.headers['user_role'] == "null":
            return jsonify(message = "Unauthorize Login first")
            # return redirect(url_for('login_view'))
        else: 
            return my_func(**kwargs)

    return wrapper


def authorize(my_roles=[]):
    def decorator(my_func):
        @wraps(my_func)
        def wrapper(**kwargs):
            if request.headers['allowed'] in my_roles:
                return my_func(**kwargs)
            # if my_roles in session['allowed']:
            #     return my_func()
            else:
                return jsonify(message="You are Unauthorize to access this route")

        return wrapper
    return decorator
