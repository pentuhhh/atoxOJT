import mysql.connector
from argon2 import PasswordHasher



mydb = mysql.connector.connect(
    host="10.1.2.163",
    user="root",
    password="root",
    database="daDB1"    
)
if mydb.is_connected():
    while True:
        mode = input("LOGIN/REGISTER/DELETE/UPDATE/EXIT?: ")
        if mode == "REGISTER" or mode == "register":
            print("register")
            email = input("Enter Email: ")
            userNAM = input("Enter Username: ")
            password = input("Enter Password: ")
            cmd =  "insert into daDB1.userinfo (emailADD, username, passHASH) values (%s, %s, %s)"
            userdata = (email, userNAM, password)
            cursor = mydb.cursor()
            cursor.execute(cmd, userdata)
        elif mode == "DELETE" or mode == "delete":
            print("delete")
            IDnum = int(input("Enter ID number: "))
            cmd = "delete from daDB1.userinfo where id=%s"
            selected = (IDnum,)
            cursor = mydb.cursor()
            cursor.execute(cmd,selected)
        elif mode == "UPDATE" or mode == "update":
            IDnum = int(input("Enter ID number: "))
            newdata = input("Email or Password?: ")
            if newdata == "Email" or newdata == "email":
                value1 = input("Enter New Email: ")
                cmd = "UPDATE userinfo SET emailADD=%s WHERE id=%s"
            elif newdata == "Password" or newdata == "password":
                value1 = input("Enter New Password: ")
                cmd = "UPDATE userinfo SET passHASH=%s WHERE id=%s"
            userdata = (value1,IDnum)
            cursor = mydb.cursor()
            cursor.execute(cmd, userdata)
        elif mode == "EXIT" or mode == "exit":
            quit()
        elif mode == "Display" or mode == "display":
            cursor = mydb.cursor()
            cursor.execute("select * from userinfo")
            print("---------------------------------------------------------------")
            for data in cursor:
                print("\n")
                print(data)

            print("---------------------------------------------------------------")
        else:
            print("Invalid")
        mydb.commit()
    cursor.close()
    mydb.close()
    
# March 29. 2023 Exercise