from flask import Blueprint, render_template
from queries.deleteQuery import *
from queries.updateQuery import *
from queries.getQuery import *
from queries.postQuery import *
from utils.auth import login_required, authorize
from utils.error_handler import *


sale = Blueprint("sale", __name__, static_folder='static', template_folder='templates/sale')

@sale.route('/')
@login_required
@authorize(my_roles=['Sale'])
@try_except
def home_view():
    # Sales.get()
    # Sales.post()
    # Sales.update()
    # Sales.delete()
    return render_template('sale/index.html')