from flask import Blueprint, render_template, url_for, redirect, request, jsonify
from queries.deleteQuery import Hr, HrQueryDelete
from queries.updateQuery import HrQueryUpdate
from queries.getQuery import HrQueryGet
from queries.postQuery import HrQueryPost
from utils.auth import *
from utils.error_handler import *


hr = Blueprint("hr", __name__, static_folder='static', template_folder='templates/hr')

@hr.route('/')
@login_required
@authorize(my_roles=['Human Resource'])
@try_except
def home_view():
    
    activeUser = HrQueryGet.activeUser()
    banUser = HrQueryGet.banUser()
    return jsonify ({'activeUser':activeUser[0]['COUNT(login_email)'], 'banUser':banUser[0]['COUNT(login_email)']})


@hr.route('/create-user', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Human Resource'])
@try_except
def create_user_view():
    if request.method == 'POST':
        message = HrQueryPost.create_users(request.get_json()) 
        return jsonify({'message':message})   
    
    else:
        
        resp_department = HrQueryGet.get_Department()
        resp_manager = HrQueryGet.get_Manager()
        resp_Role = HrQueryGet.get_Role()
        return jsonify({'department':resp_department, 'manager':resp_manager, 'role':resp_Role})



@hr.route('/list-user', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Human Resource'])
@try_except
def list_user_view():

    if request.method =='POST':

        id = request.get_json()['userId']
        body = HrQueryGet.password_request(id)

        return jsonify(body=body[0])

    resp_all_user = HrQueryGet.get_all_user()

    return jsonify(users = resp_all_user)



@hr.route('/edit-user/<id>', methods=['GET', 'POST', 'PUT'])
@login_required
@authorize(my_roles=['Human Resource'])
@try_except
def edit_user_view(id):
    if request.method == 'PUT':
        message = HrQueryUpdate.edit_user(request.get_json(), id)
        return jsonify({'message': message}) 
        
    else:
        user_details= HrQueryGet.edit_user_get(id)
        resp_department = HrQueryGet.get_Department()
        resp_manager = HrQueryGet.get_Manager()
        resp_Role = HrQueryGet.get_Role()
        return jsonify({'resp_user_detail':user_details, 'dept':resp_department, 'manager':resp_manager, 'role':resp_Role})


@hr.route('/delete-user', methods=['GET', 'POST', 'DELETE'])
@login_required
@authorize(my_roles=['Human Resource'])
@try_except
def delete_user_view():
    if request.method =='DELETE':

        id = request.get_json()['userId']
        active = request.get_json()['active']
        body = HrQueryDelete.delete_user(id, active)

        return jsonify(body=body)



@hr.route('/employee-info/<id>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Human Resource'])
@try_except
def employee_info_view(id):

    emp_infor = HrQueryGet.empInfo(id)

    return jsonify(emp_infor=emp_infor)



@hr.route('/user-status', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Human Resource'])
@try_except
def user_status_view():
    userStatus = request.args.get('status')
    filter_users = HrQueryGet.user_status(userStatus)
    return jsonify(users = filter_users)



@hr.route('/get-single-chat/<roomId>', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Human Resource'])
@try_except
def get_single_chat_data(roomId):

    offset = request.args.get('offset')
    chat_data = HrQueryGet.single_chat(roomId, offset)

    return jsonify(chat_data = chat_data)



@hr.route('/single-chat', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Administration'])
@try_except
def create_chat():
    if request.method == 'POST':
        users = request.get_json()['userId']
        empId = request.get_json()['empId']
        
        message = HrQueryPost.create_single_chat(users, empId)

        return jsonify({"message":message})