import os
folder= r"C:\Users\manas\OneDrive\Desktop\testpage"
files=os.listdir(folder)
count=1
for file in files:
    print(file)
    if(file.endswith(".png")):
        oldpath=os.path.join(folder,file)
        newname=f"Picture{count}.png"
        newpath=os.path.join(folder,newname)
        os.rename(oldpath,newpath)
        print(f"Renamed to :{file}  to  {newpath}")
        count+=1
print("All files are updated successfully : ")