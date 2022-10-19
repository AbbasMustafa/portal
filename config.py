from flask import Flask
from flask_mysqldb import MySQL
# import os
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

app = Flask(__name__)

mysql = MySQL(app)
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_PORT'] = ''
app.config['MYSQL_DB'] = ''
app.config['MYSQL_CURSORCLASS'] = ''
app.config['SECRET_KEY'] = ''