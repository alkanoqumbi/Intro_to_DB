import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Using the username 'root' found in your shell image
        # If you set a password during installation, enter it in 'password'
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='4242@Wako' 
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # This creates the DB if it doesn't exist without using SELECT/SHOW
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Prints error message if connection fails
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Handles closing the database connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "_main_":
    create_database()