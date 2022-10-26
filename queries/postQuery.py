from config import mysql
from datetime import date
from utils.error_handler import *

class Admin:

    def create_users(self, formData):
        self.emp_name = formData['employeeName']
        self.password = formData['password']
        self.confPassword = formData['confPassword']
        self.companyEmail = formData['companyEmail']
        self.department = formData['department']
        self.managers = formData['managers']
        self.role = formData['role']
        self.designation = formData['designation']
        self.salary = formData['salary']
        self.contactNo = formData['contactNo']
        self.CNIC = formData['CNIC']
        self.DOB = formData['DOB']
        self.city = formData['city']
        self.personalEmail = formData['personalEmail']
        self.address = formData['address']
        self.accountTitle = formData['accountTitle']
        self.accountNo = formData['accountNo']

        cursor = mysql.connection.cursor()
        my_query = """INSERT INTO employee_detail (employee_name, employee_address, employee_city, 
        employee_contact_no, employee_manager_id, employee_department_id, designation, salary, 
        date_of_birth, cnic, bank_account_title, personal_email, bank_account_number, register_date)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        data = (self.emp_name, self.address, self.city, self.contactNo, self.managers, self.department,
        self.designation, self.salary, self.DOB, self.CNIC, self.accountTitle, self.personalEmail,
        self.accountNo, date.today(),)
        cursor.execute(my_query, data)
        mysql.connection.commit()

        my_query = """SELECT employee_id FROM employee_detail WHERE cnic=%s"""
        data = (self.CNIC,)
        cursor.execute(my_query, data)
        row = cursor.fetchall()

        my_query = """INSERT INTO login_credential (login_email, login_password, employee_id_fk, user_role_fk, department_id_fk, active)
        VALUES (%s,%s,%s,%s,%s,%s)"""
        data = (self.companyEmail, self.password, row[0]['employee_id'], self.role, self.department, 1,)
        cursor.execute(my_query, data)
        mysql.connection.commit()

        

class Hr:

    def create_users(self, formData):
        self.emp_name = formData['employeeName']
        self.password = formData['password']
        self.confPassword = formData['confPassword']
        self.companyEmail = formData['companyEmail']
        self.department = formData['department']
        self.managers = formData['managers']
        self.role = formData['role']
        self.designation = formData['designation']
        self.salary = formData['salary']
        self.contactNo = formData['contactNo']
        self.CNIC = formData['CNIC']
        self.DOB = formData['DOB']
        self.city = formData['city']
        self.personalEmail = formData['personalEmail']
        self.address = formData['address']
        self.accountTitle = formData['accountTitle']
        self.accountNo = formData['accountNo']

        cursor = mysql.connection.cursor()
        my_query = """INSERT INTO employee_detail (employee_name, employee_address, employee_city, 
        employee_contact_no, employee_manager_id, employee_department_id, designation, salary, 
        date_of_birth, cnic, bank_account_title, personal_email, bank_account_number, register_date)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        data = (self.emp_name, self.address, self.city, self.contactNo, self.managers, self.department,
        self.designation, self.salary, self.DOB, self.CNIC, self.accountTitle, self.personalEmail,
        self.accountNo, date.today(),)
        cursor.execute(my_query, data)
        mysql.connection.commit()

        my_query = """SELECT employee_id FROM employee_detail WHERE cnic=%s"""
        data = (self.CNIC,)
        cursor.execute(my_query, data)
        row = cursor.fetchall()

        my_query = """INSERT INTO login_credential (login_email, login_password, employee_id_fk, user_role_fk, department_id_fk, active)
        VALUES (%s,%s,%s,%s,%s,%s)"""
        data = (self.companyEmail, self.password, row[0]['employee_id'], self.role, self.department, 1,)
        cursor.execute(my_query, data)
        mysql.connection.commit()


class Sales:

    def post(self):
        pass


class Production:

    def post(self):
        pass


# class Developers:

#     def post(self):
#         pass




AdminQueryPost = Admin()
HrQueryPost = Hr()
SaleQueryPost = Sales()
ProductionQueryPost = Production()
# DeveloperQueryPost = Developers()
