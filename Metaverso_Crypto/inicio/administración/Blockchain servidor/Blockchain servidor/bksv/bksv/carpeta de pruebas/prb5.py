from vpython import rate, pi, vec

def animate_sphere(sphere):
    def animation():
        rate(30)
        sphere.rotate(angle=pi/180, axis=vec(1, 0, 0))
        if scene.current_time < 70:
            scene.after(animation)
    
    animation()
