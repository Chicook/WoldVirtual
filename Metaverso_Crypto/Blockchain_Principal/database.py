import psycopg2
from psycopg2 import sql

def conectar_base_datos():
    """
    Conecta a la base de datos PostgreSQL y obtiene todos los registros de la tabla 'usuarios'.
    """
    conexion = None
    try:
        conexion = psycopg2.connect(
            database="tu_base_datos",
            user="tu_usuario",
            password="tu_contraseña",
            host="tu_host",
            port="tu_puerto"
        )
        with conexion.cursor() as cursor:
            cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier('usuarios')))
            resultados = cursor.fetchall()
            for resultado in resultados:
                print(resultado)
    except Exception as e:
        print(f"Error en la conexión a la base de datos: {e}")
    finally:
        if conexion:
            conexion.close()
            print("Conexión cerrada.")

# Llamada a la función para probar la conexión
conectar_base_datos()

# import psycopg2

# def conectar_base_datos():
   # try:
   # conexion = psycopg2.connect(
   # database="tu_base_datos",
    #    user="tu_usuario",
   # password="tu_contraseña",
      #  host="tu_host",
       # port="tu_puerto"
                                                                                )
       # with conexion.cursor() as cursor:
       # cursor.execute("SELECT * FROM usuarios")
      #  resultados = cursor.fetchall()
      #  for resultado in resultados:
      #  print(resultado)
       # except Exception as e:
      #  print(f"Error en la conexión a la base de datos: {e}")
       # finally:
      #  if conexion:
       # conexion.close()
