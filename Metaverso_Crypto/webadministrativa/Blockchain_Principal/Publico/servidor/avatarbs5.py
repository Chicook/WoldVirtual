from Metaverso_Crypto.webadministrativa.Blockchain_Principal.Publico.servidor.avatarbs2 import log_action
import bpy

def cambiar_estructura_avatar():
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

    bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 1))
    bpy.ops.object.modifier_add(type='SKIN')
    bpy.context.object.modifiers["Skin"].use_smooth_shade = True
    bpy.context.object.modifiers["Skin"].show_in_editmode = True
    bpy.ops.object.modifier_apply(modifier="Skin")
    bpy.ops.object.editmode_toggle()

    bpy.context.view_layer.objects.active = bpy.data.objects["Armature"]
    bpy.ops.object.parent_set(type='ARMATURE_NAME')

    bpy.ops.transform.resize(value=(1, 1, 2))

    class AvatarSettingsPanel(bpy.types.Panel):
        bl_label = "Configuración del Avatar"
        bl_idname = "OBJECT_PT_avatar_settings"
        bl_space_type = 'PROPERTIES'
        bl_region_type = 'WINDOW'
        bl_context = "object"

        def draw(self, context):
            layout = self.layout
            obj = context.object

            row = layout.row()
            row.prop(obj, "scale", index=2)

            row = layout.row()
            row.prop(obj, "scale", index=0)

            row.prop(obj, "scale", index=1)

    bpy.utils.register_class(AvatarSettingsPanel)

    bpy.context.scene.frame_start = 0
    bpy.context.scene.frame_end = 10

    bpy.ops.object.mode_set(mode='POSE')
    for bone in armature.bones:
        bone.rotation_mode = 'XYZ'
        if bone.name.endswith('.L'):
            bone.rotation_euler.x = 0.5

    log_action("Estructura del avatar cambiada")


