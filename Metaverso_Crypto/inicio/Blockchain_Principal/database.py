









# modulo database #

# import psycopg2
# from psycopg2 import sql

# def conectar_base_datos():
   #  """
  #  Conecta a la base de datos PostgreSQL y devuelve la conexión.

 #   Returns:
       # conexion: Objeto de conexión a la base de datos.
   # """
  #  try:
       # conexion = psycopg2.connect(
           # database="tu_base_datos",
           # user="tu_usuario",
         #   password="tu_contraseña",
           # host="tu_host",
          #  port="tu_puerto"
      #  )
      #  print("Conexión a la base de datos establecida.")
       # return conexion
  #  except psycopg2.DatabaseError as e:
       # print(f"Error en la conexión a la base de datos: {e}")
        # return None

# def obtener_usuarios(conexion):
   # """
   # Obtiene todos los usuarios de la base de datos.

   # Args:
       # conexion: Objeto de conexión a la base de datos.

 #   Returns:
       # list: Lista de usuarios.
  #  """
    # try:
       # with conexion.cursor() as cursor:
          #  cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier('usuarios')))
           # resultados = cursor.fetchall()
          #  return resultados
  #  except psycopg2.DatabaseError as e:
       # print(f"Error al obtener usuarios: {e}")
      #  return []

# def cerrar_conexion(conexion):
   # """
  #  Cierra la conexión a la base de datos.

  #  Args:
      #  conexion: Objeto de conexión a la base de datos.
  #  """
    # if conexion:
      #  conexion.close()
     #   print("Conexión cerrada.")

# Ejemplo de uso
# if __name__ == "__main__":
  #  conexion = conectar_base_datos()
  #  if conexion:
     #   usuarios = obtener_usuarios(conexion)
    #    for usuario in usuarios:
         #   print(usuario)
      #  cerrar_conexion(conexion)

# database.py

# import psycopg2
# from psycopg2 import sql

# def conectar_base_datos():
   #  conexion = None
   # try:
       # conexion = psycopg2.connect(
        # database="tu_base_datos",
          #  user="tu_usuario",
          #  password="tu_contraseña",
          #  host="tu_host",
           # port="tu_puerto"
      #  )
       # with conexion.cursor() as cursor:
           # cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier('usuarios')))
           # resultados = cursor.fetchall()
            # for resultado in resultados:
             #   print(resultado)
  #  except psycopg2.DatabaseError as e:
       # print(f"Error en la conexión a la base de datos: {e}")
   # finally:
      #  if conexion:
           # conexion.close()
           # print("Conexión cerrada.")
