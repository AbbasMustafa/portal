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

    def get_sale_agent(self):
        cursor = mysql.connection.cursor()        
        my_query = f"""SELECT employee_id, employee_name, department_name FROM user_role INNER JOIN 
        employee_detail ON user_role.role_id = employee_detail.employee_role_id
        INNER JOIN department ON employee_detail.employee_department_id = department.department_id
        WHERE role_name = 'Admin' OR role_name = 'Sales' """
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data
    
    def get_production(self):
        cursor = mysql.connection.cursor()        
        my_query = f"""SELECT employee_id, employee_name, department_name, role_name FROM employee_detail INNER JOIN 
        manager_table ON employee_detail.employee_id = manager_table.manager_emp_id  INNER JOIN department ON 
        employee_detail.employee_department_id = department.department_id INNER JOIN user_role ON 
        user_role.role_id = employee_detail.employee_role_id
        WHERE department_name = 'Production' """
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

    def get_service(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT * FROM service_table """
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def get_product(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT * FROM product_table """
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def getOrderId(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT order_id FROM order_detail ORDER BY order_id DESC LIMIT 1 """
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def get_order(self,id):
        cursor = mysql.connection.cursor()
        my_query = f"""SELECT order_id, order_title, order_date, order_status, order_complete, order_deadline, order_pageNo,
        order_subjectArea, order_style, order_sourceNo, order_description, order_signature, order_detail.order_code, 
        order_acadmicLevel, service_name, product_name, order_metadata, order_service_dev, order_product_dev, drive_folder_id,
        group_concat(employee_name) employee_name, group_concat(order_assign_status) order_assign_status,
        group_concat(order_emp_status) order_emp_status
        FROM order_detail INNER JOIN order_employee_association ON order_detail.order_id = order_employee_association.order_id_fk
        INNER JOIN employee_detail ON employee_detail.employee_id = order_employee_association.employee_id_fk
        LEFT JOIN service_table ON order_detail.order_service = service_table.service_id LEFT JOIN product_table ON
        order_detail.order_product = product_table.product_id LEFT JOIN documents ON order_detail.order_id = documents.order_id_fk
        WHERE order_id = {id} GROUP BY order_id;"""
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    def get_all_order(self,limit,offset):
        cursor = mysql.connection.cursor()
        my_query = f"""SELECT order_id , order_detail.order_code, order_status, order_title, order_deadline, group_concat(employee_name) employee_name, 
        group_concat(order_assign_status) order_assign, Price_order, currency
        FROM order_detail INNER JOIN order_employee_association ON order_detail.order_id = order_employee_association.order_id_fk 
        INNER JOIN employee_detail ON employee_detail.employee_id = order_employee_association.employee_id_fk INNER JOIN
        order_price ON order_detail.order_id = order_price.order_id_fk
        GROUP BY order_id LIMIT {limit} OFFSET {offset}"""
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
    
    def get_all_user(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT employee_id, employee_name, designation, salary, register_date, manager_name, 
        department_name, active FROM employee_detail INNER JOIN manager_table ON
        employee_detail.employee_manager_id = manager_table.manager_id INNER JOIN department ON 
        employee_detail.employee_department_id = department.department_id INNER JOIN login_credential ON
        login_credential.employee_id_fk = employee_detail.employee_id AND department_name != 'Administration' """
        cursor.execute(my_query)
        return_data = cursor.fetchall()
        return return_data

    # def activeUser(self):
    #     cursor = mysql.connection.cursor()
    #     my_query = """SELECT COUNT(login_email) FROM login_credential WHERE active = 1 """
    #     cursor.execute(my_query)
    #     return_data = cursor.fetchall()
    #     return return_data

    # def banUser(self):
    #     cursor = mysql.connection.cursor()
    #     my_query = """SELECT COUNT(login_email) FROM login_credential WHERE active = 0 """
    #     cursor.execute(my_query)
    #     return_data = cursor.fetchall()
    #     return return_data



class Sales (Admin):

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
