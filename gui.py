from tkinter import *
from tkinter import filedialog
from multiples import base_converter
import os
import shutil


root = Tk()
root.title("Clean Directory")
root.minsize(450,350)


duplicated_files = []
sizes = []


def get_directory():

    directory = filedialog.askdirectory()
    
    input_dir.delete(0, END)
    input_dir.insert(END, directory)

    locate_duplicated_files()
    

def locate_duplicated_files():

    global duplicated_files, sizes

    directory = input_dir.get()
    
    found_files = []
    files_path = []
    files_sizes = []

    for root, directories, files in os.walk(directory):

        for file in files:
            new_file = os.path.join(root, file)
            new_file_size = os.path.getsize(new_file)
            found_files.append(file)
            files_path.append(new_file)
            files_sizes.append(new_file_size)

    for i in range(len(found_files)):
        if found_files.count(found_files[i]) != 1:
            duplicated_files.append(files_path[i])
            sizes.append(files_sizes[i])

    list_box.delete(0, END)
    for file in duplicated_files:
        list_box.insert(END, file)


def organize_duplicated_files(dub_files=duplicated_files, sizes=sizes):

    paths_and_names = []
    file_path = []
    file_names = []
    file_size = []

    for i in range(len(dub_files)):
        splited_path = os.path.split(dub_files[i])
        paths_and_names.append(splited_path)
        
    for f in range(len(paths_and_names)):
        if paths_and_names[f][1] not in file_names:
            file_names.append(paths_and_names[f][1])
            file_path.append(dub_files[f])
            file_size.append(sizes[f])

    list_box.delete(0, END)

    for j in range(len(file_path)):
        list_box.insert(END, (file_path[j], base_converter(file_size[j])))






entry_frame = Frame(root)
output_frame = Frame(root)

entry_frame.grid(sticky="we", padx=10, pady=10)
output_frame.grid(row=1, column=0, sticky="news", padx=10, pady=10)

Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)

Grid.columnconfigure(entry_frame, 1, weight=1)
Grid.columnconfigure(output_frame, 1, weight=1)
Grid.rowconfigure(output_frame, 0, weight=1)


select_dir_button = Button(entry_frame, text="Directory", width=10, 
                            command=get_directory)

input_dir = Entry(entry_frame, font="Monospace 10", fg="black", bg="white",
                    justify="center")

select_dir_button.grid(sticky="we", padx=5, pady=5)
input_dir.grid(row=0, column=1, sticky="we", padx=5, pady=5)


start_btn = Button(output_frame, text="Run", width=10, 
                command=locate_duplicated_files)

scroll = Scrollbar(output_frame, orient="vertical")
list_box = Listbox(output_frame, yscrollcommand=scroll.set)
scroll.config(command=list_box.yview)

start_btn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

list_box.grid(row=0, rowspan=2, column=1, sticky="news", padx=5, pady=5)
scroll.grid(row=0, column=2, sticky="ns")


# show_var()



root.mainloop()