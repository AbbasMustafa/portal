from flask import Blueprint, render_template, request, jsonify
from queries.deleteQuery import ProductionQueryDelete
from queries.updateQuery import ProductionQueryUpdate
from queries.getQuery import ProductionQueryGet
from queries.postQuery import ProductionQueryPost
from utils.auth import login_required, authorize
from utils.error_handler import *


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



@production.route('/get-order-chat/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Production'])
@try_except
def get_orders_chat(id):

    offset = request.args.get('offset')
    chat_data = ProductionQueryGet.get_order_chat(id, offset)

    return jsonify(chat_data = chat_data)