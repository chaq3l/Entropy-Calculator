import mysql
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="test_database"
    )

mycursor = db.cursor()
#mycursor.execute("CREATE DATABASE test_database")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
