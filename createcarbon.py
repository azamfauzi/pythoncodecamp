import pymysql
from python_mysql_dbconfig import read_db_config
conn = pymysql.connect(host='localhost',user='root',password='abc123',db='devclinic')
tablename = raw_input("Enter table name")
cursor = conn.cursor()
cursor.execute("desc " + tablename)
# $McQ->registration_id = $request->input('registration_id');
# date assign
person = raw_input("Enter you variable name for ex: qPatient")


for (table_name) in cursor:
    
    print("$dateString" + str(table_name[0]) + " = $request->input('" + table_name[0] + "');")
    print("$dateObject" + str(table_name[0]) + " = Carbon::createFromFormat('d-m-Y', $dateString" + str(table_name) + ")->format('Y-m-d');")    
    cursor.close

