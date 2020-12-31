#Basic query sample 3 for combing record into a list and count
import mysql.connector
from collections import Counter

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password1",
    database="pb_project"
)
mylist=[]

mysql = "SELECT rb1, rb2, rb3, rb4, rb5 FROM data where rb1 = 3"
mycursor=mydb.cursor()
mycursor.execute(mysql)
myresult=mycursor.fetchall()

for row in myresult:
    mylist.extend(row) #Put record in a list
print(mylist)

print(mylist)
myset = Counter(mylist)

for value, count in myset.most_common():
    print("%d appears %d times" %(value, count)) #Print count
#print(myset.most_common())
