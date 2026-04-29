import mysql.connector as MyDBConnection
from mysql.connector import Error
def connection():
    conn=None
    try:
        conn=MyDBConnection.connect(database="userdb", user="root", password="Yellowstone#2026$")
        print("Connected to MySQL database")

        cursor = conn.cursor()

        myquery = (
            "INSERT INTO laptop (Id, Name, Price, Purchase_Date) "
            "VALUES (1, 'Dell XPS 13', 999.99, '2024-01-15')"
        )
        cursor.execute(myquery)
        conn.commit()
        print("Data inserted successfully")
        cursor.close()
    except Error as e:
        print(f"ERROR: {e}")
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    connection()
