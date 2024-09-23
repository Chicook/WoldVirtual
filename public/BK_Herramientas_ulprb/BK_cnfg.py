"""
Este código 
es de ejemplo.

import sys
import os

# Añadir las rutas de los módulos al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulo1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulo2')))

# Importar las funciones de los módulos
from modulo1 import funcion_init_modulo1
from modulo2 import funcion_init_modulo2

# Usar las funciones importadas
funcion_init_modulo1()
funcion_init_modulo2()
"""
