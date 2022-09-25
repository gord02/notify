import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_passwd, dm_name):
    connection = None
    
    try:
        connection = mysql.connector.connect(host=host_name,
                                             user=user_name,
                                             passwd=user_passwd,
                                              database=dm_name
                                            )
        print("connection to MySql DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        print("database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

       
connection = create_connection("localhost", "root", "", "checkon")   
db_query = "CREATE DATABASE checkon"
table_create = """
CREATE TABLE IF NOT EXISTS companies (
    company TEXT,
    fileName TEXT,
    found INT
)
"""
add_companies = """
INSERT INTO companies(company, fileName, found)
    VALUES 
    ("Snapchat", "snap.py", 0),
    ("Addepar", "addepar.py", 0),
    ("Quora", "quora.py", 0),
    ("twoSigma", "twoSigma.py", 0),
    ("Yelp", "yelp.py", 0);
"""
# create_database(connection, db_query)
execute_query(connection, add_companies)
