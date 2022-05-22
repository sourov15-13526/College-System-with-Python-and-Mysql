import mysql.connector as mysql

db = mysql.connect(host="localhost",user="root",password="",database="college_system")
command_handler = db.cursor(buffered=True)

def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Insert Student data")
        print("2. Insert Teacher data")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            username = input(str("Student username : "))
            password = input(str("Student password : "))
            age = input(str("Student age : "))
            gender = input(str("student gender : "))
            contact = input(str("student contact : "))
            query_vals = (username,password,age,gender,contact)
            command_handler.execute("INSERT INTO users (username,password,privilege,age,gender,contact) VALUES (%s,%s,'student',%s,%s,%s)",query_vals)
            db.commit()
            print(username + " has been registered as a student")
        
        elif user_option == "2":
            print("")
            print("Register New Teacher")
            username = input(str("Teacher username : "))
            password = input(str("Teacher password : "))
            age = input(str("teacher age : "))
            gender = input(str("teacher gender : "))
            contact = input(str("teacher contact : "))
            query_vals = (username,password,age,gender,contact)
            command_handler.execute("INSERT INTO users (username,password,privilege,age,gender,contact) VALUES (%s,%s,'teacher',%s,%s,%s)",query_vals)
            db.commit()
            print(username + " has been registered as a teacher")
    
        elif user_option == "3":
            print("")
            print("Delete Existing Student Account")
            username = input(str("Student username : "))
            query_vals = (username,"student")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == "4":
            print("")
            print("Delete Existing Teacher Account")
            username = input(str("Teacher username : "))
            query_vals = (username,"teacher")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == "5":
            break
        else:
            print("No valid option selected")


def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "sourov":
        if password == "sourov1234":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised") 

def main():
    while 1:
        print("Welcome to the college system")
        print("")
        print("Enter 1 to login as admin")

        user_option = input(str("Option : "))
        if user_option == "1":
            auth_admin()
        else:
            print("No valid option was selected")

main()
