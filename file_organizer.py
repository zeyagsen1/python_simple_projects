import os as o
import shutil


def arrange_files(file_list):
    for i in range(len(file_list)):

        split = file_list[i].split('.')
        if len(split) > 1 and split[1] == "exe":
            print(file_list[i])
            shutil.move("C:/Users/ibrah/Desktop/" + file_list[i], destination_path)
        if len(split) > 1 and split[1] == "jpg":
            shutil.move("C:/Users/ibrah/Desktop/" + file_list[i], "C:/Users/ibrah/Desktop/image files")


# removedirs,makedirs
path_downloads = "C:/Users/ibrah/Downloads/"
image_file_exist = False
exe_file_exist = False
path = "C:/Users/ibrah/Desktop"
destination_path = "C:/Users/ibrah/Desktop/exe files"

list_of_files = o.listdir(path)
for a in range(len(list_of_files)):
    if list_of_files[a] == "image files":
        image_file_exist = True
    if list_of_files[a] == "exe files":
        exe_file_exist = True
if image_file_exist and exe_file_exist:
    arrange_files(list_of_files)
else:
    o.makedirs(path + "/exe files")
    o.makedirs(path + "/image files")
    arrange_files(list_of_files)

d_files=o.listdir(path_downloads)

for i in range(len(d_files)):
    a=d_files[i].split('.')
    if(a[1]=='pdf'):
        print(path_downloads+d_files[i])
       # o.removedirs(path_downloads+d_files[i])
