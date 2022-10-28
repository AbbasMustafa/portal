from config import mysql

class Admin:

    def delete_user(self, id, active):
        cursor = mysql.connection.cursor()
        my_query = f"""UPDATE login_credential SET active = {active} WHERE employee_id_fk={id}"""
        cursor.execute(my_query)
        mysql.connection.commit()
        return 'User Deleted'


class Hr (Admin):

    def delete(self):
        pass
    # def delete_user(self, id, active):
    #     cursor = mysql.connection.cursor()
    #     my_query = f"""UPDATE login_credential SET active = {active} WHERE employee_id_fk={id}"""
    #     cursor.execute(my_query)
    #     mysql.connection.commit()
    #     return 'User Deleted'


class Sales:

    def delete(self):
        pass



class Production:

    def delete(self):
        pass


# class Writers:

#     def delete(self):
#         pass

AdminQueryDelete = Admin()
HrQueryDelete = Hr()
SaleQueryDelete = Sales()
ProductionQueryDelete = Production()
# WriterQueryDelete = Writers()
