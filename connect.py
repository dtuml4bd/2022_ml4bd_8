import mysql.connector 

mydb = mysql.connector.connect(
    host ="localhost",
    username="root",
    password="",
    database="mysqlpython"
)
mycursor=mydb.cursor()
# mycursor.execute("create database person")
mycursor.execute("CREATE table studentDetail (id VARCHAR(40) PRIMARY KEY ,name VARCHAR(40))")
print("Database Created")
    