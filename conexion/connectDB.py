import mysql.connector
from mysql.connector import Error
class ConectarDB:
    def conectar():
        try:
            conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ecotechsolutions",
            )
            if conexion.is_connected():
                return conexion
        except Error:
            return f"Error"