import bpy

# Crear el planeta
bpy.ops.mesh.primitive_uv_sphere_add(radius=2, location=(0, 0, 0))
planeta = bpy.context.object
planeta.name = "Planeta"

# Crear la capa de ozono
bpy.ops.mesh.primitive_uv_sphere_add(radius=2.1, location=(0, 0, 0))
capa_ozono = bpy.context.object
capa_ozono.name = "Capa_Ozono"

# Crear la tercera esfera con separación interior
bpy.ops.mesh.primitive_uv_sphere_add(radius=2.5, location=(0, 0, 0))
esfera_interior = bpy.context.object
esfera_interior.name = "Esfera_Interior"

# Aplicar textura metálica básica a la tercera esfera
material = bpy.data.materials.new(name="Metal_Material")
material.use_nodes = True
bsdf = material.node_tree.nodes["Principled BSDF"]
bsdf.inputs['Metallic'].default_value = 1
bsdf.inputs['Roughness'].default_value = 0.5
esfera_interior.data.materials.append(material)

# Crear la estación espacial
bpy.ops.mesh.primitive_uv_sphere_add(radius=5, location=(10, 0, 0))
estacion_espacial = bpy.context.object
estacion_espacial.name = "Estacion_Espacial"

# Animar la estación espacial para que rodee el planeta
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 250
estacion_espacial.animation_data_create()
estacion_espacial.animation_data.action = bpy.data.actions.new(name="Orbita")

fcurves = estacion_espacial.animation_data.action.fcurves
data_path = "location"
index = 0

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
    