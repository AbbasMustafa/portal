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

class Hr:

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
    
    def get_Manager(self):
        cursor = mysql.connection.cursor()
        my_query = """SELECT * FROM manager_table"""
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
