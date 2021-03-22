from pathlib import Path, PurePosixPath

#get all paths from directory we need
old_directory = "C:/Users/Laur/Desktop/Folder_Old/"
new_directory_txt = "C:/Users/Laur/Desktop/Folder_New_Txt/"
new_directory_jpg = "C:/Users/Laur/Desktop/Folder_New_Jpg/"
new_directory_png = "C:/Users/Laur/Desktop/Folder_New_Png/"
new_directory_exe = "C:/Users/Laur/Desktop/Folder_New_Exe/"
new_directory_zip = "C:/Users/Laur/Desktop/Folder_New_Zip/"


pathlist = Path(old_directory).glob('*')
#pathlist_png = Path("C:/Users/Laur/Desktop/Folder_Old/").glob('**/*.png')
#pathlist_jpg = Path("C:/Users/Laur/Desktop/Folder_Old/").glob('**/*.jpg')

for path in pathlist:
    #because path is object not string
    #get current path/file name and new path
    path_in_str = str(path)
    extension = PurePosixPath(path_in_str).suffix
    file_name = Path(path_in_str).stem
    if(extension == '.txt'):
        new_path_in_str = 'C:/Users/Laur/Desktop/Folder_New_Txt/' + file_name + extension
    elif(extension == '.jpg'):
        new_path_in_str = 'C:/Users/Laur/Desktop/Folder_New_Jpg/' + file_name + extension
    elif(extension == '.png'):
        new_path_in_str = 'C:/Users/Laur/Desktop/Folder_New_Png/' + file_name + extension

    print("Path 1 = " + path_in_str )
    print("New_Path 1 = " + new_path_in_str )
    #change files position
    Path(path_in_str).rename(new_path_in_str)
