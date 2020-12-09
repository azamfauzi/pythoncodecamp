import pymysql
from python_mysql_dbconfig import read_db_config
conn = pymysql.connect(host='localhost',user='root',password='abc123',db='helpdeskassetnew')
tablename = raw_input("Enter table name")
cursor = conn.cursor()
cursor.execute("desc " + tablename)
# $McQ->registration_id = $request->input('registration_id');
person = raw_input("Enter you variable name")


for (table_name) in cursor:
    print("<?php if(isset($" + str(person) + "->" + table_name[0] + ")) { echo $" + str(person) + "->" + table_name[0] + ";}?>")
    cursor.close


