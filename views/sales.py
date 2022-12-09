from flask import Blueprint, render_template, request
from queries.deleteQuery import SaleQueryDelete
from queries.updateQuery import SaleQueryUpdate
from queries.getQuery import SaleQueryGet
from queries.postQuery import SaleQueryPost
from utils.auth import *
from utils.error_handler import *
from utils.google_drive import *


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

    return jsonify(emp_infor=emp_infor)



@sale.route('/create-order', methods=['GET', 'POST'])
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
        
        fileName = []
        doctype = []
        saveDir = []

        userId = request.headers['emp_id']

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
                            
        resp = SaleQueryPost.create_orders(request.form, saveDir, doctype, directory, fileName, userId)
            
            # fileUpload(fileName, orderId, directory)

        return jsonify({"message": resp})

    else:
        # if request.args.get('message'):
        #     message = request.args.get('message')
        # else:
        #     message = ""

        saleAgent = SaleQueryGet.get_sale_agent()
        productionPerson = SaleQueryGet.get_production()
        service = SaleQueryGet.get_service()
        product = SaleQueryGet.get_product()

        return jsonify({"sale":saleAgent, "production":productionPerson, "service":service, "product":product, "orderId":orderId})




@sale.route('/all-order', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def get_all_order():
    limit = int(request.args.get('rangeEnd'))
    offset = int(request.args.get('rangeStart'))
    data = SaleQueryGet.get_all_order(limit, offset)
    return jsonify(data = data)



@sale.route('/get-order/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def get_orders(id):
    data = SaleQueryGet.get_order(id)
    # chat_data = SaleQueryGet.get_order_chat(id)

    if data[0]['drive_folder_id']:
        googlefile = fileGet(data[0]['drive_folder_id'])
        return jsonify(data = data[0], googlFiles = googlefile)
    else:
        return jsonify(data = data[0])



@sale.route('/get-order-chat/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def get_orders_chat(id):

    offset = request.args.get('offset')
    chat_data = SaleQueryGet.get_order_chat(id, offset)

    return jsonify(chat_data = chat_data)



@sale.route('/edit-order/<id>', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def edit_order(id):
    if request.method == 'PUT':
        
        fileName = []
        doctype = []
        saveDir = []

        userId = request.headers['emp_id']

        uploaded_files = request.files.getlist("files[]")
        if uploaded_files:

            directory = f'static/Files/ORDER# {id}'
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            for file in uploaded_files:
                if file.filename:    
                    fileName.append(file.filename)
                    file.save(os.path.join(directory, file.filename))
                    doctype.append(file.filename.split('.')[-1])
                    saveDir.append(f'{directory}/{file.filename}')
                            
        resp = SaleQueryUpdate.edit_order(request.form, saveDir, doctype, directory, fileName, id)


        return jsonify({"message": resp})