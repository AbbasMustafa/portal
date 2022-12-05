from config import mysql

def login_query(user_name, password):
    cursor = mysql.connection.cursor()
    my_query = """SELECT department_name, role_name, employee_name, employee_id_fk, designation FROM department INNER JOIN login_credential login ON 
    department.department_id = login.department_id_fk 
    INNER JOIN user_role ON user_role.role_id = login.user_role_fk INNER JOIN employee_detail ON 
    login.employee_id_fk = employee_detail.employee_id
    WHERE (login.login_email = %s  AND login.login_password = %s) AND active = '1' """
    data = (user_name, password,)
    cursor.execute(my_query, data)
    return_data = cursor.fetchall()
    return return_data


def get_password(email):
    cursor = mysql.connection.cursor()
    my_query = """SELECT login_password, login_email FROM login_credential WHERE login_email=%s AND
    active = '1' """
    data = (email,)
    cursor.execute(my_query, data)
    return_data = cursor.fetchall()
    return return_data


def save_chat(message, room_id, username, date, emp_id_fk):
    cursor = mysql.connection.cursor()
    my_query = """INSERT INTO chat_data (chat_message, chat_room_id_fk, chat_username, chat_date, employee_id_fk) VALUES(%s,%s,%s,%s,%s)"""
    data = (message, room_id, username, date, emp_id_fk,)
    cursor.execute(my_query, data)
    mysql.connection.commit()
    return "saved"