from sqlite3 import connect

import mysql.connector as MyDBConnection
from mysql.connector import Error
def connection():
    conn=None
    try:
        conn=MyDBConnection.connect(database="classicmodels", user="root", password="Yellowstone#2026$")
        if conn.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"ERROR: {e}")
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("MySQL connection closed")
if __name__ == "__main__":    
    connection() 