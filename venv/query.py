#Basic query sample

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password1",
    database="pb_project"
)
print("Please enter a number: ")
value = int(input())
mysql = "SELECT * FROM data where rb1 = %d OR rb2 = %d OR rb3 = %d OR rb4 = %d OR rb5 = %d" %(value, value, value, value, value)


mycursor=mydb.cursor()
mycursor.execute(mysql)
myresult=mycursor.fetchall()
print("There are ", mycursor.rowcount, " records.")
for row in myresult:
    print(row)