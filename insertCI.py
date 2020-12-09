import pymysql
from python_mysql_dbconfig import read_db_config
conn = pymysql.connect(host='localhost',user='root',password='abc123',db='qprinter')
tablename = raw_input("Enter table name")
valuevariable = raw_input("Enter Array Values Variable")
cursor = conn.cursor()
cursor.execute("desc " + tablename)

# $McQ->registration_id = $request->input('registration_id');
begin = 0
person = raw_input("Enter you variable name")
for (table_name) in cursor:   
    if begin == 0:
        primary_key = table_name[0]
        begin = 1
    print("$" + str(person) + "_" + table_name[0] + " = $this->input->post('" + table_name[0] + "');")
    cursor.close   

cursor = conn.cursor()
cursor.execute("desc " + tablename)
for (table_name) in cursor:   
  
    print('$' + str(valuevariable) + '["' + table_name[0] + '"] = $' + str(person) + '_' + table_name[0] + ';')
    cursor.close   

print('<!-- insert update file -->')
print('if($' + str(person) + '_' + primary_key + ' > 0 ){')
print('  $this->db->where(\'' + primary_key + '\',$' + person + '_' + primary_key + ');')
print('  $this->db->update(\'' + tablename + '\');')
print('}else{')
print('  $this->db->insert(\'' + tablename + '\',$' + valuevariable + ');')
print('}')
print('')
print('')
print('')
print('')

print('<!-- remove update file -->')
print('  $this->db->where(\'' + primary_key + '\',$' + person + '_' + primary_key + ');')
print('  $this->db->delete(\'' + tablename + '\');')

cursor = conn.cursor()
cursor.execute("desc " + tablename)
for (table_name) in cursor:
    print('$("#' + table_name[0] + '").html(data.' + table_name[0] + ');')
    cursor.close

cursor = conn.cursor()
cursor.execute("desc " + tablename)
for (table_name) in cursor:
    print('var ' + table_name[0] + ' = $("#' + table_name[0] + '").val();')
    cursor.close

cursor = conn.cursor()
cursor.execute("desc " + tablename)
for (table_name) in cursor:
    print('"' + table_name[0] + '" :' + table_name[0] + ',')
    cursor.close

cursor = conn.cursor()
cursor.execute("desc " + tablename)
for (table_name) in cursor:
    print('$("#' + table_name[0] + person + ').html(data.' + table_name[0] + ');')
    cursor.close    



