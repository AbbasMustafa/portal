from flask import Blueprint, render_template
from queries.deleteQuery import WriterQueryDelete
from queries.updateQuery import WriterQueryUpdate
from queries.getQuery import WriterQueryGet
from queries.postQuery import WriterQueryPost
from utils.auth import login_required, authorize
from utils.error_handler import *


writer = Blueprint("writer", __name__, static_folder='static', template_folder='templates/writer')

@writer.route('/')
@login_required
@authorize(my_roles=['Writer','Admin'])
@try_except
def home_view():
    WriterQueryGet.get()
    WriterQueryUpdate.update()
    WriterQueryDelete.delete()
    WriterQueryPost.post()
    return render_template('writer/index.html')