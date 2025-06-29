# MySQLServer.py
import mysql.connector
from mysql.connector import errorcode

try:
    # Attempt to connect to MySQL server (adjust user/password if needed)
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='KikiJay@2002'
    )

    cursor = cnx.cursor()

    # Try to create the database
    create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    cursor.execute(create_db_query)
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close resources
    if 'cursor' in locals():
        cursor.close()
    if 'cnx' in locals() and cnx.is_connected():
        cnx.close()
