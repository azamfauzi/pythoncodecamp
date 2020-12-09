
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def connect():
    """ Connect to MySQL database """
 
    db_config = read_db_config()
 
    try:
        print('Connecting to MySQL databasess...')
        conn = MySQLConnection(db_config)
        if conn.is_connected():
            print('connection establissshed.')
            cursor = conn.cursor()
            cursor.execute("desc patients")
            
            for (table_name) in cursor:
                print("$request->input('" + table_name[0] + "')")
            cursor.close

        else:
            print('connection failed.')
 
    except Error as error:
        print(error)
 
    finally:
        conn.close()
        print('Connection closed.')
def generateVariableFromInput():
    print('Setting Tox X')
    db_config = read_db_config()    	 
    try:
        print('Connecting to MySQL database...')
        text = input("Select table name")
        conn = MySQLConnection(db_config) 
        if conn.is_connected():
            print('connection establishe')
            cursor = conn.cursor()
            cursor.execute("desc patients")            
            for (table_name) in cursor:
                print("$request->input('" + table_name[0] + "')")
            cursor.close

        else:
            print('connection failed.')
    except Error as error:
        print(error)
 
    finally:
        conn.close()
        print('Connection closed.') 	
if __name__ == '__main__':    
	connect()


        


