from config import mysql

class Admin:
        
    def edit_user(self, formData, id):

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



class Hr:
    
    def edit_user(self, formData, id):

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


class Sales:
    
    def update(self):
        pass


class Production:

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