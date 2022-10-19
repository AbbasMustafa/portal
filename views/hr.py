from flask import Blueprint, render_template
from queries.deleteQuery import *
from queries.updateQuery import *
from queries.getQuery import *
from queries.postQuery import *

hr = Blueprint("hr", __name__, static_folder='static', template_folder='templates/hr')

@hr.route('/')
def home_view():
    # hr.delete()
    # hr.post()
    # hr.get()
    # hr.update()
    return render_template('hr/index.html')