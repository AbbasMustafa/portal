from config import mysql


class Admin:

    def get_Role(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT role_id, role_name FROM user_role"""
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def get_Department(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT * FROM department"""
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data
    
    def get_Manager(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT * FROM manager_table"""
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def get_all_user(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT employee_id, employee_name, designation, salary, register_date, manager_name, 
        department_name, active FROM employee_detail INNER JOIN manager_table ON
        employee_detail.employee_manager_id = manager_table.manager_id INNER JOIN department ON 
        employee_detail.employee_department_id = department.department_id INNER JOIN login_credential ON
        login_credential.employee_id_fk = employee_detail.employee_id"""
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def edit_user_get(self, id):
        cursor = mysql.connection.cursor()
        my_query = f"""SELECT employee_id, employee_name, employee_address, employee_city, employee_contact_no, employee_manager_id, personal_email, login_email,
        employee_department_id, designation, salary, date_of_birth, cnic, bank_account_title, role_name, manager_name, department_name,
        bank_account_number, register_date, role_id FROM login_credential INNER JOIN employee_detail 
        ON login_credential.employee_id_fk = employee_detail.employee_id
        INNER JOIN department ON employee_detail.employee_department_id = department.department_id INNER JOIN 
        manager_table ON employee_detail.employee_manager_id = manager_table.manager_id INNER JOIN user_role ON
        employee_detail.employee_role_id = user_role.role_id WHERE employee_id = {id} """
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def password_request(self, id):
        cursor = mysql.connection.cursor()
        my_query = f"""SELECT login_email, login_password FROM login_credential WHERE employee_id_fk = {id} """
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data
        
    def empInfo(self, id):
        cursor = mysql.connection.cursor()
        my_query = f"""SELECT employee_name, employee_address, employee_city, employee_contact_no, personal_email, login_email,
        designation, salary, date_of_birth, cnic, bank_account_title, role_name, manager_name, department_name,
        bank_account_number, register_date FROM login_credential INNER JOIN employee_detail 
        ON login_credential.employee_id_fk = employee_detail.employee_id
        INNER JOIN department ON employee_detail.employee_department_id = department.department_id LEFT JOIN 
        manager_table ON employee_detail.employee_manager_id = manager_table.manager_id INNER JOIN user_role ON
        login_credential.user_role_fk = user_role.role_id WHERE employee_id = {id}"""
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def user_status(self, userStatus):
        cursor = mysql.connection.cursor()        
        my_query = f"""SELECT employee_id, employee_name, designation, salary, register_date, manager_name, 
        department_name, active FROM employee_detail INNER JOIN manager_table ON
        employee_detail.employee_manager_id = manager_table.manager_id INNER JOIN department ON 
        employee_detail.employee_department_id = department.department_id INNER JOIN login_credential ON
        login_credential.employee_id_fk = employee_detail.employee_id WHERE active = {userStatus}"""
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def is_manager(self, id):
        cursor = mysql.connection.cursor()        
        my_query = f"""SELECT manager_id FROM manager_table WHERE manager_emp_id = {id}"""
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data


class Hr (Admin):

    def get_Role(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT role_id, role_name FROM user_role WHERE role_name != 'Admin' """
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def get_Department(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT * FROM department WHERE department_name != 'Administration' """
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def activeUser(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT COUNT(login_email) FROM login_credential WHERE active = 1 """
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def banUser(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT COUNT(login_email) FROM login_credential WHERE active = 0 """
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data



class Sales:

    def get(self):
        pass


class Production:

    def get(self):
        pass


# class Developers:

#     def get(self):
#         pass




AdminQueryGet = Admin()
HrQueryGet = Hr()
SaleQueryGet = Sales()
ProductionQueryGet = Production()
# DeveloperQueryGet = Developers()
