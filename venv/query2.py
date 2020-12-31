#Basic query sample 2 for adding item
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password1",
    database="pb_project"
)
print("Please enter a number: ")
value = int(input())
mysql = "SELECT no FROM data where rb1 = %d OR rb2 = %d OR rb3 = %d OR rb4 = %d OR rb5 = %d" %(value, value, value, value, value)
mylist = []
mycursor=mydb.cursor()
mycursor.execute(mysql)
myresult=mycursor.fetchall()
print("There are ", mycursor.rowcount, " records.")

for row in myresult:
    mylist.extend(row) #Put record in a list
#print(mylist)

for i in mylist:
    j=i+1
    print(j)