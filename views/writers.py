from flask import Blueprint, render_template
from queries.deleteQuery import *
from queries.updateQuery import *
from queries.getQuery import *
from queries.postQuery import *
from utils.auth import login_required, authorize
from utils.error_handler import *


writer = Blueprint("writer", __name__, static_folder='static', template_folder='templates/writer')

@writer.route('/')
@login_required
@authorize(my_roles=['Writer'])
@try_except
def home_view():
    # Writers.get()
    # Writers.update()
    # Writers.delete()
    # Writers.post()
    return render_template('writer/index.html')