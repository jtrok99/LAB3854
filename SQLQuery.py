import mysql.connector as MyDBConnection
from mysql.connector import Error
def connect():
    conn=None
    try:
        conn=MyDBConnection.connect(database="userdb", user="root", password='Yellowstone#2026$')
        print("Connected to MySQL database")
        mysql_insert_query = """ INSERT INTO Laptop (Id, Name, Price, Purchase_Date)
        VALUES (%s, %s, %s, %s)"""
        record_to_insert = [(4, 'HP Pavilion Power', 1999, '2019-01-11'), (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
                            (6, 'Microsoft Surface', 2330, '2019-07-23')]
        cursor = conn.cursor()
        cursor.executemany(mysql_insert_query, record_to_insert)
        conn.commit()
        print(f"{cursor.rowcount}: Records inserted successfully")
    except Error as e:
        print(f"ERROR: {e}")
    finally:
        if conn is not None and conn.is_connected():            
            conn.close()
            print("MySQL connection is closed")
if __name__ == "__main__":    connect()
