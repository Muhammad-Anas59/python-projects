import os
import shutil
source_fol=r"C:\Users\manas\OneDrive\Desktop\folderforshutil"
dest_fol=r"C:\Users\manas\OneDrive\Desktop\Copiesfroshutil"
os.makedirs(dest_fol,exist_ok=True)
for i in range(1,101):
    name=f"folder_{i}"
    destination=os.path.join(dest_fol,name)
    os.makedirs(destination,exist_ok=True)
    for item in os.listdir(source_fol):
        source_path=os.path.join(source_fol,item)
        dest_path=os.path.join(dest_fol,item)
        if os.path.isfile(source_path):
            shutil.copy2(source_path,dest_path)
        elif os.path.isfile(source_path):
            shutil.copytree(source_path,dest_path,dirs_exist_ok=True)
print("100 folders are created successfull by copying all the data similar to the source folder :")


