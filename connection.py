import mysql.connector
from mysql.connector import Error

class DBConnection:
    def __init__(self):
        self.db_config = {
            'user': 'root',
            'password': '',
            'host': 'localhost',
            'database': 'agencia_alquiler',
            'port': 3306
        }
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            return True, "Conexión establecida exitosamente."
        except Error as e:
            return False, str(e)

    def obtener_cursor(self):
        if self.connection and self.connection.is_connected():
            return self.connection.cursor()
        return None

    def commit(self):
        if self.connection and self.connection.is_connected():
            self.connection.commit()

    def cerrar(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()