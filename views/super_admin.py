from flask import Blueprint, jsonify, redirect, url_for, render_template, request, json
from queries.getQuery import AdminQueryGet
from queries.deleteQuery import AdminQueryDelete
from queries.updateQuery import AdminQueryUpdate
from queries.postQuery import AdminQueryPost
from utils.auth import authorize_with_param, login_required, authorize, login_required_with_param
from utils.error_handler import *

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
        if len(request.form) == 17:
            AdminQueryPost.create_users(request.form)
        else: 
            return render_template('superAdmin/createUser.html', department=resp_department, manager=resp_manager, 
            role=resp_Role, error_msg = 'fill all field')   
        
        return redirect(url_for('superAdmin.create_user_view'))
    
    else:
        resp_department = AdminQueryGet.get_Department()
        resp_manager = AdminQueryGet.get_Manager()
        resp_Role = AdminQueryGet.get_Role()
    return render_template('superAdmin/createUser.html', department=resp_department, manager=resp_manager, role=resp_Role)



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
        if len(request.form) == 15:
            AdminQueryUpdate.edit_user(request.form, id)
        else:
            return render_template('superAdmin/profile-edit.html', resp_user_detail = user_details, dept=resp_department, manager=resp_manager, role=resp_Role, error_msg = 'fill all field' )
        

    user_details= AdminQueryGet.edit_user_get(id)
    resp_department = AdminQueryGet.get_Department()
    resp_manager = AdminQueryGet.get_Manager()
    resp_Role = AdminQueryGet.get_Role()
    return render_template('superAdmin/profile-edit.html', resp_user_detail = user_details, dept=resp_department, manager=resp_manager, role=resp_Role)



@superAdmin.route('/employee-info/<id>', methods=['GET', 'POST'])
@login_required_with_param
@authorize_with_param(my_roles=['Administration'])
@try_except_with_param
def employee_info_view(id):

    emp_infor = AdminQueryGet.empInfo(id)

    return render_template('superAdmin/emp-info.html', emp_infor=emp_infor)