from flask import Blueprint, render_template
from queries.deleteQuery import *
from queries.updateQuery import *
from queries.getQuery import *
from queries.postQuery import *
from utils.auth import login_required, authorize
from utils.error_handler import *


developer = Blueprint("developer", __name__, static_folder='static', template_folder='templates/developer')

@developer.route('/')
@login_required
@authorize(my_roles=['Developer'])
@try_except
def home_view():
    # Developers.delete()
    # Developers.post()
    # Developers.get()
    # Developers.update()
    return render_template('developer/index.html')