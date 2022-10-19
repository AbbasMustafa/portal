from flask import Blueprint, render_template
from queries.deleteQuery import *
from queries.updateQuery import *
from queries.getQuery import *
from queries.postQuery import *

developer = Blueprint("developer", __name__, static_folder='static', template_folder='templates/developer')

@developer.route('/')
def home_view():
    # Developers.delete()
    # Developers.post()
    # Developers.get()
    # Developers.update()
    return render_template('developers/index.html')