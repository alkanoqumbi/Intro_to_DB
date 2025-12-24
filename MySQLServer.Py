import mysql.connector 

def create_database():
    try:
        # Connect to MySQL server
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="4242@Wako" 
        )
        cursor = mydb.cursor()

        # Create database without using SELECT or SHOW
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            cursor.close()
            mydb.close()

if __name__ == "_main_":
    create_database()