from flask import Blueprint, render_template
from queries.deleteQuery import DeveloperQueryDelete
from queries.updateQuery import DeveloperQueryUpdate
from queries.getQuery import DeveloperQueryGet
from queries.postQuery import DeveloperQueryPost
from utils.auth import login_required, authorize
from utils.error_handler import *


developer = Blueprint("developer", __name__, static_folder='static', template_folder='templates/developer')

@developer.route('/')
@login_required
@authorize(my_roles=['Developer','Admin'])
@try_except
def home_view():
    DeveloperQueryDelete.delete()
    DeveloperQueryPost.post()
    DeveloperQueryGet.get()
    DeveloperQueryUpdate.update()
    return render_template('developer/index.html')