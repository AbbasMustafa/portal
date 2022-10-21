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
@authorize(my_roles=['Sale','Admin'])
@try_except
def home_view():
    SaleQueryGet.get()
    SaleQueryPost.post()
    SaleQueryUpdate.update()
    SaleQueryDelete.delete()
    return render_template('sale/index.html')