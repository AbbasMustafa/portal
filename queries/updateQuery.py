from config import mysql
from utils.google_drive import *
from flask import request
from utils.mailSender import *

class Admin:
        
    def edit_user(self, formData, id):

        try:
            self.emp_name = formData['employeeName']
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
            self.id = id

            cursor = mysql.connection.cursor()

            if 'isManager' in formData and formData['isManager'] == 'on':
                my_query =f"""SELECT department_name FROM department WHERE department_id = {self.department}"""
                cursor.execute(my_query)
                dept = cursor.fetchall()

                my_query =f"""SELECT role_name FROM user_role WHERE role_id = {self.role}"""
                cursor.execute(my_query)
                Role = cursor.fetchall()

                managerDepart = f"{dept[0]['department_name']} - {Role[0]['role_name']}"
                my_query = """INSERT INTO manager_table (manager_name, manager_department,manager_emp_id) VALUES (%s,%s,%s)"""
                data = (self.emp_name, managerDepart, self.id,)
                cursor.execute(my_query,data)
                mysql.connection.commit()

            elif 'isManager' in formData and formData['isManager'] == 'off':
                my_query = f"""DELETE FROM manager_table WHERE manager_emp_id = {self.id}"""
                cursor.execute(my_query)
                mysql.connection.commit()


            my_query = """UPDATE employee_detail SET employee_name=%s, employee_address=%s, 
            employee_city=%s, employee_contact_no=%s, employee_manager_id=%s, employee_department_id=%s, 
            designation=%s, salary=%s, date_of_birth=%s, cnic=%s, bank_account_title=%s, 
            personal_email=%s, bank_account_number=%s, employee_role_id=%s WHERE employee_id=%s"""
            data = (self.emp_name, self.address, self.city, self.contactNo, self.managers, self.department,
            self.designation, self.salary, self.DOB,self.CNIC, self.accountTitle, self.personalEmail,
            self.accountNo, self.role, self.id,)
            cursor.execute(my_query, data)
            mysql.connection.commit()

            my_query = """UPDATE login_credential SET login_email=%s, user_role_fk=%s, department_id_fk=%s
            WHERE employee_id_fk=%s """
            data = (self.companyEmail, self.role, self.department, self.id,)
            cursor.execute(my_query, data)
            mysql.connection.commit()

            return 'User Updated'
        
        except Exception as e:
            print(e)
            return 'error'





    def edit_order(self, formData, saveDir, doctype, directory, fileName, id):
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
            # self.room_id = formData['chat_room_id']
            self.folderId = request.headers['drive_folder_id']

            cursor = mysql.connection.cursor()

            saleAgent = self.saleAgent.split(',')
            assignedTo = self.assignedTo.split(',')

            if not self.service or not self.product or not self.numberOfPage or not self.numberOfSoruce:
                self.service = None
                self.product = None
                self.numberOfPage = None
                self.numberOfSoruce = None


            if len(fileName) > 0:

                if self.folderId != "null":

                    googleDoc = fileUpdate(fileName, self.folderId, directory)
                    # print(saveDir, id, doctype, googleDoc, googleDoc)
                    for i in range(len(doctype)):
                        my_query = """INSERT INTO documents (document_path, order_id_fk, document_type, drive_folder_id, drive_file_id, order_code) VALUES(%s,%s,%s,%s,%s,%s)"""
                        data = (saveDir[i], id, doctype[i], googleDoc[0], googleDoc[1][i], self.orderCode,)
                        cursor.execute(my_query, data)
                        mysql.connection.commit()

                else:

                    googleDoc = fileUpload(fileName, id, directory)
                    print("return", googleDoc)
                    for i in range(len(doctype)):
                        my_query = """INSERT INTO documents (document_path, order_id_fk, document_type, drive_folder_id, drive_file_id, order_code) VALUES(%s,%s,%s,%s,%s,%s)"""
                        data = (saveDir[i], id, doctype[i], googleDoc[0], googleDoc[1][i], self.orderCode,)
                        cursor.execute(my_query, data)
                        mysql.connection.commit()

            
            
            my_query = """UPDATE order_detail SET order_title=%s, order_service=%s, order_product=%s, 
            order_deadline=%s, order_pageNo=%s, order_subjectArea=%s, order_style=%s, order_sourceNo=%s, order_description=%s, 
            order_signature=%s, order_acadmicLevel=%s, order_type=%s, order_metadata=%s, order_service_dev=%s, 
            order_product_dev=%s WHERE order_id = %s"""
            data = (self.orderTitle, self.service, self.product, self.deadline,
            self.numberOfPage, self.subjectArea, self.style, self.numberOfSoruce, self.description,
            self.signed, self.AcedmicLevel, self.oredrType, self.keyValuePiar, self.serviceDev, 
            self.productDev,id)
            cursor.execute(my_query, data)
            mysql.connection.commit()


            my_query = """UPDATE order_price SET Price_order=%s, currency=%s WHERE order_id_fk=%s"""
            data = (self.totalCost, self.currency, id)
            cursor.execute(my_query, data)
            mysql.connection.commit()
        
            
            return "Order Updated"

        except Exception as e:
            print(e)
            return "error"


    def add_recipients(self, formData):

        try:
            self.recipient = formData['recipients']
            self.role = formData['role']
            self.order_id = formData['orderId']
            self.order_code = formData['orderCode']
            self.room_id = formData['roomId']
            self.user_email = formData['userEmail']
            self.domain = formData['domain']

            if self.role == 'Developer' or self.role == 'Writer' or self.role == 'Freelancer':
                assign_status = 'assign to'
                user_role = 'production'
            else:
                assign_status = 'assign by'
                user_role = self.role

            cursor = mysql.connection.cursor()

            my_query = """INSERT INTO order_employee_association 
            (order_id_fk, employee_id_fk, order_emp_status, order_code, order_assign_status) 
            VALUES (%s,%s,%s,%s,%s)"""
            data = (self.order_id, self.recipient, 'Active', self.order_code, assign_status,)
            cursor.execute(my_query, data)
            mysql.connection.commit()


            my_query = """INSERT INTO chat_association_table (employee_id_fk, room_id_fk, chat_type) VALUES(%s,%s,%s)"""
            data = (self.recipient, self.room_id, 'order',)
            cursor.execute(my_query, data)
            mysql.connection.commit()


            mail_sender(self.user_email, self.order_id, self.domain, user_role)

            return "Recipient Added"

        except Exception as e:
            print(e)
            return "error"


    def update_order_status(self,formData):
        
        try:
            self.order_id = formData['orderId']
            self.status = formData['status']
            
            cursor = mysql.connection.cursor()

            my_query = f"""UPDATE order_detail SET order_status='{self.status}' WHERE order_id = '{self.order_id}' """
            cursor.execute(my_query)
            mysql.connection.commit()

            return self.status

        except Exception as e:
            print(e)
            return "Cannot change status"



    def update_file(self, saveDir, doctype, directory, fileName, orderId, folder_id):

        try:

            if len(fileName) > 0:

                cursor = mysql.connection.cursor()

                if folder_id != "":

                    googleDoc = fileUpdate(fileName, folder_id, directory)
                    # print(saveDir, id, doctype, googleDoc, googleDoc)
                    for i in range(len(doctype)):
                        my_query = """INSERT INTO documents (document_path, order_id_fk, document_type, drive_folder_id, drive_file_id, order_code) VALUES(%s,%s,%s,%s,%s,%s)"""
                        data = (saveDir[i], orderId, doctype[i], googleDoc[0], googleDoc[1][i], f"ORDER# {orderId}",)
                        cursor.execute(my_query, data)
                        mysql.connection.commit()

                    return ["File added", googleDoc[1]]

                else:

                    googleDoc = fileUpload(fileName, orderId, directory)
                
                    for i in range(len(doctype)):
                        my_query = """INSERT INTO documents (document_path, order_id_fk, document_type, drive_folder_id, drive_file_id, order_code) VALUES(%s,%s,%s,%s,%s,%s)"""
                        data = (saveDir[i], orderId, doctype[i], googleDoc[0], googleDoc[1][i], f"ORDER# {orderId}",)
                        cursor.execute(my_query, data)
                        mysql.connection.commit()

                    return ["File added", googleDoc[1]]

        except Exception as e:
            print(e)
            return "Error uploading file"


    def add_recipients_global(self, formData):

        try:
            empId = formData['empId']
            roomId = formData['roomId']

            cursor = mysql.connection.cursor()

            my_query = """INSERT INTO chat_association_table (employee_id_fk, room_id_fk, chat_type)
            VALUES (%s,%s,%s)"""
            data = (empId, roomId, 'global')
            cursor.execute(my_query, data)
            mysql.connection.commit()

            return "Recipient added"

        except Exception as e:
            print(e)
            return "Cannot add recipient"






