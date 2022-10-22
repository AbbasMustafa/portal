from flask import Blueprint, render_template
from queries.deleteQuery import ProductionQueryDelete
from queries.updateQuery import ProductionQueryUpdate
from queries.getQuery import ProductionQueryGet
from queries.postQuery import ProductionQueryPost
from utils.auth import login_required, authorize
from utils.error_handler import *


production = Blueprint("production", __name__, static_folder='static', template_folder='templates/developer')

@production.route('/')
@login_required
@authorize(my_roles=['Production'])
@try_except
def home_view():
    ProductionQueryDelete.delete()
    ProductionQueryPost.post()
    ProductionQueryGet.get()
    ProductionQueryUpdate.update()
    return render_template('production/index.html')