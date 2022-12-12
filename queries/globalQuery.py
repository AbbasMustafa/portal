from config import mysql
from datetime import datetime

def login_query(user_name, password):
    try : 
        cursor = mysql.connection.cursor()
        my_query = """SELECT department_name, role_name, employee_name, employee_id_fk, designation, manager_emp_id FROM department INNER JOIN login_credential login ON 
        department.department_id = login.department_id_fk 
        INNER JOIN user_role ON user_role.role_id = login.user_role_fk INNER JOIN employee_detail ON 
        login.employee_id_fk = employee_detail.employee_id LEFT JOIN manager_table ON employee_detail.employee_id = manager_table.manager_emp_id
        WHERE (login.login_email = %s  AND login.login_password = %s) AND active = '1' ; """
        data = (user_name, password,)
        cursor.execute(my_query, data)
        return_data = cursor.fetchall()
        return return_data
    
    except Exception as e:
        print(e)
        return "Error while logging in "


def get_password(email):
    try:
        cursor = mysql.connection.cursor()
        my_query = """SELECT login_password, login_email FROM login_credential WHERE login_email=%s AND
        active = '1' """
        data = (email,)
        cursor.execute(my_query, data)
        return_data = cursor.fetchall()
        return return_data
    except Exception as e:
        print(e)
        return "Error while retriveing password"


def save_chat(message, room_id, username, date, emp_id_fk):
    try:
        cursor = mysql.connection.cursor()
        my_query = """INSERT INTO chat_data (chat_message, chat_room_id_fk, chat_username, chat_date, employee_id_fk) VALUES(%s,%s,%s,%s,%s)"""
        data = (message, room_id, username, date, emp_id_fk,)
        cursor.execute(my_query, data)
        mysql.connection.commit()
        return "saved"
    except Exception as e:
        print(e)
        return "Error while saving chat"


def create_single_chat(user, empId):
    try:
        cursor = mysql.connection.cursor()

        my_query = """SELECT chat_room_id FROM chat_table INNER JOIN chat_association_table ON 
        chat_table.chat_room_id = chat_association_table.room_id_fk
        WHERE chat_table.created_by =%s AND chat_association_table.employee_id_fk =%s"""
        data=(user, id_date,)
        cursor.execute(my_query)
        is_exsist = cursor.fetchall()

        if not is_exsist:

            my_query = """INSERT INTO chat_table (created_by, created_at) VALUES (%s,%s)"""
            id_date = datetime.now()
            data = (user, id_date,)
            cursor.execute(my_query, data)
            mysql.connection.commit()

            my_query = f"""SELECT chat_room_id FROM chat_table WHERE created_at = {id_date} """
            cursor.execute(my_query)
            chat_id = cursor.fetchall()

            my_query = """INSERT INTO chat_association_table (employee_id_fk, room_id_fk) VALUES (%s,%s)"""
            data = (empId, chat_id,)
            cursor.execute(my_query, data)
            mysql.connection.commit()

            return chat_id

    except Exception as e:
        print(e)
        return "Problem Creating Chat"