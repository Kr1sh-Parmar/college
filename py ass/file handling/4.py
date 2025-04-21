import os
import shutil

def copy_to_subdirectory():
    os.makedirs("new_dir", exist_ok=True)
    shutil.copy("source_dir/file.txt", "new_dir/copy.txt")

    print("File copied to new_dir/copy.txt")




