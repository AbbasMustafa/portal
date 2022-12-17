from flask import Flask, jsonify, request
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
# from flask_socketio import join_room

# app = Flask(__name__)
# baseUrl = "/api"


app.register_blueprint(superAdmin, url_prefix = '/admin')
app.register_blueprint(hr, url_prefix = '/hr')
app.register_blueprint(sale, url_prefix = '/sale')
# app.register_blueprint(writer, url_prefix = '/writer')
app.register_blueprint(production, url_prefix = '/production')
app.register_blueprint(chat, url_prefix = '/chat')



@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
@try_except
def login_view():
    try:
        # if 'user_role' in session:
        #     return route_to()

        # else:
        if request.method == "POST":
            
            user_name = request.get_json()['username']
            password = request.get_json()['pass']

            return_data = login_query(user_name, password)
            if return_data:

                if not return_data[0]['manager_emp_id']:
                    is_manager = 'false'
                else: 
                    is_manager = 'true'
                
                return jsonify(message = 'Login Success' , URL = return_data[0]['department_name'], 
                name=return_data[0]['employee_name'], designation=return_data[0]['designation'], 
                user_role=return_data[0]['role_name'], emp_id = return_data[0]['employee_id_fk'],
                is_manager=is_manager)
                
            else:
                message = 'Wrong Credentials Or You have no acces to portal'
                return jsonify(message=message, URL = '#')

    except Exception as e:
        print(e)
        return jsonify({"message":"Something went wrong while logging in"})    



@try_except
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password_view():
    try:
        if request.method == 'POST':
            email = request.get_json()['email']
            return_pass = get_password(email)
            if return_pass:
                return jsonify(message=f"Password Sent To {return_pass[0]['login_email']}")

            else:
                return jsonify(message="No Email Found Or Your Are Ban")
    
    except Exception as e:
        print(e)
        return jsonify({"message":"Something went wrong while recovering your password"})




@app.route('/logout')
@login_required
@try_except
def logout_view():
    try:
        return jsonify({"message":'Logout successful'})
    except Exception as e:
        print(e)
        return jsonify({"message":'Something went wrong while logging out'})


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