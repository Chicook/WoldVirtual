# modulo recursos #

class RecursosUsuario:
    def __init__(self, porcentaje_cpu, porcentaje_ancho_banda):
        self.porcentaje_cpu = porcentaje_cpu
        self.porcentaje_ancho_banda = porcentaje_ancho_banda

    def asignar_recursos(self, recursos_comunitarios):
        """
        Asigna recursos a un usuario basado en los recursos comunitarios.

        Args:
            recursos_comunitarios (dict): Recursos disponibles en la comunidad.

        Returns:
            dict: Recursos asignados al usuario.
        """
        return {
            'cpu': recursos_comunitarios['cpu'] * (self.porcentaje_cpu / 100),
            'ancho_banda': recursos_comunitarios['ancho_banda'] * (self.porcentaje_ancho_banda / 100),
        }

    def ajustar_recursos(self, nuevo_porcentaje_cpu, nuevo_porcentaje_ancho_banda):
        """
        Ajusta los recursos asignados al usuario.

        Args:
            nuevo_porcentaje_cpu (int): Nuevo porcentaje de CPU asignado.
            nuevo_porcentaje_ancho_banda (int): Nuevo porcentaje de ancho de banda asignado.
        """
        self.porcentaje_cpu = nuevo_porcentaje_cpu
        self.porcentaje_ancho_banda = nuevo_porcentaje_ancho_banda
        print(f"Recursos ajustados: CPU {self.porcentaje_cpu}%, Ancho de Banda {self.porcentaje_ancho_banda}%")

class MonitoreoRecursos:
    def __init__(self):
        self.recursos_usuarios = {}

    def actualizar_recursos(self, nombre_usuario, uso_cpu, uso_ancho_banda):
        """
        Actualiza el uso de recursos de un usuario.

        Args:
            nombre_usuario (str): Nombre del usuario.
            uso_cpu (float): Porcentaje de uso de CPU.
            uso_ancho_banda (float): Porcentaje de uso de ancho de banda.
        """
        self.recursos_usuarios[nombre_usuario] = {
            'uso_cpu': uso_cpu,
            'uso_ancho_banda': uso_ancho_banda
        }

    def obtener_informacion(self):
        """
        Obtiene la información de uso de recursos de todos los usuarios.

        Returns:
            dict: Información de uso de recursos.
        """
        return self.recursos_usuarios

    def eliminar_usuario(self, nombre_usuario):
        """
        Elimina la información de recursos de un usuario.

        Args:
            nombre_usuario (str): Nombre del usuario a eliminar.
        """
        if nombre_usuario in self.recursos_usuarios:
            del self.recursos_usuarios[nombre_usuario]
            print(f"Usuario {nombre_usuario} eliminado del monitoreo de recursos.")
        else:
            print(f"Usuario {nombre_usuario} no encontrado.")

    @staticmethod
    def inicializar():
        """
        Inicializa los recursos.
        """
        print("Recursos inicializados")

# Ejemplo de uso
if __name__ == "__main__":
    recursos_comunitarios = {'cpu': 100, 'ancho_banda': 1000}
    usuario = RecursosUsuario(50, 50)
    recursos_asignados = usuario.asignar_recursos(recursos_comunitarios)
    print(f"Recursos asignados: {recursos_asignados}")

    usuario.ajustar_recursos(60, 70)

    monitoreo = MonitoreoRecursos()
    monitoreo.actualizar_recursos("usuario1", 30, 200)
    print(f"Información de recursos: {monitoreo.obtener_informacion()}")
    monitoreo.eliminar_usuario("usuario1")
    print(f"Información de recursos después de eliminar: {monitoreo.obtener_informacion()}")
    MonitoreoRecursos.inicializar()

# modulo recursos #

# class RecursosUsuario:
   #  def __init__(self, porcentaje_cpu, porcentaje_ancho_banda):
      #  self.porcentaje_cpu = porcentaje_cpu
       # self.porcentaje_ancho_banda = porcentaje_ancho_banda

   # def asignar_recursos(self, recursos_comunitarios):
      #  """
      #  Asigna recursos a un usuario basado en los recursos comunitarios.

      #  Args:
          #  recursos_comunitarios (dict): Recursos disponibles en la comunidad.

     #   Returns:
          #  dict: Recursos asignados al usuario.
     #   """
      #  return {
           # 'cpu': recursos_comunitarios['cpu'] * (self.porcentaje_cpu / 100),
           # 'ancho_banda': recursos_comunitarios['ancho_banda'] * (self.porcentaje_ancho_banda / 100),
     #   }

# class MonitoreoRecursos:
  #  def __init__(self):
       # self.recursos_usuarios = {}

  #  def actualizar_recursos(self, nombre_usuario, uso_cpu, uso_ancho_banda):
       # """
       # Actualiza el uso de recursos de un usuario.

      #  Args:
           # nombre_usuario (str): Nombre del usuario.
         #   uso_cpu (float): Porcentaje de uso de CPU.
          #  uso_ancho_banda (float): Porcentaje de uso de ancho de banda.
       # """
        # self.recursos_usuarios[nombre_usuario] = {
          #  'uso_cpu': uso_cpu,
          #  'uso_ancho_banda': uso_ancho_banda
      #  }

   # def obtener_informacion(self):
      #  """
      #  Obtiene la información de uso de recursos de todos los usuarios.

      #  Returns:
          #  dict: Información de uso de recursos.
       # """
      #  return self.recursos_usuarios

   # @staticmethod
  #  def inicializar():
       # """
      #  Inicializa los recursos.
       # """
       # print("Recursos inicializados")

# Ejemplo de uso
# if __name__ == "__main__":
  #  recursos_comunitarios = {'cpu': 100, 'ancho_banda': 1000}
   # usuario = RecursosUsuario(50, 50)
   # recursos_asignados = usuario.asignar_recursos(recursos_comunitarios)
   # print(f"Recursos asignados: {recursos_asignados}")

  #  monitoreo = MonitoreoRecursos()
   # monitoreo.actualizar_recursos("usuario1", 30, 200)
  #  print(f"Información de recursos: {monitoreo.obtener_informacion()}")
  #  MonitoreoRecursos.inicializar()

# recursos.py

# class RecursosUsuario:
   # def __init__(self, porcentaje_cpu, porcentaje_ancho_banda):
       # self.porcentaje_cpu = porcentaje_cpu
      #  self.porcentaje_ancho_banda = porcentaje_ancho_banda

  #  @staticmethod
   # def asignar_recursos_a_usuario(usuario, recursos_comunitarios):
      #  return {
          #  'cpu': recursos_comunitarios['cpu'] * (usuario.porcentaje_cpu / 100),
           # 'ancho_banda': recursos_comunitarios['ancho_banda'] * (usuario.porcentaje_ancho_banda / 100),
     #   }

# class MonitoreoRecursos:
  #  def __init__(self):
       # self.recursos_usuarios = {}

   # def actualizar_recursos(self, nombre_usuario, uso_cpu, uso_ancho_banda):
        # self.recursos_usuarios[nombre_usuario] = {
           # 'uso_cpu': uso_cpu,
           # 'uso_ancho_banda': uso_ancho_banda
      #  }

 #   def obtener_informacion(self):
       # return self.recursos_usuarios

  #  @staticmethod
   # def inicializar():
       # print("Recursos inicializados")
    
