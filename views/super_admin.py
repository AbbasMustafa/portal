from flask import Blueprint, redirect, url_for, render_template
from queries.deleteQuery import *
from queries.updateQuery import *
from queries.getQuery import *
from queries.postQuery import *
from utils.error_handler import *

superAdmin = Blueprint("superAdmin", __name__, static_folder='static', template_folder='templates/superAdmin')

@superAdmin.route('/')
def home_view():
    # Admin.get()
    # Admin.post()
    # Admin.delete()
    # Admin.update()
    return render_template('superAdmin/index.html')

