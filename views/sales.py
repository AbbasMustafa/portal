from flask import Blueprint, render_template, request
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
@login_required
@authorize(my_roles=['Sales'])
@try_except
def employee_info_view(id):

    emp_infor = SaleQueryGet.empInfo(id)

    return render_template('sale/emp-info.html', emp_infor=emp_infor)



@sale.route('/create-order')
@login_required
@authorize(my_roles=['Sales'])
@try_except
def order_create_view():

    orderId = SaleQueryGet.getOrderId()
    if not orderId:
        orderId = 1
    else:
        orderId = orderId[0]['order_id'] + 1
    
    
    if request.method == 'POST':
        
        fileName =[]
        doctype = []
        saveDir = []

        uploaded_files = request.files.getlist("files[]")
        if uploaded_files:

            directory = f'static/Files/ORDER# {orderId}'
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            for file in uploaded_files:
                if file.filename:    
                    fileName.append(file.filename)
                    file.save(os.path.join(directory, file.filename))
                    doctype.append(file.filename.split('.')[-1])
                    saveDir.append(f'{directory}/{file.filename}')
            
            
    
            resp = SaleQueryPost.create_orders(request.form, saveDir, doctype, directory, fileName)
            
            # fileUpload(fileName, orderId, directory)


        return redirect(url_for('sale.order_create_view', message = resp))

    else:
        if request.args.get('message'):
            message = request.args.get('message')
        else:
            message = ""

        saleAgent = SaleQueryGet.get_sale_agent()
        productionPerson = SaleQueryGet.get_production()
        service = SaleQueryGet.get_service()
        product = SaleQueryGet.get_product()

        return render_template('sale/add-new-order.html', sale=saleAgent, production=productionPerson, service=service, product=product, orderId=orderId, message=message)


