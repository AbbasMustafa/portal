from flask import Blueprint, render_template, url_for, redirect, request
from queries.deleteQuery import HrQueryDelete
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
   
    return render_template('hr/index.html')


@hr.route('/create-user', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Human Resource'])
@try_except
def create_user_view():
    if request.method == 'POST':
        if len(request.form) == 17:
            HrQueryPost.create_users(request.form)
        else: 
            return render_template('hr/createUser.html', department=resp_department, manager=resp_manager, 
            role=resp_Role, error_msg = 'fill all field')   
        
        return redirect(url_for('hr.create_user_view'))
    
    else:
        resp_department = HrQueryGet.get_Department()
        resp_manager = HrQueryGet.get_Manager()
        resp_Role = HrQueryGet.get_Role()
    return render_template('hr/createUser.html', department=resp_department, manager=resp_manager, role=resp_Role)



@hr.route('/list-user', methods=['GET', 'POST'])
@login_required
@authorize(my_roles=['Human Resource'])
@try_except
def list_user_view():

    resp_all_user = HrQueryGet.get_all_user()

    return render_template('hr/all-user.html', users = resp_all_user)



@hr.route('/edit-user/<id>', methods=['GET', 'POST'])
@login_required_with_param
@authorize_with_param(my_roles=['Human Resource'])
@try_except_with_param
def edit_user_view(id):
    if request.method == 'POST':
        if len(request.form) == 15:
            HrQueryUpdate.edit_user(request.form, id)
        else:
            return render_template('hr/profile-edit.html', resp_user_detail = user_details, dept=resp_department, manager=resp_manager, role=resp_Role, error_msg = 'fill all field' )
        

    user_details= HrQueryGet.edit_user_get(id)
    resp_department = HrQueryGet.get_Department()
    resp_manager = HrQueryGet.get_Manager()
    resp_Role = HrQueryGet.get_Role()
    return render_template('hr/profile-edit.html', resp_user_detail = user_details, dept=resp_department, manager=resp_manager, role=resp_Role)