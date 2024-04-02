bl_info = {
    "name": "Batch import reference images",
    "author": "DC",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Add > Image > Batch import reference images",
    "description": "Batch import reference images from the 'refimg' folder in the same directory",
    "warning": "",
    "doc_url": "",
    "category": "Add image",
}



import bpy
import os
import math




class ImportBatchReference(bpy.types.Operator):
    """Imports all reference images from the 'refimg' folder in the same directory"""
    bl_idname = "import_files.batch_ref_img"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Batch Reference Images"

    
    def execute(self, context):
        #get working directory
        current_directory = os.path.dirname(bpy.data.filepath)
        #create path to target dircetory
        target_directory = current_directory + "/refimg"
        #get files array
        files = os.listdir(target_directory)
        #number of files
        num_files = len(files)
        i = 1
        image_counter = 1
        
        for file in files:
            print(file)
                 
             
            #import image
            bpy.ops.object.load_reference_image(filepath = target_directory + "/" + file)
            img = bpy.context.object
            
            #roate image
            img.rotation_euler[0] = math.radians(90)
            
            #position the image
            if num_files > 1:
                if i <= num_files/2:
                    img.location = (-6 * image_counter, 3, 3)
                    i += 1
                    image_counter += 1
                    #reset the image counter once it reaches half
                    #so that it starts placing images close to the positive side of the X axis
                    if image_counter > num_files/2:
                        image_counter = 1
                else:
                    img.location = (6 * image_counter, 3, 3)
                    image_counter += 1
            
            
            else:
                #if there is only one image 
                img.location[2] = 3

            
            print("done")        
        
        return {'FINISHED'}
    
    
    
    
#creating the add buton
def batch_import_button(self, context):
    self.layout.operator(
        ImportBatchReference.bl_idname,
        text="Batch import reference images",
        icon='PLUGIN')




def register():
    bpy.utils.register_class(ImportBatchReference)
    bpy.types.VIEW3D_MT_image_add.append(batch_import_button)
   


def unregister():
    bpy.utils.unregister_class(ImportBatchReference)
    bpy.types.VIEW3D_MT_image_add.remove(batch_import_button)
    



if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.import_files.batch_ref_img()