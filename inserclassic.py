import pymysql
from python_mysql_dbconfig import read_db_config
conn = pymysql.connect(host='localhost',user='root',password='abc123',db='eml')
tablename = raw_input("Enter table name")
cursor = conn.cursor()
cursor.execute("desc " + tablename)
# $McQ->registration_id = $request->input('registration_id');
#person = raw_input("Enter you variable name")
#classname = raw_input("Enter class name  : ")
#print("$" + str(person) + "= new " + str(classname))   
str_insert = 'INSERT INTO ' +  tablename + ' '
str_field = '('
str_value = ' VALUES ('

begin = True
for (table_name) in cursor:   
    if begin == True :
        str_field = str_field + table_name[0]
        str_value = str_value + '" . $_POST["' + table_name[0] + '"]'
        print('" . $_POST["' + table_name[0] + '"] . "\'"')

        begin = False
    elif begin == False :
        str_field = str_field + "," + table_name[0]
        str_value = str_value + ". ','" + ' . $_POST["' + table_name[0] + '"]'
        print('" . $_POST["' + table_name[0] + '"] . "\'"')
   # print("$" + str(person) + "->" + table_name[0] + " = $request->input('" + table_name[0] + "');")
    cursor.close    

str_field = str_field + ")"
str_value = str_value + ")"
#print(str(str_field))
#print(str(str_value))
print("/n")
print("/n")
print("/n")
#print(str_insert + str_field + str_value)