class Hr:

    def edit_user(self, formData, id):
        try:
            self.emp_name = formData['employeeName']
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
            self.id = id

            cursor = mysql.connection.cursor()
            
            my_query = """UPDATE employee_detail SET employee_name=%s, employee_address=%s, 
            employee_city=%s, employee_contact_no=%s, employee_manager_id=%s, employee_department_id=%s, 
            designation=%s, salary=%s, date_of_birth=%s, cnic=%s, bank_account_title=%s, 
            personal_email=%s, bank_account_number=%s, employee_role_id=%s WHERE employee_id=%s"""
            data = (self.emp_name, self.address, self.city, self.contactNo, self.managers, self.department,
            self.designation, self.salary, self.DOB,self.CNIC, self.accountTitle, self.personalEmail,
            self.accountNo, self.role, self.id,)
            cursor.execute(my_query, data)
            mysql.connection.commit()

            my_query = """UPDATE login_credential SET login_email=%s, user_role_fk=%s, department_id_fk=%s
            WHERE employee_id_fk=%s """
            data = (self.companyEmail, self.role, self.department, self.id,)
            cursor.execute(my_query, data)
            mysql.connection.commit()

            return "User Updated"
        
        except Exception as e:
            return "error"


    
    def add_recipients_global(self, formData):

        try:
            empId = formData['empId']
            roomId = formData['roomId']

            cursor = mysql.connection.cursor()

            my_query = """INSERT INTO chat_association_table (employee_id_fk, room_id_fk, chat_type)
            VALUES (%s,%s,%s)"""
            data = (empId, roomId, 'global')
            cursor.execute(my_query, data)
            mysql.connection.commit()

            return "Recipient added"

        except Exception as e:
            print(e)
            return "Cannot add recipient"


class Sales (Admin):
    
    def update(self):
        pass


class Production (Admin):

    def update(self):
        pass


# class Developers:
    
#     def update(self):
#         pass


AdminQueryUpdate = Admin()
HrQueryUpdate = Hr()
SaleQueryUpdate = Sales()
ProductionQueryUpdate = Production()
# DeveloperQueryUpdate = Developers()