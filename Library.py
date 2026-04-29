import mysql.connector as MyDBConnection
from mysql.connector import Error
def connect():
    conn = None
    try:
        conn = MyDBConnection.connect(database="userdb", user="root", password='Yellowstone#2026$')
        print("Connected to MySQL database")
        query = "SELECT * FROM laptop"
        cursor = conn.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        for line in records:
            print(line)
    except Error as e:
        print('ERROR', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    connect()
