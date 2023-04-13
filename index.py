import mysql.connector

mydb = mysql.connector.connect(
    host="10.1.2.163",
    user="root",
    password="root",
    database="daDB1"    
)
def repeat():
    if mydb.is_connected():
        print("you are connected my nigga")

        mode = input("LOGIN/REGISTER/DELETE?: ")

    if mode == "REGISTER" or "register":
        print("register")
        exit
        emall = input("Enter Email: ")
        userNAM = input("Enter Username: ")
        password = input("Enter Password: ")
        cmd =  "insert into daDB1.userinfo (emailADD, username, passHASH) values (%s, %s, %s)"
        userdata = (emall, userNAM, password)
        cursor = mydb.cursor()
        cursor.execute(cmd, userdata)

        mydb.commit()
        cursor.close()
        mydb.close()

    elif mode == "DELETE" or "delete":
        print("delete")
        IDnum = input("Enter ID number: ")

        cmd = "delete from daDB1.userinfo where id= %s;"
        selected = (IDnum)
        cursor = mydb.cursor()
        cursor.execute(cmd,IDnum)
        mydb.commit()
        cursor.close()
        mydb.close()
repeat()





    



    # dbname = input("create what database:")
    


    # cursor = mydb.cursor()
    # cursor.execute("select * from persons")

    # for persons in cursor:
    #     print(persons)

    # cursor.execute("create database " + dbname)

    # if cursor.execute == False:
    #     print("invalid string")
    # else:
    #     print("database created") 


    # if(not cursor.execute):
    #     print("Failed")
    #     exit
    # print("Success")




# cursor = mydb.cursor()
# cursor.execute("create database testest;")
