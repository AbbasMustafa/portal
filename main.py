from flask import Flask, jsonify, render_template, request, session, url_for, redirect
from config import *
from views.super_admin import superAdmin
from views.hr import hr
from views.sales import sale
from views.production import production
from utils.error_handler import *
from utils.auth import *
from utils.redirectRouter import *
from utils.google_drive import *
from queries.globalQuery import *
from chat.Chats import chat
from flask_socketio import join_room

# app = Flask(__name__)
# baseUrl = "/api"


app.register_blueprint(superAdmin, url_prefix = '/admin')
app.register_blueprint(hr, url_prefix = '/hr')
app.register_blueprint(sale, url_prefix = '/sale')
# app.register_blueprint(writer, url_prefix = '/writer')
app.register_blueprint(production, url_prefix = '/developer')
app.register_blueprint(chat, url_prefix = '/chat')



@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
@try_except
def login_view():
    if 'user_role' in session:
        return route_to()

    else:
        if request.method == "POST":
            user_name = request.form.get('username')
            password = request.form.get('pass')
            return_data = login_query(user_name, password)
            if return_data:
                session['allowed'] = return_data[0]['department_name']
                session['user_role'] = return_data[0]['role_name']
                session['emp_name'] = return_data[0]['employee_name']
                session['designation'] = return_data[0]['designation']
                session['emp_id'] = return_data[0]['employee_id_fk']
                return route_to()
                # session['allowed'] = ['Administration', 'Human Resource', 'Sales']

            else:
                message = 'Wrong Credentials Or You have no acces to portal'
                return render_template('login.html', message=message)     
        else:
            return render_template('login.html')


@try_except
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password_view():
    
    if request.method == 'POST':
        email = request.get_json()['email']
        return_pass = get_password(email)
        if return_pass:
            return jsonify(message=f"Password Sent To {return_pass[0]['login_email']}")

        else:
            return jsonify(message="No Email Found Or Your Are Ban")




@app.route('/logout')
@login_required
@try_except
def logout_view():
    session.clear()
    return redirect(url_for('login_view'))



# ======================================================================================
# @app.route('/google-setups', methods=['GET','POST'])
# def googleDrive():
#     mymain()
#     return "Done"

# @app.route('/google-setup', methods=['GET','POST'])
# def googleDrive1():    
#     return "Done"

# ======================================================================================



if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=5000, debug=True)
    socketio.run(app,host='0.0.0.0',port=5000, debug=True)