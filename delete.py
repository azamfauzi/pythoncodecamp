import pymysql
from python_mysql_dbconfig import read_db_config
# $McQ->registration_id = $request->input('registration_id');
modelVar = raw_input("Model Name")
variabelName = raw_input("Enter Variable Name")
print("-------------------------------------------------------")
print("")
print("$" + variabelName +  "= " + modelVar + "::find($id);")
print("$" + variabelName + "->delete()")
print("")
print("")
print("-------------------------------------------------------")


