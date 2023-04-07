import bpy

# Función para crear un esqueleto humano
def crear_esqueleto():
    bpy.ops.object.armature_add(enter_editmode=False, location=(0, 0, 0))
    armature = bpy.context.object.data
    
    bpy.ops.object.mode_set(mode='EDIT')
    bone_head = (0, 0, 0)
    bone_tail = (0, 0, 1)
    armature.edit_bones.new('Head').head = bone_head
    armature.edit_bones.new('Neck').head = bone_head
    armature.edit_bones.new('Shoulder.L').head = bone_head
    armature.edit_bones.new('Arm.L').head = bone_head
    armature.edit_bones.new('Hand.L').head = bone_head
    armature.edit_bones.new('Shoulder.R').head = bone_head
    armature.edit_bones.new('Arm.R').head = bone_head
    armature.edit_bones.new('Hand.R').head = bone_head
    armature.edit_bones.new('Spine').head = bone_head
    armature.edit_bones.new('Pelvis').head = bone_head
    armature.edit_bones.new('Thigh.L').head = bone_head
    armature.edit_bones.new('Shin.L').head = bone_head
    armature.edit_bones.new('Foot.L').head = bone_head
    armature.edit_bones.new('Thigh.R').head = bone_head
    armature.edit_bones.new('Shin.R').head = bone_head
    armature.edit_bones.new('Foot.R').head = bone_head
    
    bpy.context.object.show_in_front = True
    bpy.context.object.show_x_ray = True
    
    return armature

# Función para crear una figura humana básica
def crear_figura_humana(armature):
    bpy.context.view_layer.objects.active = bpy.data.objects["Armature"]
    bpy.ops.object.mode_set(mode='POSE')
    
    for bone in armature.bones:
        bone.rotation_mode = 'XYZ'
        if bone.name.endswith('.L'):
            bone.rotation_euler.x = 0.5
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 1))
    bpy.ops.object.modifier_add(type='SKIN')
    bpy.context.object.modifiers["Skin"].use_smooth_shade = True
    bpy.context.object.modifiers["Skin"].show_in_editmode = True
    bpy.ops.object.modifier_apply(modifier="Skin")
    
    bpy.context.object.parent = armature
    
    bpy.ops.transform.resize(value=(1, 1, 2))
    
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')
    
    bpy.context.object.name = 'Figura Humana'

# Creamos un avatar hombre
hombre_armature = crear_esqueleto()
crear_figura_humana(hombre_armature)

# Creamos un avatar mujer
mujer_armature = crear_esqueleto()
crear_figura_humana(mujer_armature)

# Modificamos el tamaño de la figura de la mujer
bpy.context.view_layer.objects.active = bpy.data.objects["Figura Humana.001"]
bpy.ops.transform.resize(value=(0.9, 0.9, 0.9))
bpy.context.object.name = 'Figura Humana Muj
