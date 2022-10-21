from flask import Flask, render_template, request, session, url_for, redirect
from config import *
from views.super_admin import superAdmin
from views.hr import hr
from views.sales import sale
from views.writers import writer
from views.developers import developer
from utils.error_handler import *
from utils.auth import *
from utils.redirectRouter import *
from queries.globalQuery import *


# app = Flask(__name__)
# baseUrl = "/api"


app.register_blueprint(superAdmin, url_prefix = '/admin')
app.register_blueprint(hr, url_prefix = '/hr')
app.register_blueprint(sale, url_prefix = '/sale')
app.register_blueprint(writer, url_prefix = '/writer')
app.register_blueprint(developer, url_prefix = '/developer')


@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
@try_except
def login_view():
    if request.method == "POST":
        user_name = request.form.get('username')
        password = request.form.get('pass')
        return_data = login_query(user_name, password)
        if return_data:
            session['user_role'] = return_data[0]['role_name']
            return route_to()
        else:
            return 'Wrong Credentials'
    else:
        return render_template('login.html')


@app.route('/logout')
@login_required
@try_except
def logout_view():
    session.clear()
    return redirect(url_for('login_view'))



if __name__ == '__main__':
    app.run(debug=True, port=5000)