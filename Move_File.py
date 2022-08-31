import os
import shutil

from_dir='C:/Users/Abhinav C/Downloads'
to_dir='C:/Users/Abhinav C/Desktop/Document_Files'

list_of_files=os.listdir(from_dir)
#print(list_of_files)

for files in list_of_files:
    name,extension=os.path.splitext(files)
    #print(name)
    #print(extension)

    if extension == ' ':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1=from_dir+'/'+files
        path2=to_dir+'/'+'Document_Files'
        path3=to_dir+'/'+'Document_Files'+'/'+files
        print("Path1:",path1)
        print("Path3:",path3)

        if os.path.exists(path2):
            print("Moving....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Started moving....")
            shutil.move(path1,path3)