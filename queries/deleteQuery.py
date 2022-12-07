from config import mysql

class Admin:

    def delete_user(self, id, active):
        try:
            cursor = mysql.connection.cursor()
            my_query = f"""UPDATE login_credential SET active = {active} WHERE employee_id_fk={id}"""
            cursor.execute(my_query)
            mysql.connection.commit()
            return 'User Deleted'
        except Exception as e:
            print(e)
            return "Cannot delete user"


class Hr (Admin):

    def delete(self):
        pass


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
