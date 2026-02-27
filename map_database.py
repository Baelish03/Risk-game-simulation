import os
import mysql.connector
from dotenv import load_dotenv

class Database:
    def __init__(self):
        load_dotenv()
        credentials = [os.getenv("DB_HOST"), os.getenv("DB_USER"), os.getenv("DB_PASSWORD")]
        mysql_login = self.login_mysql(credentials)
        db_name = "world"
        self.create_db(mysql_login, db_name)
        mysql_login = self.login_db(credentials, db_name)
        table_names = [["countries", ["country", "VARCHAR(256)"],
                                     ["neighbors", "MEDIUMTEXT"],
                                     ["continent_id", "INT"]], 
                       ["continents", ["continent", "VARCHAR(16)"],
                                      ["color", "VARCHAR(7)"],
                                      ["continent_id", "INT"]
                        ]]
        for name in table_names:
            self.create_table(mysql_login, name)



    

    def login_mysql(self, credentials):
        """
        Enter in mysql.
        """
        try:
            mysql_login = mysql.connector.connect(
                host=credentials[0],
                user=credentials[1],
                password=credentials[2],
            )
            print("Secure connection to mysql")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        return mysql_login

    def create_db(self, login, db_name):
        cursor = login.cursor()
        try:
            cursor.execute("CREATE DATABASE " + db_name)
            print("Database " + db_name + " created")            
        except mysql.connector.Error as err:
            if err.errno == 1007:
                print ("Warning: database " + db_name + " already exists")
            else:
                print(f"Error: {err}")
        return None
    
    def login_db(self, credentials, db_name):
        try:
            mysql_login = mysql.connector.connect(
                host=credentials[0],
                user=credentials[1],
                password=credentials[2],
                database=db_name
            )
            print("Secure connection to mysql. Now you are in " + db_name + " database")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        return mysql_login
    
    def create_table(self, database, table_name):
        cursor = database.cursor()
        try:
            cursor.execute("CREATE TABLE " + table_name)
            print("Table " + table_name + " created")            
        except mysql.connector.Error as err:
            if err.errno == 1007:
                print ("Warning: table " + table_name + " already exists")
            else:
                print(f"Error: {err}")
        return None
            
 

db = Database()
