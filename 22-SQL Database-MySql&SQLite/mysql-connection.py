# pip install mysql-connector ile connector kurulumu yapıyoruz

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="node-app"
)
mycursor=mydb.cursor()
# mycursor.execute("CREATE TABLE custormers (name VARCHAR(255), address VARCHAR(255)) ")

# mycursor.execute("CREATE DATABASE mydatabase")  # kod ile database oluşturmak
# mycursor.execute("SHOW DATABASES") # IDE açmadan databaseleri programda görüntüleyebiliriz
# for x in mycursor:
#     print(x)