from config import mysql

def login_query(user_name, password):
    cursor = mysql.connection.cursor()
    query = """SELECT role_name FROM login_credential INNER JOIN user_role
        ON login_credential.user_role_fk = user_role.role_id WHERE login_email = %s AND login_password = %s """
    data = (user_name, password,)
    cursor.execute(query, data)
    return_data = cursor.fetchall()
    return return_data

