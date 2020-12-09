import pymysql
from python_mysql_dbconfig import read_db_config
conn = pymysql.connect(host='localhost',user='root',password='abc123',db='kptm')
tablename = raw_input("Enter table name")
valuevariable = raw_input("Enter Array Values Variable")
cursor = conn.cursor()
cursor.execute("desc " + tablename)

# $McQ->registration_id = $request->input('registration_id');
person = raw_input("Enter you variable name")
print("<table>")
for (table_name) in cursor:   
  
    print('<tr><td>' + table_name[0] + '<td><?php echo $' + str(person) +'->' + table_name[0] + ";?></td></tr>")
    cursor.close

 