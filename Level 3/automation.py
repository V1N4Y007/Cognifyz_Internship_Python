import os
import shutil

def organize(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder path does not exist.")
        return

    files = os.listdir(folder_path)
    for file in files:
        if file.endswith('.txt'):
            prefix = file.split('_')[0]  
            dest_folder = os.path.join(folder_path, prefix)

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            source_path = os.path.join(folder_path, file)
            destination_path = os.path.join(dest_folder, file)

            shutil.move(source_path, destination_path)
            print(f"📁 Moved {file} → {prefix}/")

organize('C:/Users/abc/Downloads/internship/Level 3')
