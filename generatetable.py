import pymysql
from python_mysql_dbconfig import read_db_config
conn = pymysql.connect(host='localhost',user='root',password='abc123',db='devclinic')

cursor = conn.cursor()
cursor.execute("show tables")
# $McQ->registration_id = $request->input('registration_id');


i = 0
for (table_name) in cursor:
    i = i  + 1
    print(str(i) + " " + table_name[0])
    cursor.close

