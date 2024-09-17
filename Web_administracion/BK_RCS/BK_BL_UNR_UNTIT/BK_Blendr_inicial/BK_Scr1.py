"""
Descripción de lo que hace este código Python en blender;

1. **Crear el Planeta y su Capa de Ozono**:
   - **Planeta**: Se crea una esfera en el centro de la escena para representar el planeta. Se le aplica una textura azul para simular el mar.
   - **Casquetes Polares**: Se añaden dos esferas pequeñas en la parte superior e inferior del planeta para simular los casquetes polares.
   - **Capa de Ozono**: Se crea una segunda esfera ligeramente más grande que el planeta para representar la capa de ozono. Se le aplica una textura blanca tenue para simular nubes.

2. **Crear la Estación Espacial**:
   - **Estación Espacial**: Se crea una esfera grande alrededor del planeta, que representa la estación espacial. Se le aplica una textura metálica básica.
   - **Suelo y Niveles**: Se añaden varios planos alrededor del planeta para simular el suelo y diferentes niveles de infraestructura dentro de la estación espacial.
   - **Cúpula**: Se añade una esfera pequeña en el centro de la estación espacial, por encima del planeta, para representar una cúpula.

3. **Añadir el Sol Artificial**:
   - **Sol Artificial**: Se crea una esfera pequeña dentro de la estación espacial, en una posición elevada, para simular un sol artificial. Se le aplica una textura amarilla.

4. **Animar la Estación Espacial**:
   - **Configuración de la Animación**: Se define el rango de fotogramas para la animación (de 1 a 250).
   - **Curvas de Animación**: Se añaden curvas de animación para la posición de la estación espacial, asegurando que se mueva en una órbita circular alrededor del planeta.
   - **Curva de Órbita**: Se crea una curva NURBS que define la trayectoria de la órbita.
   - **Modificador de Seguimiento de Curva**: Se añade un modificador a la estación espacial para que siga la curva de órbita.

5. **Función Principal**:
   - **Ejecución de Funciones**: La función principal (`main`) llama a todas las funciones anteriores en el orden adecuado para construir y animar toda la escena.

En resumen, el script crea un planeta con su capa de ozono, una estación espacial que lo rodea, un sol artificial dentro de la estación espacial, y anima la estación espacial para que orbite alrededor del planeta. Todo esto se hace utilizando texturas básicas para simular el mar, los casquetes 
polares y las nubes.

"""
""""
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
"""
"""
este código, 
es para blender.
"""