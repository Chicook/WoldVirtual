from vpython import vec, sphere, color

def create_sphere():
    sphere_pos = vec(0, 0, 0)
    return sphere(pos=sphere_pos, radius=1, color=color.red)
    
