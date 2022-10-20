from config import *
from flask import redirect, url_for, session
from utils.error_handler import *

@try_except
def route_to():
    if 'user_role' in session:
        
        if session['user_role'] == 'Admin':
            return redirect(url_for('superAdmin.home_view'))
        
        elif session['user_role'] == 'Hr':
            return redirect(url_for('hr.home_view'))
        
        elif session['user_role'] == 'Sale':
            return redirect(url_for('sale.home_view'))
        
        elif session['user_role'] == 'Developer':
            return redirect(url_for('developer.home_view'))

        elif session['user_role'] == 'Writer':
            return redirect(url_for('writer.home_view'))
    
    else:
        return 'Login First'