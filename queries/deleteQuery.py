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


    def delete_order_recipients(self, formData):

        try:
            id = formData['orderId']
            emp_id = formData['recipients']
            room_id = formData['roomId']

            cursor = mysql.connection.cursor()
            my_query = f"""DELETE FROM order_employee_association WHERE order_id_fk='{id}' AND employee_id_fk = '{emp_id}' """
            cursor.execute(my_query)
            mysql.connection.commit()

            my_query = f"""DELETE FROM chat_association_table WHERE employee_id_fk = '{emp_id}' AND room_id_fk = '{room_id}' """
            cursor.execute(my_query)
            mysql.connection.commit()
            
            return 'Recipient Deleted'
        
        except Exception as e:
            print(e)
            return "Cannot remove recipients"


class Hr (Admin):

    def delete(self):
        pass


class Sales(Admin):

    def delete(self):
        pass



class Production(Admin):

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
