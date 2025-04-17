bl_info = {
    "name": "Auto Export on Save",
    "author": "Daniel Sör",
    "version": (1, 0),
    "blender": (4, 4, 0),  # Specify the Blender version
    "location": "File > Export",
    "description": "Automatically executes collection exports after saving.",
    "warning": "",
    "category": "Import-Export",
}

import bpy
from bpy.app.handlers import persistent

@persistent
def export_on_save(dummy):
    bpy.ops.wm.collection_export_all()

def register():
    bpy.app.handlers.save_post.append(export_on_save)

def unregister():
    bpy.app.handlers.save_post.remove(export_on_save)

if __name__ == "__main__":
    register()
