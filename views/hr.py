from flask import Blueprint, render_template, url_for, redirect
from queries.deleteQuery import HrQueryDelete
from queries.updateQuery import HrQueryUpdate
from queries.getQuery import HrQueryGet
from queries.postQuery import HrQueryPost
from utils.auth import login_required, authorize
from utils.error_handler import *


hr = Blueprint("hr", __name__, static_folder='static', template_folder='templates/hr')

@hr.route('/')
@login_required
@authorize(my_roles=['Human Resource'])
@try_except
def home_view():
    HrQueryDelete.delete()
    HrQueryPost.post()
    HrQueryGet.get()
    HrQueryUpdate.update()
    return render_template('hr/index.html')
    # return redirect(url_for('superAdmin.home_view'))