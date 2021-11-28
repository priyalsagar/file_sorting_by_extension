import os
import shutil

path = "D:\priyal/" #input("enter your path:- ") "/Users/apple/Downloads/"
name = os.listdir(path)

folder_name=['image','text','pdf','python',]

for x in range(0,4):
    if not os.path.exists(path + folder_name[x]):
     os.makedirs(path+folder_name[x])
for files in name:
    if ".png" or ".jpg" in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'image/'+files)
    if ".jpeg" in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'image/'+files)
    #if ".jpg" in files and not os.path.exists(path+'image/'+files):
        #shutil.move(path+files,path+'image/'+files)
    
    if ".text" in files and not os.path.exists(path+'text/'+files):
        shutil.move(path+files,path+'text/'+files)
    if ".pdf" in files and not os.path.exists(path+'pdf/'+files):
        shutil.move(path+files,path+'pdf/'+files)
    if ".py" in files and not os.path.exists(path+'python/'+files):
        shutil.move(path+files,path+'python/'+files)
    
print("your files are sorted !")