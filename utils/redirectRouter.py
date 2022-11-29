from config import *
from flask import redirect, url_for, session
from utils.error_handler import *

@try_except
def route_to():
    if 'user_role' in session:
        
        if session['allowed'] == 'Administration':
            return 'admin'
        
        elif session['allowed'] == 'Human Resource':
            return 'hr'
        
        elif session['allowed'] == 'Sales':
            return 'sale'
        
        elif session['allowed'] == 'Production':
            return 'production'

    
    else:
        return 'Login First'