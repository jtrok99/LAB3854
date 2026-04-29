import mysql.connector as MyDBConnection
from mysql.connector import Error

def connect():
    conn = None
    try:
        conn = MyDBConnection.connect(database="userdb", user="root", password="Yellowstone#2026$")
        print("Connected to MySQL database")

        cursor = conn.cursor()
        myquery = (
            "CREATE TABLE laptop ("
            "Id int(11) NOT NULL, "
            "Name varchar(250) NOT NULL, "
            "Price float NOT NULL, "
            "Purchase_Date date NOT NULL)"
        )
        cursor.execute(myquery)
        print("Table created successfully")
    except Error as e:
        print(f"ERROR: {e}")
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("MySQL connection closed")


if __name__ == "__main__":
    connect()
