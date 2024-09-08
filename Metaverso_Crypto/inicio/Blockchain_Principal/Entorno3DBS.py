from vpython import *

# Crear la escena
scene = canvas(title='Estación Espacial', width=800, height=600)

# Crear la estructura de la estación espacial
radius = 10
num_spaces = 6
space_width = 2

structure = []
for i in range(num_spaces):
    theta = i * 2*pi/num_spaces
    x = radius*cos(theta)
    y = radius*sin(theta)
    space = cylinder(pos=vec(x, y, 0), axis=vec(0, 0, space_width), radius=space_width/2)
    structure.append(space)

# Crear la esfera animada
sphere_pos = vec(0, 0, 0)
sphere = sphere(pos=sphere_pos, radius=1, color=color.red)

def animate_sphere():
    rate(30)
    sphere.rotate(angle=pi/180, axis=vec(1, 0, 0))
    if scene.current_time < 70:
        scene.after(animate_sphere)

# Animar la esfera
animate_sphere()
