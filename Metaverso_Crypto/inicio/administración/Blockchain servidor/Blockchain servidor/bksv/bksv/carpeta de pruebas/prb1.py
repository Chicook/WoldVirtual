from vpython import *
from prb2 import create_scene
from prb3 import create_structure
from prb4 import create_sphere
from prb5 import animate_sphere

# Crear la escena
scene = create_scene()

# Crear la estructura de la estación espacial
structure = create_structure()

# Crear la esfera animada
sphere = create_sphere()

# Animar la esfera
animate_sphere(sphere)
