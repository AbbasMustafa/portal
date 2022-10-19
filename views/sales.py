from flask import Blueprint, render_template
from queries.deleteQuery import *
from queries.updateQuery import *
from queries.getQuery import *
from queries.postQuery import *

sale = Blueprint("sale", __name__, static_folder='static', template_folder='templates/sale')

@sale.route('/')
def home_view():
    # Sales.get()
    # Sales.post()
    # Sales.update()
    # Sales.delete()
    return render_template('sale/index.html')