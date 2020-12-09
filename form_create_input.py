import pymysql
from python_mysql_dbconfig import read_db_config
conn = pymysql.connect(host='localhost',user='root',password='abc123',db='helpdeskassetnew')
tablename = raw_input("Enter table name")
cursor = conn.cursor()
cursor.execute("desc " + tablename)

# $McQ->registration_id = $request->input('registration_id');
person = raw_input("Enter you variable name (recordset")

print("-------------------------------------------------------")
for (table_name) in cursor:
    #print("$" + str(p
    #print("")rson) + "->" + table_name[0] + " = $request->input('" + table_name[0] + "')")
    print('<div class="form-group">')
    print('     <label class="col-md-2 control-label">' + table_name[0] +  '</label>')
    print('         <div class="col-md-5">')
    print('            <input class="form-control" placeholder="' + table_name[0] + '" type="text" name="' + table_name[0] + '">')
    print('         </div>')
    print('</div>')
    
    cursor.close
print("")
print("")    
print("-------------------------------------------------------")


print("-------------------------------------------------------")
cursor.execute("desc " + tablename)
for (table_name) in cursor:
    #print("$" + str(p
    #print("")rson) + "->" + table_name[0] + " = $request->input('" + table_name[0] + "')")
    print('<div class="form-group">')
    print('     <label class="col-md-2 control-label">' + table_name[0] +  '</label>')
    print('         <div class="col-md-5">')
    print('            <input class="form-control" placeholder="' + table_name[0] + '" type="text" name="' + table_name[0] + '" value="<?php if(isset($' + person + ')){ echo ' + person + "->" + table_name[0] + ';}?>">')
    print('         </div>')
    print('</div>')    
    cursor.close
print("")
print("")    
print("-------------------------------------------------------")