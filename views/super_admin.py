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



@superAdmin.route('/delete-user', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def delete_user_view():
    if request.method =='POST':

        id = request.get_json()['userId']
        active = request.get_json()['active']
        body = AdminQueryDelete.delete_user(id, active)

        return jsonify(body=body)




@superAdmin.route('/edit-user/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def edit_user_view(id):
    if request.method == 'POST':
        
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


@superAdmin.route('/order', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def orders():
    return render_template('superAdmin/all-order.html')



@superAdmin.route('/all-order', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def get_all_order():
    limit = int(request.args.get('rangeEnd'))
    offset = int(request.args.get('rangeStart'))
    data = AdminQueryGet.get_all_order(limit, offset)
    return jsonify(data = data)


@superAdmin.route('/get-order/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def get_orders(id):
    data = AdminQueryGet.get_order(id)
    chat_data = AdminQueryGet.get_order_chat(id)

    if data[0]['drive_folder_id']:
        googlefile = fileGet(data[0]['drive_folder_id'])
        return jsonify(data = data[0], googlFiles = googlefile, chat_data=chat_data)
    else:
        return jsonify(data = data[0], chat_data=chat_data)



@superAdmin.route('/edit-order/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def edit_order(id):
    if request.method == 'POST':
        
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




# @superAdmin.route('/add-department', methods=['GET', 'POST'])
# @login_required
# @authorize(my_roles=['Administration'])
# @try_except
# def add_depart_view():
#     if request.method == 'POST':
#         depart = request.get_json()['depart']
#         message = AdminQueryPost.add_department(depart)
#         return jsonify(message=message)