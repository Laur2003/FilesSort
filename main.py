from pathlib import Path, PurePosixPath
import time
from datetime import datetime
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

old_directory = "C:/Users/Laur/Downloads/"

new_directory_txt = "C:/Users/Laur/Downloads/Downloads_Txt/"
new_directory_jpg = "C:/Users/Laur/Downloads/Downloads_Jpg/"
new_directory_png = "C:/Users/Laur/Downloads/Downloads_Png/"
new_directory_exe = "C:/Users/Laur/Downloads/Downloads_Exe/"
new_directory_ico = "C:/Users/Laur/Downloads/Downloads_Ico/"
new_directory_zip = "C:/Users/Laur/Downloads/Downloads_Zip/"
new_directory_json = "C:/Users/Laur/Downloads/Downloads_Json/"
new_directory_pdf = "C:/Users/Laur/Downloads/Downloads_Pdf/"
new_directory_docx = "C:/Users/Laur/Downloads/Downloads_Docx/"
new_directory_torrent = "C:/Users/Laur/Downloads/Downloads_Torrent/"
new_directory_rar = "C:/Users/Laur/Downloads/Downloads_Rar/"
new_directory_html = "C:/Users/Laur/Downloads/Downloads_Html/"
new_directory_css = "C:/Users/Laur/Downloads/Downloads_Css/"
new_directory_js = "C:/Users/Laur/Downloads/Downloads_Js/"
new_directory_py = "C:/Users/Laur/Downloads/Downloads_Py/"
new_directory_apk = "C:/Users/Laur/Downloads/Downloads_Apk/"

list_of_directories = [
    {'dir_name':new_directory_txt , 'dir_ext':'.txt'},
    {'dir_name':new_directory_jpg , 'dir_ext':'.jpg'},
    {'dir_name':new_directory_png , 'dir_ext':'.png'},
    {'dir_name':new_directory_exe , 'dir_ext':'.exe'},
    {'dir_name':new_directory_ico , 'dir_ext':'.ico'},
    {'dir_name':new_directory_zip , 'dir_ext':'.zip'},
    {'dir_name':new_directory_json , 'dir_ext':'.json'},
    {'dir_name':new_directory_pdf , 'dir_ext':'.pdf'},
    {'dir_name':new_directory_docx , 'dir_ext':'.docx'},
    {'dir_name':new_directory_torrent , 'dir_ext':'.torrent'},
    {'dir_name':new_directory_rar , 'dir_ext':'.rar'},
    {'dir_name':new_directory_html , 'dir_ext':'.html'},
    {'dir_name':new_directory_css , 'dir_ext':'.css'},
    {'dir_name':new_directory_js , 'dir_ext':'.js'},
    {'dir_name':new_directory_py , 'dir_ext':'.py'},
    {'dir_name':new_directory_apk , 'dir_ext':'.apk'},
]
class Watcher:
    DIRECTORY_TO_WATCH = old_directory

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        pathlist = Path(old_directory).glob('*')
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            for path in pathlist:
                path_to_move = ''
                #because path is object not string
                #get current path/file name and new path
                path_in_str = str(path)
                new_path_in_str = ''
                extension = PurePosixPath(path_in_str).suffix
                file_name = Path(path_in_str).stem
                status = False

                for dict_dir in list_of_directories:
                    if dict_dir['dir_ext'] == extension:
                        new_path_in_str = dict_dir['dir_name'] + file_name + extension
                        path_to_move = dict_dir['dir_name']
                        status = True
                        print(new_path_in_str + "lmao")
                        break;

                #create dir if it doesn't exists
                if(status == True):
                    if(Path(path_to_move).exists() == False):
                        try:
                            filepath = Path(path_to_move)
                            filepath.mkdir(parents=True, exist_ok=True)
                        except OSError:
                            print ("Creation of the directory %s failed" % path)
                        else:
                            print ("Successfully created the directory %s " % path)

                    def check_file(filePath):
                        now = datetime.now()
                        current_time = now.strftime("%H_%M_%S")
                        current_time_list = list(current_time)

                        extension = PurePosixPath(filePath).suffix
                        filePathList = list(filePath)
                        position = len(filePath) - len(extension)

                        for i in range(len(current_time_list)):
                            filePathList.insert(i + position, current_time_list[i])

                        filePath = ''.join(filePathList)
                        return filePath


                    if Path(new_path_in_str).exists():
                        new_path_in_str = check_file(new_path_in_str)
                        print(new_path_in_str + "lopoooo")

                    Path(path_in_str).rename(new_path_in_str)
                    print("Path 1 = " + path_in_str )
                    print("New_Path 1 = " + new_path_in_str )


if __name__ == '__main__':
    w = Watcher()
    w.run()
