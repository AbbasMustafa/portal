from config import *
from flask import redirect, url_for, session
from utils.error_handler import *

@try_except
def route_to():
    if 'user_role' in session:
        
        if session['allowed'] == 'Administration':
            return redirect(url_for('superAdmin.home_view'))
        
        elif session['allowed'] == 'Human Resource':
            return redirect(url_for('hr.home_view'))
        
        elif session['allowed'] == 'Sales':
            return redirect(url_for('sale.home_view'))
        
        elif session['allowed'] == 'Production':
            return redirect(url_for('production.home_view'))

    
    else:
        return 'Login First'