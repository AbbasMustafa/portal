from flask import Blueprint, render_template
from queries.deleteQuery import SaleQueryDelete
from queries.updateQuery import SaleQueryUpdate
from queries.getQuery import SaleQueryGet
from queries.postQuery import SaleQueryPost
from utils.auth import login_required, authorize
from utils.error_handler import *


sale = Blueprint("sale", __name__, static_folder='static', template_folder='templates/sale')

@sale.route('/')
@login_required
@authorize(my_roles=['Sales'])
@try_except
def home_view():

    return render_template('sale/index.html')


@sale.route('/create-order')
@login_required
@authorize(my_roles=['Sales'])
@try_except
def order_create_view():

    return render_template('sale/add-new-order.html')