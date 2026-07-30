from connection import DBConnection
from mysql.connector import Error

class DatabaseManager:
    def __init__(self):
        # Instancia el gestor de conexión
        self.db_conn = DBConnection()

    def inicializar_conexion(self):
        """Inicia el proceso de conexión a la base de datos."""
        return self.db_conn.conectar()

    def obtener_vehiculos(self):
        """Ejecuta la consulta SELECT para obtener la flota."""
        cursor = self.db_conn.obtener_cursor()
        query = "SELECT ID, Marca, Modelo, Año, Combustible, Disponible FROM Vehiculos"
        cursor.execute(query)
        registros = cursor.fetchall()
        cursor.close()
        return registros

    def agregar_vehiculo(self, marca, modelo, anio, combustible, disponible):
        """Ejecuta la sentencia INSERT para agregar un nuevo registro."""
        cursor = self.db_conn.obtener_cursor()
        query = "INSERT INTO Vehiculos (Marca, Modelo, Año, Combustible, Disponible) VALUES (%s, %s, %s, %s, %s)"
        values = (marca, modelo, int(anio), combustible, disponible)
        cursor.execute(query, values)
        self.db_conn.commit()
        cursor.close()

    def actualizar_vehiculo(self, vehiculo_id, marca, modelo, anio, combustible, disponible):
        """Ejecuta la sentencia UPDATE para modificar un registro existente."""
        cursor = self.db_conn.obtener_cursor()
        query = "UPDATE Vehiculos SET Marca = %s, Modelo = %s, Año = %s, Combustible = %s, Disponible = %s WHERE ID = %s"
        values = (marca, modelo, int(anio), combustible, disponible, int(vehiculo_id))
        cursor.execute(query, values)
        self.db_conn.commit()
        cursor.close()

    def borrar_vehiculo(self, vehiculo_id):
        """Ejecuta la sentencia DELETE para remover un vehículo por su ID."""
        cursor = self.db_conn.obtener_cursor()
        query = "DELETE FROM Vehiculos WHERE ID = %s"
        cursor.execute(query, (int(vehiculo_id),))
        self.db_conn.commit()
        cursor.close()

    def obtener_metricas_informe(self):
        """Realiza consultas de conteo para generar métricas del sistema."""
        cursor = self.db_conn.obtener_cursor()
        
        cursor.execute("SELECT COUNT(*) FROM Vehiculos WHERE Disponible = TRUE")
        disponibles = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM Vehiculos WHERE Disponible = FALSE")
        mantenimiento = cursor.fetchone()[0]
        
        cursor.close()
        return disponibles, mantenimiento

    def cerrar(self):
        self.db_conn.cerrar()