from config import mysql

def login_query(user_name, password):
    cursor = mysql.connection.cursor()
    query = """SELECT department_name, role_name FROM department INNER JOIN login_credential login ON 
    department.department_id = login.department_id_fk 
    INNER JOIN user_role ON user_role.role_id = login.user_role_fk
    WHERE login.login_email = %s AND login.login_password = %s """
    data = (user_name, password,)
    cursor.execute(query, data)
    return_data = cursor.fetchall()
    return return_data

