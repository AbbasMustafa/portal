from flask import Blueprint, render_template
from queries.deleteQuery import SaleQueryDelete
from queries.updateQuery import SaleQueryUpdate
from queries.getQuery import SaleQueryGet
from queries.postQuery import SaleQueryPost
from utils.auth import *
from utils.error_handler import *


sale = Blueprint("sale", __name__, static_folder='static', template_folder='templates/sale')

@sale.route('/')
@login_required
@authorize(my_roles=['Sales'])
@try_except
def home_view():

    return render_template('sale/index.html')


@sale.route('/employee-info/<id>', methods=['GET', 'POST'])
@login_required_with_param
@authorize_with_param(my_roles=['Sales'])
@try_except_with_param
def employee_info_view(id):

    emp_infor = SaleQueryGet.empInfo(id)

    return render_template('sale/emp-info.html', emp_infor=emp_infor)


@sale.route('/create-order')
@login_required
@authorize(my_roles=['Sales'])
@try_except
def order_create_view():

    saleAgent = SaleQueryGet.get_sale_agent()
    productionPerson = SaleQueryGet.get_production()
    return render_template('sale/add-new-order.html', sale=saleAgent, production=productionPerson)