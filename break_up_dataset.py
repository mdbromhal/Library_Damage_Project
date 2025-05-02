"""Script that breaks up dataset images into subfolders"""
import os


# 1. List all image files in source folder
source_folder = "/Volumes/Dylan/LibraryDamage/Cropped_images"
source_files = os.listdir(source_folder)
batch_size = 500
# print(source_folder)

# Iterating through files 500 at a time
for batch_num in range(0, len(source_files), batch_size):
    # Specifiying which images are in the batch
    file_batch = source_files[batch_num : batch_num + batch_size]

    # print(file_batch)
    # print(len(file_batch))
    # print("------")

    # Making a new directory 
    new_folder_name = source_folder + "_batch_" + str(batch_num // batch_size)
    if os.path.exists(new_folder_name):
        raise Exception("Batch directory already exists.")
    else:
        print(new_folder_name)
        os.makedirs(new_folder_name)

        for image in file_batch:

            old_image_path = os.path.join(source_folder, str(image))
            new_image_path = os.path.join(new_folder_name, str(image))
            
            if os.path.exists(old_image_path):
            
                os.rename(old_image_path, new_image_path)
            else:
                print(f"File not found: {str(image)}")
    # new_directory = os.makedirs(source_folder + "_batch_" + str(batch_num))



# 2. Create new destination folders in batches of 500 images each


# 3. Move 500 images at a time to the folders

