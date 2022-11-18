from flask import Blueprint, jsonify, redirect, url_for, render_template, request, json
import requests
from queries.getQuery import AdminQueryGet
from queries.deleteQuery import AdminQueryDelete
from queries.updateQuery import AdminQueryUpdate
from queries.postQuery import AdminQueryPost
from utils.auth import authorize_with_param, login_required, authorize, login_required_with_param
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
        if len(request.form) == 17 or len(request.form) == 18:
            message = AdminQueryPost.create_users(request.form)
        else: 
            return render_template('superAdmin/createUser.html', department=resp_department, manager=resp_manager, 
            role=resp_Role, error_msg = 'fill all field')   
        
        return redirect(url_for('superAdmin.create_user_view', message = message))
    
    else:

        if request.args.get('message'):
            message = request.args.get('message')
        else:
            message = ""

        resp_department = AdminQueryGet.get_Department()
        resp_manager = AdminQueryGet.get_Manager()
        resp_Role = AdminQueryGet.get_Role()
    return render_template('superAdmin/createUser.html', department=resp_department, manager=resp_manager, role=resp_Role, message=message)



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
        return render_template('superAdmin/all-user.html', users = resp_all_user)



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
@login_required_with_param
@authorize_with_param(my_roles=['Administration'])
@try_except_with_param
def edit_user_view(id):
    if request.method == 'POST':
        if len(request.form) == 15 or len(request.form) == 16:
            AdminQueryUpdate.edit_user(request.form, id)
        else:
            return render_template('superAdmin/profile-edit.html', resp_user_detail = user_details, dept=resp_department, manager=resp_manager, role=resp_Role, error_msg = 'fill all field' )
        

    user_details= AdminQueryGet.edit_user_get(id)
    resp_department = AdminQueryGet.get_Department()
    resp_manager = AdminQueryGet.get_Manager()
    resp_Role = AdminQueryGet.get_Role()
    resp_isAdmin = AdminQueryGet.is_manager(id)
    return render_template('superAdmin/profile-edit.html', resp_user_detail = user_details, dept=resp_department, manager=resp_manager, role=resp_Role, isAdmin=resp_isAdmin)



@superAdmin.route('/employee-info/<id>', methods=['GET', 'POST'])
@login_required_with_param
@authorize_with_param(my_roles=['Administration'])
@try_except_with_param
def employee_info_view(id):

    emp_infor = AdminQueryGet.empInfo(id)

    return render_template('superAdmin/emp-info.html', emp_infor=emp_infor)



@superAdmin.route('/user-status', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def user_status_view():
    userStatus = request.args.get('status')
    filter_users = AdminQueryGet.user_status(userStatus)
    return render_template('superAdmin/all-user.html', users = filter_users)



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
            
            
    
            resp = AdminQueryPost.create_orders(request.form, saveDir, doctype, directory, fileName)
            
            # fileUpload(fileName, orderId, directory)


        return redirect(url_for('superAdmin.order_create_view', message = resp))

    else:
        if request.args.get('message'):
            message = request.args.get('message')
        else:
            message = ""

        saleAgent = AdminQueryGet.get_sale_agent()
        productionPerson = AdminQueryGet.get_production()
        service = AdminQueryGet.get_service()
        product = AdminQueryGet.get_product()

        return render_template('superAdmin/add-new-order.html', sale=saleAgent, production=productionPerson, service=service, product=product, orderId=orderId, message=message)


@superAdmin.route('/all-order', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def get_all_order():
    data = AdminQueryGet.get_order()
    docs = get_docs()
    print(docs)
    return jsonify(data = data)




# @superAdmin.route('/json-test', methods=['GET', 'POST'])
# def json_test():
    # resp = AdminQueryGet.test_data()
    # res = requests.get(f"https://www.googleapis.com/drive/v2/files?q='1mWLRE14TeJXtJWUyYcBo27aMi84fjCM7'+in+parents&key=AIzaSyBnRf27nUBXxCXlT0fku7r56KlZ3nkf4WE")
    # print("res ========= ",res )
    
    # return str(res)


# @superAdmin.route('/add-department', methods=['GET', 'POST'])
# @login_required
# @authorize(my_roles=['Administration'])
# @try_except
# def add_depart_view():
#     if request.method == 'POST':
#         depart = request.get_json()['depart']
#         message = AdminQueryPost.add_department(depart)
#         return jsonify(message=message)