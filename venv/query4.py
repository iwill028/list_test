#Basic query sample 4 final
import mysql.connector
from collections import Counter

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password1",
    database="pb_project"
)

#Query the game number by a input regular ball number
print("Please enter a number: ")
rb = int(input())
str_no = ""
sql_no = "SELECT no FROM data where rb1 = %d OR rb2 = %d OR rb3 = %d OR rb4 = %d OR rb5 = %d" %(rb, rb, rb, rb, rb)
#sql_no = "SELECT no FROM data where rb1 = %d" %(rb)
cursor_no=mydb.cursor()
cursor_no.execute(sql_no)
result_no=cursor_no.fetchall()
#print("There are ", cursor_no.rowcount, " records.")
list_no = [row_no[0]+1 for row_no in result_no]
str_no = ",".join(str(i) for i in list_no)
#print(str_no)
#print(list_no)

#Query the regular ball numbers by game NOs
list_rb = []
sql_rb = "SELECT rb1, rb2, rb3, rb4, rb5 FROM data where no IN (%s)" %(str_no)
#print(sql_rb)
cursor_rb=mydb.cursor()
cursor_rb.execute(sql_rb)
result_rb=cursor_rb.fetchall()
for row_rb in result_rb:
    list_rb.extend(row_rb)

#Query the power ball numbers by game NOs
list_pb = []
sql_pb = "SELECT pb FROM data where no IN (%s)" %(str_no)
#print(sql_rb)
cursor_pb=mydb.cursor()
cursor_pb.execute(sql_pb)
result_pb=cursor_pb.fetchall()
for row_pb in result_pb:
    list_pb.extend(row_pb)

set_rb = Counter(list_rb)
for value, count in set_rb.most_common():
    print("%d appears %d times" %(value, count)) #Print count

set_pb = Counter(list_pb)
for value, count in set_pb.most_common():
    print("PB %d appears %d times" %(value, count))