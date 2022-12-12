from config import mysql


class Admin:

    def get_Role(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT role_id, role_name FROM user_role"""
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot fetch role"


    def get_Department(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT * FROM department"""
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot fetch department"
    

    def get_Manager(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT * FROM manager_table"""
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot fetch manager"


    def get_all_user(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT employee_id, employee_name, designation, salary, register_date, manager_name, 
            department_name, active FROM employee_detail INNER JOIN manager_table ON
            employee_detail.employee_manager_id = manager_table.manager_id INNER JOIN department ON 
            employee_detail.employee_department_id = department.department_id INNER JOIN login_credential ON
            login_credential.employee_id_fk = employee_detail.employee_id"""
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot fetch all users"

    
    def edit_user_get(self, id):
        try:
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
        except Exception as e:
            print(e)
            return "Cannot get user data"


    def password_request(self, id):
        try:
            cursor = mysql.connection.cursor()
            my_query = f"""SELECT login_email, login_password FROM login_credential WHERE employee_id_fk = {id} """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get user password"
        

    def empInfo(self, id):
        try:
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
        except Exception as e:
            print(e)
            return "Cannot get user employee info"


    def user_status(self, userStatus):
        try:
            cursor = mysql.connection.cursor()        
            my_query = f"""SELECT employee_id, employee_name, designation, salary, register_date, manager_name, 
            department_name, active FROM employee_detail INNER JOIN manager_table ON
            employee_detail.employee_manager_id = manager_table.manager_id INNER JOIN department ON 
            employee_detail.employee_department_id = department.department_id INNER JOIN login_credential ON
            login_credential.employee_id_fk = employee_detail.employee_id WHERE active = {userStatus}"""
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get user status"


    def is_manager(self, id):
        try:
            cursor = mysql.connection.cursor()        
            my_query = f"""SELECT manager_id FROM manager_table WHERE manager_emp_id = {id}"""
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get is_manager"


    def get_sale_agent(self):
        try:
            cursor = mysql.connection.cursor()        
            my_query = f"""SELECT employee_id, employee_name, department_name FROM user_role INNER JOIN 
            employee_detail ON user_role.role_id = employee_detail.employee_role_id
            INNER JOIN department ON employee_detail.employee_department_id = department.department_id
            WHERE role_name = 'Admin' OR role_name = 'Sales' """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get sales agent"
    

    def get_production(self):
        try:
            cursor = mysql.connection.cursor()        
            my_query = f"""SELECT employee_id, employee_name, department_name, role_name FROM employee_detail INNER JOIN 
            manager_table ON employee_detail.employee_id = manager_table.manager_emp_id  INNER JOIN department ON 
            employee_detail.employee_department_id = department.department_id INNER JOIN user_role ON 
            user_role.role_id = employee_detail.employee_role_id
            WHERE department_name = 'Production' """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get production"


    def activeUser(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT COUNT(login_email) FROM login_credential WHERE active = 1 """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get active user count"


    def banUser(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT COUNT(login_email) FROM login_credential WHERE active = 0 """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get count of ban user"


    def get_service(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT * FROM service_table """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get writer service"


    def get_product(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT * FROM product_table """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get writer product"


    def getOrderId(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT order_id FROM order_detail ORDER BY order_id DESC LIMIT 1 """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get order id"


    def get_order(self,id):
        try:
            cursor = mysql.connection.cursor()
            my_query = f"""SELECT order_id, order_title, order_date, order_status, order_complete, order_deadline, order_pageNo, Price_order, currency,
            order_subjectArea, order_style, order_sourceNo, order_description, order_signature, order_detail.order_code, role_name order_type,
            order_acadmicLevel, service_name, product_name, order_metadata, order_service_dev, order_product_dev, chat_room_id, 
            group_concat(employee_name) employee_name, group_concat(order_assign_status) order_assign_status,
            group_concat(order_emp_status) order_emp_status
            FROM order_detail INNER JOIN order_employee_association ON order_detail.order_id = order_employee_association.order_id_fk
            INNER JOIN employee_detail ON employee_detail.employee_id = order_employee_association.employee_id_fk
            LEFT JOIN service_table ON order_detail.order_service = service_table.service_id LEFT JOIN product_table ON
            order_detail.order_product = product_table.product_id 
            INNER JOIN chat_table ON chat_table.chat_room_id = order_detail.order_chat_room INNER JOIN user_role ON user_role.role_id =
            order_detail.order_type LEFT JOIN order_price ON order_detail.order_id = order_price.order_id_fk
            WHERE order_id = '{id}' GROUP BY order_id"""
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get order"

    
    def get_order_doc(self, id):
        try:
            cursor = mysql.connection.cursor()
            my_query = f"""SELECT document_path, drive_folder_id from documents WHERE order_id_fk = {id}"""
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get order document"


    def get_order_chat(self, id, offset):
        try:  
            cursor = mysql.connection.cursor()
            my_query = f"""SELECT chat_message, chat_room_id_fk, chat_username, chat_date, employee_id_fk FROM chat_data
            INNER JOIN chat_table ON chat_table.chat_room_id = chat_data.chat_room_id_fk INNER JOIN 
            order_detail ON order_detail.order_chat_room = chat_table.chat_room_id WHERE
            order_detail.order_id = '{id}' ORDER BY (chat_data_id) DESC LIMIT 100 OFFSET {offset} """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get order chat"


    def get_all_order(self,limit,offset, emp_id, status):
        try:
            cursor = mysql.connection.cursor()
            # my_query = f"""SELECT order_id , order_detail.order_code, order_status, order_title, order_deadline, group_concat(employee_name) employee_name, 
            # group_concat(order_assign_status) order_assign, Price_order, currency
            # FROM order_detail INNER JOIN order_employee_association ON order_detail.order_id = order_employee_association.order_id_fk 
            # INNER JOIN employee_detail ON employee_detail.employee_id = order_employee_association.employee_id_fk INNER JOIN
            # order_price ON order_detail.order_id = order_price.order_id_fk
            # GROUP BY order_id ORDER BY order_id DESC LIMIT {limit} OFFSET {offset}"""

            if not status:

                my_query = f"""SELECT order_id , order_detail.order_code, order_status, order_title, order_deadline, group_concat(employee_name) employee_name, 
                group_concat(order_assign_status) order_assign, Price_order, currency FROM employee_detail INNER JOIN order_employee_association ON
                employee_detail.employee_id = order_employee_association.employee_id_fk INNER JOIN order_detail ON order_detail.order_id = 
                order_employee_association.order_id_fk INNER JOIN order_price ON order_price.order_id_fk = order_detail.order_id
                WHERE order_employee_association.order_id_fk in (SELECT order_id From order_detail INNER JOIN order_employee_association ON 
                order_detail.order_id = order_employee_association.order_id_fk
                WHERE order_employee_association.employee_id_fk = {emp_id}) GROUP BY order_id
                ORDER BY order_id DESC LIMIT {limit} OFFSET {offset}"""

            else:

                my_query = f""" SELECT order_id , order_detail.order_code, order_status, order_title, order_deadline, group_concat(employee_name) employee_name, 
                group_concat(order_assign_status) order_assign, Price_order, currency FROM employee_detail INNER JOIN order_employee_association ON
                employee_detail.employee_id = order_employee_association.employee_id_fk INNER JOIN order_detail ON order_detail.order_id = 
                order_employee_association.order_id_fk INNER JOIN order_price ON order_price.order_id_fk = order_detail.order_id
                WHERE order_employee_association.order_id_fk in (SELECT order_id From order_detail INNER JOIN order_employee_association ON 
                order_detail.order_id = order_employee_association.order_id_fk
                WHERE order_employee_association.employee_id_fk = '{emp_id}') AND order_detail.order_status = '{status}' GROUP BY order_id
                ORDER BY order_id DESC LIMIT {limit} OFFSET {offset} """

            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get all order"


    def get_recipients(self, id):
        try:
            cursor = mysql.connection.cursor()
            my_query = f"""SELECT employee_id, employee_name, role_name, department_name FROM employee_detail 
            INNER JOIN user_role ON employee_detail.employee_role_id = user_role.role_id LEFT JOIN department ON 
            employee_detail.employee_department_id = department.department_id WHERE employee_id 
            NOT IN(SELECT employee_id_fk FROM order_employee_association INNER JOIN
            order_detail ON order_detail.order_id = order_employee_association.order_id_fk WHERE 
            order_detail.order_id = '{id}') AND user_role.role_name != 'Hr'"""
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get recipients"


    def get_remove_recipient(self, id):
        try:
            cursor = mysql.connection.cursor()
            my_query = f"""SELECT employee_id, employee_name, role_name, department_name FROM employee_detail 
            INNER JOIN user_role ON employee_detail.employee_role_id = user_role.role_id 
            LEFT JOIN department ON employee_detail.employee_department_id = department.department_id 
            INNER JOIN order_employee_association ON employee_detail.employee_id=order_employee_association.employee_id_fk 
            LEFT JOIN manager_table ON employee_detail.employee_id = manager_table.manager_emp_id
            WHERE order_employee_association.order_id_fk = '{id}' AND user_role.role_name != 'Admin' AND employee_detail.employee_id 
            != COALESCE(manager_table.manager_emp_id,0)"""
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get remove recipients"


    def order_stats(self, id):
        try:
            cursor = mysql.connection.cursor()
            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE order_status = 'completed' AND order_employee_association.employee_id_fk = '{id}'  """
            cursor.execute(my_query)
            completed = cursor.fetchall()
            
            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE order_status = 'cancelled' AND order_employee_association.employee_id_fk = '{id}'  """
            cursor.execute(my_query)
            cancelled = cursor.fetchall()

            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE order_status = 'revision' AND order_employee_association.employee_id_fk = '{id}'  """
            cursor.execute(my_query)
            revision = cursor.fetchall()
            
            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE order_status = 'hold' AND order_employee_association.employee_id_fk = '{id}'  """
            cursor.execute(my_query)
            hold = cursor.fetchall()

            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE order_status = 'progress' AND order_employee_association.employee_id_fk = '{id}'  """
            cursor.execute(my_query)
            progress = cursor.fetchall()

            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE order_status != 'pre-order' AND order_employee_association.employee_id_fk = '{id}'  """
            cursor.execute(my_query)
            total = cursor.fetchall()

            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE  MONTH(CURRENT_DATE()) 
            AND order_status != 'pre-order' AND order_type = 4 AND order_employee_association.employee_id_fk = '{id}'  """
            cursor.execute(my_query)
            developer_monthly = cursor.fetchall()

            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE  MONTH(CURRENT_DATE()) 
            AND order_status != 'pre-order' AND order_type = 5 AND order_employee_association.employee_id_fk = '{id}'  """
            cursor.execute(my_query)
            writer_monthly = cursor.fetchall()

            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE  WEEK(CURRENT_DATE()) 
            AND order_status != 'pre-order' AND order_type = 4 AND order_employee_association.employee_id_fk = '{id}'  """
            cursor.execute(my_query)
            developer_weekly = cursor.fetchall()

            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE  WEEK(CURRENT_DATE()) 
            AND order_status != 'pre-order' AND order_type = 5 AND order_employee_association.employee_id_fk = '{id}'  """
            cursor.execute(my_query)
            writer_weekly = cursor.fetchall()

            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE DATE(order_date) = CURDATE()
            AND order_status != 'pre-order' AND order_type = 4 AND order_employee_association.employee_id_fk = '{id}' """
            cursor.execute(my_query)
            developer_daily = cursor.fetchall()

            my_query = f"""SELECT COUNT(order_id) FROM order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk  WHERE DATE(order_date) = CURDATE()
            AND order_status != 'pre-order' AND order_type = 5 AND order_employee_association.employee_id_fk = '{id}' """
            cursor.execute(my_query)
            writer_daily = cursor.fetchall()

            return [completed, cancelled, revision, hold, progress, total, developer_monthly, writer_monthly,
            developer_weekly, writer_weekly, developer_daily, writer_daily]

        except Exception as e:
            print(e)
            return "Cannot get fetch stats"


    def status_order(self, id, status, limit, offset):

        try:
            cursor = mysql.connection.cursor()
            my_query = f"""SELECT order_id , order_detail.order_code, order_status, order_title, order_deadline, group_concat(employee_name) employee_name, 
            group_concat(order_assign_status) order_assign, Price_order, currency FROM employee_detail INNER JOIN order_employee_association ON
            employee_detail.employee_id = order_employee_association.employee_id_fk INNER JOIN order_detail ON order_detail.order_id = 
            order_employee_association.order_id_fk INNER JOIN order_price ON order_price.order_id_fk = order_detail.order_id
            WHERE order_employee_association.order_id_fk in (SELECT order_id From order_detail INNER JOIN order_employee_association ON 
            order_detail.order_id = order_employee_association.order_id_fk
            WHERE order_employee_association.employee_id_fk = '{id}') AND order_detail.order_status = {status} GROUP BY order_id
            ORDER BY order_id DESC LIMIT {limit} OFFSET {offset} """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data

        except Exception as e:
            print(e)
            return "Cannot fetch orders"



class Hr (Admin):

    def get_Role(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT role_id, role_name FROM user_role WHERE role_name != 'Admin' """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get role"


    def get_Department(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT * FROM department WHERE department_name != 'Administration' """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get department"
    

    def get_all_user(self):
        try:
            cursor = mysql.connection.cursor()
            my_query = """SELECT employee_id, employee_name, designation, salary, register_date, manager_name, 
            department_name, active FROM employee_detail INNER JOIN manager_table ON
            employee_detail.employee_manager_id = manager_table.manager_id INNER JOIN department ON 
            employee_detail.employee_department_id = department.department_id INNER JOIN login_credential ON
            login_credential.employee_id_fk = employee_detail.employee_id AND department_name != 'Administration' """
            cursor.execute(my_query)
            return_data = cursor.fetchall()
            return return_data
        except Exception as e:
            print(e)
            return "Cannot get all user"




class Sales (Admin):

    def get(self):
        pass


class Production (Admin):

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
