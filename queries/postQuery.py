from config import mysql
from datetime import datetime, date
from utils.error_handler import *
from utils.google_drive import *

class Admin:
    def create_users(self, formData):

        try:
            self.emp_name = formData['employeeName']
            self.password = formData['password']
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

            if self.managers == "" or not self.managers:
                self.managers = None

            if self.salary == "" or not self.salary:
                self.salary = None
            
            cursor = mysql.connection.cursor()

            my_query = """INSERT INTO employee_detail (employee_name, employee_address, employee_city, 
            employee_contact_no, employee_manager_id, employee_department_id, designation, salary, 
            date_of_birth, cnic, bank_account_title, personal_email, bank_account_number, register_date, employee_role_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            data = (self.emp_name, self.address, self.city, self.contactNo, self.managers, self.department,
            self.designation, self.salary, self.DOB, self.CNIC, self.accountTitle, self.personalEmail,
            self.accountNo, date.today(), self.role,)
            cursor.execute(my_query, data)
            mysql.connection.commit()

            my_query = """SELECT employee_id FROM employee_detail WHERE cnic=%s"""
            data = (self.CNIC,)
            cursor.execute(my_query, data)
            row = cursor.fetchall()

            if 'isManager' in formData:

                my_query =f"""SELECT department_name FROM department WHERE department_id = {self.department}"""
                cursor.execute(my_query)
                dept = cursor.fetchall()

                my_query =f"""SELECT role_name FROM user_role WHERE role_id = {self.role}"""
                cursor.execute(my_query)
                Role = cursor.fetchall()

                managerDepart = f"{dept[0]['department_name']} - {Role[0]['role_name']}"
                my_query = """INSERT INTO manager_table (manager_name, manager_department, manager_emp_id) VALUES (%s,%s,%s)"""
                data = (self.emp_name, managerDepart, row[0]['employee_id'],)
                cursor.execute(my_query,data)
                mysql.connection.commit()

            my_query = """INSERT INTO login_credential (login_email, login_password, employee_id_fk, user_role_fk, department_id_fk, active)
            VALUES (%s,%s,%s,%s,%s,%s)"""
            data = (self.companyEmail, self.password, row[0]['employee_id'], self.role, self.department, 1,)
            cursor.execute(my_query, data)
            mysql.connection.commit()

            return "success"
        except Exception as e:
            return "error"

    # def add_department(self, depart):
    #     cursor = mysql.connection.cursor()
    #     my_query = """INSERT INTO department (department_name) VALUES (%s)"""
    #     data = (depart,)
    #     cursor.execute(my_query, data)
    #     mysql.connection.commit()
    #     return "Department Added"

    def create_orders(self, formData, saveDir, doctype, directory, fileName):
        
        try:
            self.orderCode = formData['orderCode']
            self.saleAgent = formData['saleAgentsInput']
            self.orderTitle = formData['orderTitle']
            self.oredrType = formData['oredrType']
            self.assignedTo = formData['assignedToInput']
            self.service = formData['service']
            self.product = formData['product']
            self.deadline = formData['deadline']
            # self.cost = formData['cost']
            self.totalCost = formData['totalCost']
            self.numberOfPage = formData['numberOfPage']
            self.AcedmicLevel = formData['AcedmicLevel']
            self.style = formData['style']
            self.numberOfSoruce = formData['numberOfSoruce']
            self.description = formData['description']
            self.signed = formData['signed']
            # self.files = formData['files[]']
            self.subjectArea = formData['subjectArea']
            self.keyValuePiar = formData['keyValuePiar']
            self.serviceDev = formData['serviceDev']
            self.productDev = formData['productDev']
            self.currency = formData['currency']

            cursor = mysql.connection.cursor()

            saleAgent = self.saleAgent.split(',')
            assignedTo = self.assignedTo.split(',')

            if not self.service or not self.product:
                self.service = None
                self.product = None

            my_query = """INSERT INTO order_detail (order_title, order_date, order_service, order_product, 
            order_deadline, order_pageNo, order_subjectArea, order_style, order_sourceNo, order_description, 
            order_signature, order_code, order_acadmicLevel, order_type, order_metadata, order_service_dev, 
            order_product_dev, currency)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            data = (self.orderTitle, datetime.today(), self.service, self.product, self.deadline,
            self.numberOfPage, self.subjectArea, self.style, self.numberOfSoruce, self.description,
            self.signed, self.orderCode, self.AcedmicLevel, self.oredrType, self.keyValuePiar, self.serviceDev, 
            self.productDev, self.currency,)
            cursor.execute(my_query, data)
            mysql.connection.commit()

            my_query = f"""SELECT order_id FROM order_detail WHERE order_code = '{self.orderCode}' """
            cursor.execute(my_query)
            orderID = cursor.fetchall()

            for saleAgent in saleAgent:
                my_query = """INSERT INTO order_employee_association (employee_id_fk, order_id_fk, order_emp_status, order_code, order_assign_status) VALUES(%s,%s,%s,%s,%s)"""
                data = (saleAgent, orderID[0]['order_id'], 'Active', self.orderCode, 'assign by',)
                cursor.execute(my_query, data)
                mysql.connection.commit()

            for assignedTo in assignedTo:
                my_query = """INSERT INTO order_employee_association (employee_id_fk, order_id_fk, order_emp_status, order_code, order_assign_status) VALUES(%s,%s,%s,%s,%s)"""
                data = (assignedTo, orderID[0]['order_id'], 'Active', self.orderCode, 'assign to',)
                cursor.execute(my_query, data)
                mysql.connection.commit()

            my_query = """INSERT INTO order_price (Price_order, order_id_fk, order_code) VALUES(%s,%s,%s)"""
            data = (self.totalCost, orderID[0]['order_id'], self.orderCode,)
            cursor.execute(my_query, data)
            mysql.connection.commit()

            googleDoc = fileUpload(fileName, orderID[0]['order_id'], directory)

            for i in range(len(doctype)):
                my_query = """INSERT INTO documents (document_path, order_id_fk, document_type, drive_folder_id, drive_file_id, order_code) VALUES(%s,%s,%s,%s,%s,%s)"""
                data = (saveDir[i], orderID[0]['order_id'], doctype[i], googleDoc[0], googleDoc[1][i], self.orderCode,)
                cursor.execute(my_query, data)
                mysql.connection.commit()
            
            return "success"

        except Exception as e:
            # print(e)
            return "error"

        


        

        
class Hr:
    
    def create_users(self, formData):
        try:
            self.emp_name = formData['employeeName']
            self.password = formData['password']
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
            date_of_birth, cnic, bank_account_title, personal_email, bank_account_number, register_date, employee_role_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            data = (self.emp_name, self.address, self.city, self.contactNo, self.managers, self.department,
            self.designation, self.salary, self.DOB, self.CNIC, self.accountTitle, self.personalEmail,
            self.accountNo, date.today(), self.role,)
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

            return "success"

        except Exception:
            # print(Exception)
            return "error"



class Sales (Admin):

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
