import mysql.connector

def get_db_connection():
    """
    Returns a MySQL database connection.
    All credentials are hidden for security.
    """
    connection = mysql.connector.connect(
        host="YOUR_HOST_HERE",
        user="YOUR_USER_HERE",
        password="YOUR_PASSWORD_HERE",
        database="YOUR_DATABASE_HERE",
        port="YOUR_PORT_HERE"
    )
    return connection