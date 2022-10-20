from flask import Blueprint, render_template
from queries.deleteQuery import *
from queries.updateQuery import *
from queries.getQuery import *
from queries.postQuery import *
from utils.auth import login_required, authorize
from utils.error_handler import *


hr = Blueprint("hr", __name__, static_folder='static', template_folder='templates/hr')

@hr.route('/')
@login_required
@authorize(my_roles=['Hr'])
@try_except
def home_view():
    # hr.delete()
    # hr.post()
    # hr.get()
    # hr.update()
    return render_template('hr/index.html')