from flask import Blueprint, render_template, request, jsonify
from queries.deleteQuery import ProductionQueryDelete
from queries.updateQuery import ProductionQueryUpdate
from queries.getQuery import ProductionQueryGet
from queries.postQuery import ProductionQueryPost
from utils.auth import login_required, authorize
from utils.error_handler import *
from utils.google_drive import *


production = Blueprint("production", __name__, static_folder='static', template_folder='templates/developer')



@production.route('/employee-info/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Production'])
@try_except
def employee_info_view(id):

    emp_infor = ProductionQueryGet.empInfo(id)

    return jsonify(emp_infor=emp_infor)
   



@production.route('/all-order', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Production'])
@try_except
def get_all_order():
    limit = int(request.args.get('rangeEnd'))
    offset = int(request.args.get('rangeStart'))
    emp_id = request.args.get('empId')
    status = request.args.get('status')
    
    data = ProductionQueryGet.get_all_order(limit, offset, emp_id, status)
    return jsonify(data = data)



@production.route('/update-file', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Production'])
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

        message = ProductionQueryUpdate.update_file(saveDir, doctype, directory, fileName, orderId, folder_id)

        return jsonify({"message":message})



@production.route('/order-recipients/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Production'])
@try_except
def order_recipients(id):

    recipients = ProductionQueryGet.get_recipients(id)
    remove_recipients = ProductionQueryGet.get_remove_recipient(id)

    return jsonify(recipients=recipients, remove_recipients=remove_recipients)



@production.route('/order-add-user', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Production'])
@try_except
def order_add_users():
    if request.method == 'PUT':
        
        message = ProductionQueryUpdate.add_recipients(request.get_json())
        
        return jsonify({"message":message})
        



@production.route('/order-delete-user', methods=['GET', 'POST', 'DELETE'])
@login_required
@authorize(my_roles=['Production'])
@try_except
def delete_recipient():
    if request.method == 'DELETE':
        
        message = ProductionQueryDelete.delete_order_recipients(request.get_json())

    return jsonify({"message":message})



@production.route('/order-status', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Production'])
def order_status():
    
    id = request.args.get('userId')
    status = request.args.get('status')
    limit = int(request.args.get('rangeEnd'))
    offset = int(request.args.get('rangeStart'))

    message = ProductionQueryGet.status_order(id, status, limit, offset)

    return jsonify({"message":message})



@production.route('/get-single-chat', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Production'])
@try_except
def get_single_chat_data():

    roomId = request.args.get('roomId')
    offset = request.args.get('offset')
    # print(roomId, offset)
    chat_data = ProductionQueryGet.single_chat(roomId, offset)

    return jsonify(chat_data = chat_data)



@production.route('/get-all-chat/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Production'])
@try_except
def get_all_chat(id):

    data = ProductionQueryGet.all_chat_get(id)
    globalChat = ProductionQueryGet.global_chat_get(id)

    return jsonify({"data":data, "global":globalChat})




@production.route('/order-stats', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Production'])
@try_except
def get_order_stats():

    id = request.args.get('empId')
    message = ProductionQueryGet.order_stats(id)

    return jsonify({"completed":message[0][0]['COUNT(order_id)'], "cancelled":message[1][0]['COUNT(order_id)'], 
    "revision":message[2][0]['COUNT(order_id)'], "hold":message[3][0]['COUNT(order_id)'], 
    "progress":message[4][0]['COUNT(order_id)'], "total":message[5][0]['COUNT(order_id)'],
    "developer-monthly":message[6][0]['COUNT(order_id)'], "writer-monthly":message[7][0]['COUNT(order_id)'],
    "developer-weekly":message[8][0]['COUNT(order_id)'], "writer-weekly":message[9][0]['COUNT(order_id)'],
    "developer-daily":message[10][0]['COUNT(order_id)'],"writer-daily":message[11][0]['COUNT(order_id)']})



@production.route('/get-order/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Production'])
@try_except
def get_orders(id):
    
    empId = request.headers['emp_id']

    info = ProductionQueryGet.get_emp_in_order(empId, id)

    if not info:
 
        return jsonify({"message": "you have no access to order"})

    else:
        data = ProductionQueryGet.get_order(id)
        doc_data = ProductionQueryGet.get_order_doc(id)

        if doc_data:
            googlefile = fileGet(doc_data[0]['drive_folder_id'])
            return jsonify(data = data[0], googlFiles = googlefile, doc_data=doc_data[0])
        else:
            return jsonify(data = data[0])



@production.route('/get-order-chat/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Production'])
@try_except
def get_orders_chat(id):

    offset = request.args.get('offset')
    chat_data = ProductionQueryGet.get_order_chat(id, offset)

    return jsonify(chat_data = chat_data)
