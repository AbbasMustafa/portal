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
    emp_id = request.args.get('empId')
    status = request.args.get('status')

    data = SaleQueryGet.get_all_order(limit, offset, emp_id, status)
    return jsonify(data = data)



@sale.route('/get-order/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def get_orders(id):
    
    empId = request.headers['emp_id']

    info = SaleQueryGet.get_emp_in_order(empId, id)

    if not info:

        return jsonify({"message": "you have no access to order"})

    else:
        data = SaleQueryGet.get_order(id)
        doc_data = SaleQueryGet.get_order_doc(id)

        if doc_data:
            googlefile = fileGet(doc_data[0]['drive_folder_id'])
            return jsonify(data = data[0], googlFiles = googlefile, doc_data=doc_data[0])
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



@sale.route('/update-file', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def add_file():

    if request.method == 'PUT':

        fileName = []
        doctype = []
        saveDir = []

        orderId = request.form['orderId']
        folder_id = request.form['folder_id']
       

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

        message = SaleQueryUpdate.update_file(saveDir, doctype, directory, fileName, orderId, folder_id)

        return jsonify({"message":message})



@sale.route('/order-recipients/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def order_recipients(id):

    recipients = SaleQueryGet.get_recipients(id)
    remove_recipients = SaleQueryGet.get_remove_recipient(id)

    return jsonify(recipients=recipients, remove_recipients=remove_recipients)



@sale.route('/order-add-user', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def order_add_users():
    if request.method == 'PUT':

        message = SaleQueryUpdate.add_recipients(request.get_json())
        
        return jsonify({"message":message})
        



@sale.route('/order-delete-user', methods=['GET', 'POST', 'DELETE'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def delete_recipient():
    if request.method == 'DELETE':
        
        message = SaleQueryDelete.delete_order_recipients(request.get_json())

    return jsonify({"message":message})    



@sale.route('/change-order-status', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def change_order_status():

    if request.method == 'PUT':

        # print(request.get_json())
        message = SaleQueryUpdate.update_order_status(request.get_json())

        return jsonify({"message":message})



@sale.route('/order-status', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Sales'])
def order_status():
    
    id = request.args.get('userId')
    status = request.args.get('status')
    limit = int(request.args.get('rangeEnd'))
    offset = int(request.args.get('rangeStart'))

    message = SaleQueryGet.status_order(id, status, limit, offset)

    return jsonify({"message":message})



@sale.route('/get-single-chat', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def get_single_chat_data():

    roomId = request.args.get('roomId')
    offset = request.args.get('offset')
    # print(roomId, offset)
    chat_data = SaleQueryGet.single_chat(roomId, offset)

    return jsonify(chat_data = chat_data)



@sale.route('/get-all-chat/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def get_all_chat(id):

    data = SaleQueryGet.all_chat_get(id)
    globalChat = SaleQueryGet.global_chat_get(id)

    return jsonify({"data":data, "global":globalChat})




@sale.route('/order-stats', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Sales'])
@try_except
def get_order_stats():

    id = request.args.get('empId')
    message = SaleQueryGet.order_stats(id)

    return jsonify({"completed":message[0][0]['COUNT(order_id)'], "cancelled":message[1][0]['COUNT(order_id)'], 
    "revision":message[2][0]['COUNT(order_id)'], "hold":message[3][0]['COUNT(order_id)'], 
    "progress":message[4][0]['COUNT(order_id)'], "total":message[5][0]['COUNT(order_id)'],
    "developer-monthly":message[6][0]['COUNT(order_id)'], "writer-monthly":message[7][0]['COUNT(order_id)'],
    "developer-weekly":message[8][0]['COUNT(order_id)'], "writer-weekly":message[9][0]['COUNT(order_id)'],
    "developer-daily":message[10][0]['COUNT(order_id)'],"writer-daily":message[11][0]['COUNT(order_id)']})