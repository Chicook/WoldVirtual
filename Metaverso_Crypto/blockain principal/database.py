import psycopg2

def conectar_base_datos():
    try:
    conexion = psycopg2.connect(
    database="tu_base_datos",
        user="tu_usuario",
    password="tu_contraseña",
        host="tu_host",
        port="tu_puerto"
                                                                                )
        with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        for resultado in resultados:
        print(resultado)
        except Exception as e:
        print(f"Error en la conexión a la base de datos: {e}")
        finally:
        if conexion:
        conexion.close()
