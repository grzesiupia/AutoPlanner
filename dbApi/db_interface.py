"""
    Module db_interface is used as api of data base
"""
# pylint: disable=C0301
import mysql.connector


mydb = mysql.connector.connect(
        host="185.66.213.128",
        user="uni",
        password="123",
        database="TEST001"
    )
mycursor = mydb.cursor()

def add_usser(*, login, password, email):
    """Adds usser to users table on database. Only keywords arguments are allowing.
    Example: add_usser(login='user', password='haslo', email='student@put.poznan.pl')"""
    mycursor.execute(f"INSERT INTO users (login, password, email) VALUES ({login!a}, {password!a}, {email!a})")
    mydb.commit()

def get_user_by_login(*, login):
    """Gets user tuple by login argument. Only keywords arguments are allowing.
    Example: get_user_by_login(login='user') gets tuple (login, password, email)."""
    mycursor.execute(f"SELECT * FROM users WHERE login = {login!a}")
    return mycursor.fetchone()

def delete_user_by_login(*, login):
    """Deletes user by login argument. Only keywords arguments are allowing.
    Example: delete_user_by_login(login='user') delete record from database."""
    mycursor.execute(f"DELETE FROM users WHERE login = {login!a}")
    mydb.commit()

def get_list_of_users():
    """Gets list of user tuples by login argument.
    Example: get_list_of_users() may gets list [(login1, password1, email1), (login2, password2, email2), ...]."""
    mycursor.execute("SELECT * FROM users")
    results = mycursor.fetchall()
    users_list = []
    for result in results:
        users_list.append(result)
    return users_list


#TEST ZONE
if __name__ == '__main__':
    pass
#    print(get_user_by_login(login='test1')[1])
#    print(get_list_of_users())
#    add_usser(login="tesdsat1", password='123', email='test1')
#     mydb = mysql.connector.connect(
#         host="185.66.213.128",
#         user="uni",
#         password="123",
#         database="TEST001"
#     )
#
#     mycursor = mydb.cursor()
#
#     INSERT TEST
#
#     sql = "INSERT INTO users (login, password, email) VALUES (%s, %s, %s)"
#     val = ("test", "admin", "test@admin")
#     mycursor.execute(sql, val)
#     mydb.commit()
#
#
#     SELECT TEST
#     mycursor.execute("SELECT * FROM users WHERE login = 'admin'")
#
#     myresult = mycursor.fetchall()
#
#     for x in myresult:
#         print(x)