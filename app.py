from tkinter import *
from tkinter import filedialog
from modules.gui import MrCleaner
from modules.multiples import base_converter
import os, shutil


root = Tk()
root.minsize(500, 400)
root.title("MrCleaner 1.0")


#   IMPORTING VARIABLES FROM GUI    #
gui = MrCleaner(root)
input = gui.input
list_box = gui.list_box
ctrl_del = gui.ctrl_del
ctrl_rep = gui.ctrl_rep


#   GLOBAL VARIABLES    #
duplicated_files = []
sizes = []


#   FUNCTIONS   #
def get_directory():

    directory = filedialog.askdirectory(mustexist=True)
    
    input.delete(0, END)
    input.insert(END, directory)

    locate_duplicated_files()


def locate_duplicated_files():
    global duplicated_files, sizes

    directory = input.get()
    
    found_files = []
    files_path = []
    files_sizes = []

    for root, directories, files in os.walk(directory):
        for file in files:
            try:
                new_file = os.path.join(root, file)
                new_file_size = os.path.getsize(new_file)
                found_files.append(file)
                files_path.append(new_file)
                files_sizes.append(new_file_size)

            except FileNotFoundError as e:
                pass
            except OSError as e:
                pass

    for i in range(len(found_files)):
        if found_files.count(found_files[i]) != 1:
            duplicated_files.append(files_path[i])
            sizes.append(files_sizes[i])

    list_box.delete(0, END)

    for file in duplicated_files:
        file = f"{file}   Size: {base_converter(new_file_size)}"
        list_box.insert(END, file)


def extract_file_from_duplicated(dub_files, sizes):

    only_names = []
    file_path = []
    file_names = []
    file_size = []

    for i in range(len(dub_files)):
        only_names.append(os.path.split(dub_files[i])[1])

    for f in range(len(only_names)):
        if only_names[f] not in file_names:
            file_names.append(only_names[f])
            file_path.append(dub_files[f])
            file_size.append(sizes[f])

    return file_path, file_size




def remove_duplicated_files():
    global duplicated_files, sizes

    destiny_dir = filedialog.askdirectory(mustexist=True)
    file_path, file_size = extract_file_from_duplicated(duplicated_files, sizes)

    count = 0
    try:
        for i in range(len(duplicated_files)): 
            if duplicated_files[i] in file_path:
                shutil.copy(src=duplicated_files[i], dst=destiny_dir)
        
            if ctrl_del.get() == 1:
                # os.remove(duplicated_files[i])
                count += 1
    except:
        pass

    if ctrl_rep.get() == 1:
        report_generator(duplicated_files, sizes)

    list_box.delete(0, END)

    for j in range(len(file_path)):
        list_box.insert(END, (file_path[j], base_converter(file_size[j])))




def report_generator(dub_files, sizes):

    with open('report.txt', 'w') as rep:
        rep.write('{:~^60}\n\n'.format('Duplicated files found'))
        for l in range(len(dub_files)):
            rep.write(f'{l+1} - {dub_files[l]}  -  {base_converter(sizes[l])}\n')



#   COMMANDS    #
dir_btn = gui.select_directory.config(command=get_directory)
run_btn = gui.run_btn.config(command=remove_duplicated_files)


root.mainloop()
