from flask import Blueprint, render_template
from queries.deleteQuery import *
from queries.updateQuery import *
from queries.getQuery import *
from queries.postQuery import *

writer = Blueprint("writer", __name__, static_folder='static', template_folder='templates/writer')

@writer.route('/')
def home_view():
    # Writers.get()
    # Writers.update()
    # Writers.delete()
    # Writers.post()
    return render_template('writer/index.html')