from flask import Blueprint, redirect, url_for, render_template
from queries.getQuery import AdminQueryGet
from queries.deleteQuery import AdminQueryDelete
from queries.updateQuery import AdminQueryUpdate
from queries.postQuery import AdminQueryPost
from utils.auth import login_required, authorize
from utils.error_handler import *

superAdmin = Blueprint("superAdmin", __name__, static_folder='static', template_folder='templates/superAdmin')

@superAdmin.route('/')
@login_required
@authorize(my_roles=['Admin'])
@try_except
def home_view():
    AdminQueryGet.get()
    AdminQueryPost.post()
    AdminQueryDelete.delete()
    AdminQueryUpdate.update()
    return render_template('superAdmin/index.html')

