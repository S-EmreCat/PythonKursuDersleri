import mysql.connector 

###  DATABASE bağlantımızı yaptık
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="schooldb"
)