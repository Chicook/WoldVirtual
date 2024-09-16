



import bpy

def crear_planeta():
    # Crear el planeta
    bpy.ops.mesh.primitive_uv_sphere_add(radius=2, location=(0, 0, 0))
    planeta = bpy.context.object
    planeta.name = "Planeta"

    # Aplicar textura azul para simular el mar
    material_mar = bpy.data.materials.new(name="Mar_Material")
    material_mar.use_nodes = True
    bsdf_mar = material_mar.node_tree.nodes["Principled BSDF"]
    bsdf_mar.inputs['Base Color'].default_value = (0, 0, 1, 1)  # Azul
    planeta.data.materials.append(material_mar)

    # Añadir casquetes polares básicos
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0, 0, 2.5))
    casquete_norte = bpy.context.object
    casquete_norte.name = "Casquete_Norte"
    casquete_norte.data.materials.append(material_mar)

    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0, 0, -2.5))
    casquete_sur = bpy.context.object
    casquete_sur.name = "Casquete_Sur"
    casquete_sur.data.materials.append(material_mar)

    # Crear la capa de ozono
    bpy.ops.mesh.primitive_uv_sphere_add(radius=2.1, location=(0, 0, 0))
    capa_ozono = bpy.context.object
    capa_ozono.name = "Capa_Ozono"

    # Aplicar textura de nubes tenues a la capa de ozono
    material_nubes = bpy.data.materials.new(name="Nubes_Material")
    material_nubes.use_nodes = True
    bsdf_nubes = material_nubes.node_tree.nodes["Principled BSDF"]
    bsdf_nubes.inputs['Base Color'].default_value = (1, 1, 1, 0.3)  # Blanco tenue
    capa_ozono.data.materials.append(material_nubes)

def crear_estacion_espacial():
    # Crear la tercera esfera con separación interior y aumentar su tamaño (estación espacial)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=5.5, location=(0, 0, 0))
    estacion_espacial = bpy.context.object
    estacion_espacial.name = "Estacion_Espacial"

    # Aplicar textura metálica básica a la estación espacial
    material = bpy.data.materials.new(name="Metal_Material")
    material.use_nodes = True
    bsdf = material.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Metallic'].default_value = 1
    bsdf.inputs['Roughness'].default_value = 0.5
    estacion_espacial.data.materials.append(material)

    # Crear el suelo alrededor del planeta
    bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, -1))
    suelo = bpy.context.object
    suelo.name = "Suelo"
    suelo.data.materials.append(material)

    # Crear diferentes niveles en el suelo
    for i in range(1, 4):
        bpy.ops.mesh.primitive_plane_add(size=10 - i, location=(0, 0, -1 - i))
        nivel = bpy.context.object
        nivel.name = f"Nivel_{i}"
        nivel.data.materials.append(material)

    # Crear una cúpula pequeña en el centro
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 1))
    cupula = bpy.context.object
    cupula.name = "Cupula"
    cupula.data.materials.append(material)

def crear_sol_artificial():
    # Añadir el sol artificial dentro de la estación espacial
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 3))
    sol_artificial = bpy.context.object
    sol_artificial.name = "Sol_Artificial"

    # Aplicar textura amarilla al sol artificial
    material_sol = bpy.data.materials.new(name="Sol_Material")
    material_sol.use_nodes = True
    bsdf_sol = material_sol.node_tree.nodes["Principled BSDF"]
    bsdf_sol.inputs['Base Color'].default_value = (1, 1, 0, 1)  # Amarillo
    sol_artificial.data.materials.append(material_sol)

def animar_estacion_espacial():
    # Animar la estación espacial para que rodee el planeta
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 250
    estacion_espacial = bpy.data.objects["Estacion_Espacial"]
    estacion_espacial.animation_data_create()
    estacion_espacial.animation_data.action = bpy.data.actions.new(name="Orbita")

    fcurves = estacion_espacial.animation_data.action.fcurves
    data_path = "location"

    for i in range(3):
        fcurve = fcurves.new(data_path=data_path, index=i)
        kf = fcurve.keyframe_points.insert(frame=1, value=estacion_espacial.location[i])
        kf.interpolation = 'LINEAR'
        kf = fcurve.keyframe_points.insert(frame=250, value=estacion_espacial.location[i] + (10 if i == 0 else 0))
        kf.interpolation = 'LINEAR'

    # Añadir un modificador de curva para la órbita
    curve = bpy.data.curves.new(name='Orbita_Curva', type='CURVE')
    curve.dimensions = '3D'
    spline = curve.splines.new(type='NURBS')
    spline.points.add(3)
    spline.points[0].co = (10, 0, 0, 1)
    spline.points[1].co = (0, 10, 0, 1)
    spline.points[2].co = (-10, 0, 0, 1)
    spline.points[3].co = (0, -10, 0, 1)

    curve_obj = bpy.data.objects.new('Orbita_Curva', curve)
    bpy.context.collection.objects.link(curve_obj)

    follow_path = estacion_espacial.modifiers.new(name='FollowPath', type='FOLLOW_PATH')
    follow_path.object = curve_obj
    follow_path.use_curve_follow = True

    bpy.context.view_layer.objects.active = estacion_espacial
    bpy.ops.object.constraint_add(type='FOLLOW_PATH')
    estacion_espacial.constraints["Follow Path"].target = curve_obj
    estacion_espacial.constraints["Follow Path"].use_fixed_location = True
    estacion_espacial.constraints["Follow Path"].offset_factor = 0
    estacion_espacial.constraints["Follow Path"].keyframe_insert(data_path="offset_factor", frame=1)
    estacion_espacial.constraints["Follow Path"].offset_factor = 1
    estacion_espacial.constraints["Follow Path"].keyframe_insert(data_path="offset_factor", frame=250)

def main():
    crear_planeta()
    crear_estacion_espacial()
    crear_sol_artificial()
    animar_estacion_espacial()

if __name__ == "__main__":
    main()
