import os
import glob

base_dir = "val"

for subdir in os.listdir(base_dir):
    subdir_path = os.path.join(base_dir, subdir)
    if os.path.isdir(subdir_path):
        print(f"Processing directory: {subdir_path}")
        image_files = glob.glob(os.path.join(subdir_path, "*.jpg"))  

        # Loop through the image files and rename them
        for i, old_name in enumerate(image_files):
            # Get the file extension
            extension = os.path.splitext(old_name)[1]
            
            # Generate the new file name
            new_name = os.path.join(subdir_path, f"val-{subdir.lower()}-{i+1:03d}{extension}")
            
            # Rename the file
            os.rename(old_name, new_name)
