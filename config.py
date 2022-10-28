from flask import Flask
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)

mysql = MySQL(app)
app.config['MYSQL_USER'] = os.getenv('DB_USERNAME')
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_DB'] = os.getenv('DB_NAME')
app.config['MYSQL_CURSORCLASS'] = os.getenv('DB_CURSORCLASS')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')