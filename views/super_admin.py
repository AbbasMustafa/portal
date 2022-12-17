from flask import Blueprint, jsonify, redirect, url_for, render_template, request, json
import requests
from queries.getQuery import AdminQueryGet
from queries.deleteQuery import AdminQueryDelete
from queries.updateQuery import AdminQueryUpdate
from queries.postQuery import AdminQueryPost
from utils.auth import *
from utils.error_handler import *
from utils.google_drive import *


superAdmin = Blueprint("superAdmin", __name__, static_folder='static', template_folder='templates/superAdmin')

@superAdmin.route('/')
@login_required
@authorize(my_roles=['Administration'])
@try_except
def home_view():
    
    return render_template('superAdmin/index.html')



@superAdmin.route('/create-user', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def create_user_view():
    if request.method == 'POST':
        message = AdminQueryPost.create_users(request.get_json())
        return jsonify({'message':message})
      
    
    else:

        resp_department = AdminQueryGet.get_Department()
        resp_manager = AdminQueryGet.get_Manager()
        resp_Role = AdminQueryGet.get_Role()
        return jsonify({'department':resp_department, 'manager':resp_manager, 'role':resp_Role})



@superAdmin.route('/list-user', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def list_user_view():
    if request.method =='POST':

        id = request.get_json()['userId']
        body = AdminQueryGet.password_request(id)

        return jsonify(body=body[0])
        

    else:
        resp_all_user = AdminQueryGet.get_all_user()
        return jsonify( users = resp_all_user)



@superAdmin.route('/delete-user', methods=['GET', 'POST', 'DELETE'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def delete_user_view():
    if request.method =='DELETE':

        id = request.get_json()['userId']
        active = request.get_json()['active']
        message = AdminQueryDelete.delete_user(id, active)

        return jsonify({"message":message})




@superAdmin.route('/edit-user/<id>', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def edit_user_view(id):
    if request.method == 'PUT':
        
        message = AdminQueryUpdate.edit_user(request.get_json(), id)
        return jsonify({'message': message})
    
    else:
        user_details= AdminQueryGet.edit_user_get(id)
        resp_department = AdminQueryGet.get_Department()
        resp_manager = AdminQueryGet.get_Manager()
        resp_Role = AdminQueryGet.get_Role()
        resp_isManager = AdminQueryGet.is_manager(id)
        return jsonify ({'resp_user_detail': user_details, 'dept':resp_department, 'manager':resp_manager, 'role':resp_Role, 
            'isManager':resp_isManager})



@superAdmin.route('/employee-info/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def employee_info_view(id):

    emp_infor = AdminQueryGet.empInfo(id)

    return jsonify(emp_infor=emp_infor)



@superAdmin.route('/user-status', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def user_status_view():
    userStatus = request.args.get('status')
    filter_users = AdminQueryGet.user_status(userStatus)
    return jsonify(users = filter_users)



@superAdmin.route('/create-order', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def order_create_view():

    orderId = AdminQueryGet.getOrderId()
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
                            
        resp = AdminQueryPost.create_orders(request.form, saveDir, doctype, directory, fileName, userId)
            
            # fileUpload(fileName, orderId, directory)

        return jsonify({"message": resp})

    else:
        # if request.args.get('message'):
        #     message = request.args.get('message')
        # else:
        #     message = ""

        saleAgent = AdminQueryGet.get_sale_agent()
        productionPerson = AdminQueryGet.get_production()
        service = AdminQueryGet.get_service()
        product = AdminQueryGet.get_product()

        return jsonify({"sale":saleAgent, "production":productionPerson, "service":service, "product":product, "orderId":orderId})




@superAdmin.route('/all-order', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def get_all_order():
    limit = int(request.args.get('rangeEnd'))
    offset = int(request.args.get('rangeStart'))
    emp_id = request.args.get('empId')
    status = request.args.get('status')
    
    data = AdminQueryGet.get_all_order(limit, offset, emp_id, status)
    return jsonify(data = data)



@superAdmin.route('/get-order/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def get_orders(id):

    empId = request.headers['emp_id']

    info = AdminQueryGet.get_emp_in_order(empId, id)

    if not info:
        return jsonify({"message": "you have no access to order"})

    else:
        data = AdminQueryGet.get_order(id)
        doc_data = AdminQueryGet.get_order_doc(id)

        if doc_data:
            googlefile = fileGet(doc_data[0]['drive_folder_id'])
            return jsonify(data = data[0], googlFiles = googlefile, doc_data=doc_data[0])
        else:
            return jsonify(data = data[0])



@superAdmin.route('/get-order-chat/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def get_orders_chat(id):

    offset = request.args.get('offset')
    chat_data = AdminQueryGet.get_order_chat(id, offset)

    return jsonify(chat_data = chat_data)



@superAdmin.route('/edit-order/<id>', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Administration'])
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
                            
        resp = AdminQueryUpdate.edit_order(request.form, saveDir, doctype, directory, fileName, id)


        return jsonify({"message": resp})



@superAdmin.route('/update-file', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Administration'])
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

        message = AdminQueryUpdate.update_file(saveDir, doctype, directory, fileName, orderId, folder_id)

        return jsonify({"message":message})



@superAdmin.route('/order-recipients/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def order_recipients(id):

    recipients = AdminQueryGet.get_recipients(id)
    remove_recipients = AdminQueryGet.get_remove_recipient(id)

    return jsonify(recipients=recipients, remove_recipients=remove_recipients)



@superAdmin.route('/order-add-user', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def order_add_users():
    if request.method == 'PUT':
        
        message = AdminQueryUpdate.add_recipients(request.get_json())
        
        return jsonify({"message":message})
        



@superAdmin.route('/order-delete-user', methods=['GET', 'POST', 'DELETE'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def delete_recipient():
    if request.method == 'DELETE':
        
        message = AdminQueryDelete.delete_order_recipients(request.get_json())

    return jsonify({"message":message})



@superAdmin.route('/change-order-status', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def change_order_status():

    if request.method == 'PUT':

        message = AdminQueryUpdate.update_order_status(request.get_json())

        return jsonify({"message":message})



@superAdmin.route('/order-stats', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def get_order_stats():

    id = request.args.get('empId')
    message = AdminQueryGet.order_stats(id)

    return jsonify({"completed":message[0][0]['COUNT(order_id)'], "cancelled":message[1][0]['COUNT(order_id)'], 
    "revision":message[2][0]['COUNT(order_id)'], "hold":message[3][0]['COUNT(order_id)'], 
    "progress":message[4][0]['COUNT(order_id)'], "total":message[5][0]['COUNT(order_id)'],
    "developer-monthly":message[6][0]['COUNT(order_id)'], "writer-monthly":message[7][0]['COUNT(order_id)'],
    "developer-weekly":message[8][0]['COUNT(order_id)'], "writer-weekly":message[9][0]['COUNT(order_id)'],
    "developer-daily":message[10][0]['COUNT(order_id)'],"writer-daily":message[11][0]['COUNT(order_id)']})



@superAdmin.route('/get-single-chat', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def get_single_chat_data():

    roomId = request.args.get('roomId')
    offset = request.args.get('offset')
    # print(roomId, offset)
    chat_data = AdminQueryGet.single_chat(roomId, offset)

    return jsonify(chat_data = chat_data)



@superAdmin.route('/single-chat', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def create_chat():
    if request.method == 'POST':
        users = request.get_json()['userId']
        empId = request.get_json()['empId']
        
        message = AdminQueryPost.create_single_chat(users, empId)

        return jsonify({"message":message})



@superAdmin.route('/get-all-chat/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def get_all_chat(id):

    data = AdminQueryGet.all_chat_get(id)
    globalChat = AdminQueryGet.global_chat_get(id)

    return jsonify({"data":data, "global":globalChat})



@superAdmin.route('/annoucement-recipient/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def annoucment_recipients(id):

    recipients = AdminQueryGet.get_recipients_global(id)
    remove_recipients = AdminQueryGet.get_remove_recipient_global(id)

    return jsonify(recipients=recipients, remove_recipients=remove_recipients)



@superAdmin.route('/global-user', methods=['GET', 'PUT', 'DELETE'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def global_users():
    if request.method == 'PUT':
        
        message = AdminQueryUpdate.add_recipients_global(request.get_json())
        
        return jsonify({"message":message})


    if request.method == 'DELETE':

        message = AdminQueryDelete.delete_recipients_global(request.get_json())
        
        return jsonify({"message":message})





# @superAdmin.route('/add-department', methods=['GET', 'POST'])
# @login_required
# @authorize(my_roles=['Administration'])
# @try_except
# def add_depart_view():
#     if request.method == 'POST':
#         depart = request.get_json()['depart']
#         message = AdminQueryPost.add_department(depart)
#         return jsonify(message=message)