# database.py

import psycopg2
from psycopg2 import sql

def conectar_base_datos():
    """
    Conecta a la base de datos PostgreSQL y realiza una consulta.
    """
    conexion = None
    try:
        # Establecer conexión con la base de datos
        conexion = psycopg2.connect(
            database="tu_base_datos",
            user="tu_usuario",
            password="tu_contraseña",
            host="tu_host",
            port="tu_puerto"
        )
        with conexion.cursor() as cursor:
            # Ejecutar una consulta SQL
            cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier('usuarios')))
            resultados = cursor.fetchall()
            for resultado in resultados:
                print(resultado)
    except psycopg2.DatabaseError as e:
        print(f"Error en la conexión a la base de datos: {e}")
    finally:
        if conexion:
            conexion.close()
            print("Conexión cerrada.")

# Ejemplo de uso
if __name__ == "__main__":
    conectar_base_datos()
