# modulo de database #

import psycopg2
from psycopg2 import sql

def conectar_base_datos():
    """
    Establece una conexión con la base de datos PostgreSQL.

    Returns:
        conexion: Objeto de conexión a la base de datos.
    """
    try:
        conexion = psycopg2.connect(
            database="tu_base_datos",
            user="tu_usuario",
            password="tu_contraseña",
            host="tu_host",
            port="tu_puerto"
        )
        print("Conexión a la base de datos establecida.")
        return conexion
    except psycopg2.DatabaseError as e:
        print(f"Error en la conexión a la base de datos: {e}")
        return None

def insertar_bloque(conexion, bloque):
    """
    Inserta un bloque en la base de datos.

    Args:
        conexion: Objeto de conexión a la base de datos.
        bloque: Objeto Bloque a insertar.
    """
    try:
        with conexion.cursor() as cursor:
            query = sql.SQL("INSERT INTO bloques (index, timestamp, datos, hash, hash_anterior) VALUES (%s, %s, %s, %s, %s)")
            cursor.execute(query, (bloque.index, bloque.timestamp, bloque.datos, bloque.hash, bloque.hash_anterior))
            conexion.commit()
            print(f"Bloque {bloque.index} insertado en la base de datos.")
    except psycopg2.DatabaseError as e:
        print(f"Error al insertar el bloque: {e}")
        conexion.rollback()

def obtener_bloques(conexion):
    """
    Recupera todos los bloques de la base de datos.

    Args:
        conexion: Objeto de conexión a la base de datos.

    Returns:
        list: Lista de bloques.
    """
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM bloques")
            bloques = cursor.fetchall()
            return bloques
    except psycopg2.DatabaseError as e:
        print(f"Error al obtener los bloques: {e}")
        return []

def insertar_transaccion(conexion, remitente, destinatario, cantidad):
    """
    Inserta una transacción en la base de datos.

    Args:
        conexion: Objeto de conexión a la base de datos.
        remitente (str): Nombre del remitente.
        destinatario (str): Nombre del destinatario.
        cantidad (float): Cantidad de la transacción.
    """
    try:
        with conexion.cursor() as cursor:
            query = sql.SQL("INSERT INTO transacciones (remitente, destinatario, cantidad) VALUES (%s, %s, %s)")
            cursor.execute(query, (remitente, destinatario, cantidad))
            conexion.commit()
            print("Transacción insertada en la base de datos.")
    except psycopg2.DatabaseError as e:
        print(f"Error al insertar la transacción: {e}")
        conexion.rollback()

def obtener_transacciones(conexion):
    """
    Recupera todas las transacciones de la base de datos.

    Args:
        conexion: Objeto de conexión a la base de datos.

    Returns:
        list: Lista de transacciones.
    """
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM transacciones")
            transacciones = cursor.fetchall()
            return transacciones
    except psycopg2.DatabaseError as e:
        print(f"Error al obtener las transacciones: {e}")
        return []

def cerrar_conexion(conexion):
    """
    Cierra la conexión con la base de datos.

    Args:
        conexion: Objeto de conexión a la base de datos.
    """
    if conexion:
        conexion.close()
        print("Conexión con la base de datos cerrada.")

# Ejemplo de uso
if __name__ == "__main__":
    conexion = conectar_base_datos()
    if conexion:
        # Crear instancia de la blockchain
        blockchain = Blockchain()

        # Procesar una transacción y agregar un bloque
        remitente = "Usuario1"
        destinatario = "Usuario2"
        cantidad = 150.0

        # Agregar bloque a la blockchain
        nuevo_bloque = blockchain.agregar_bloque(f"Transacción de {remitente} a {destinatario} por {cantidad} unidades")

        # Insertar el bloque y la transacción en la base de datos
        insertar_bloque(conexion, nuevo_bloque)
        insertar_transaccion(conexion, remitente, destinatario, cantidad)

        # Obtener bloques almacenados
        bloques = obtener_bloques(conexion)
        print("Bloques en la base de datos:")
        for bloque in bloques:
            print(bloque)

        # Obtener transacciones almacenadas
        transacciones = obtener_transacciones(conexion)
        print("Transacciones en la base de datos:")
        for transaccion in transacciones:
            print(transaccion)

        # Cerrar conexión
        cerrar_conexion(conexion)
