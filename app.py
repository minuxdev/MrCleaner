from tkinter import *
from tkinter import filedialog, messagebox
from modules.gui import MrCleaner
from modules.report_gen import report_generator
from modules.multiples import base_converter
import os, shutil
from tqdm import tqdm
from threading import Thread


root = Tk()
root.title("MrCleaner ver:1.0")
root.geometry("700x500+300+100")
root.minsize(400, 300)

#   IMPORTING VARIABLES FROM GUI    #
gui = MrCleaner(root)
input_ = gui.input
list_box = gui.list_box
ctrl_del = gui.ctrl_del
ctrl_rep = gui.ctrl_rep
progress = gui.percentage


#   GLOBAL VARIABLES    #
duplicated_files = []
sizes = []


#   FUNCTIONS   #
def get_directory():
    input_.delete(0, END)
    list_box.delete(0, END)
    directory = filedialog.askdirectory(title="Select directory",
                                        mustexist=True)
    input_.insert(END, directory)

    if directory:
        msg = '''NOTE: Depending on how deep your subdirectories is,\
it my take a while and or seem to be frozen, so please, be patient and do not interrupt!'''
        # agree = messagebox.showinfo('Message', msg)
        
        Thread(target=locate_duplicated_files).start()


def locate_duplicated_files():
    global duplicated_files, sizes
    dir_btn = gui.select_directory
    run_btn = gui.run_btn
    dir_btn.config(state=DISABLED)
    run_btn.config(state=DISABLED)

    directory = input_.get()
    
    found_files = []
    files_path = []
    files_sizes = []
    c = 0
    for rt, directories, files in tqdm(os.walk(directory)):
        for file in files:
            try:
                new_file = os.path.join(rt, file)
                new_file_size = os.path.getsize(new_file)
                found_files.append(file)
                files_path.append(new_file)
                files_sizes.append(new_file_size)
                c += 1

            except FileNotFoundError as e:
                pass
            except OSError as e:
                pass
            root.update_idletasks()
            progress['text'] = f'{c}'

    for i in range(len(found_files)):
        if found_files.count(found_files[i]) != 1:
            duplicated_files.append(files_path[i])
            sizes.append(files_sizes[i])

    list_box.delete(0, END)

    if len(duplicated_files) != 0:
        list_box.insert(END, "{:=^79}".format(' DUPLICATED FILES '))
        list_box.insert(END, '')

        for f in range(len(duplicated_files)):
            file = f"{duplicated_files[f]} Size: {base_converter(sizes[f])}"
            list_box.insert(END, file)
    else:
        messagebox.showinfo('Message', 'No duplicated file found!')
    
    progress['text'] = '100%'
    run_btn.config(state=ACTIVE)
    dir_btn.config(state=ACTIVE)


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
    
    if len(duplicated_files) != 0:
        file_path, file_size = extract_file_from_duplicated(duplicated_files, sizes)
        destiny_dir = filedialog.askdirectory(title="Choose backup directory", 
                                                mustexist=True)
        count = 0
        
        if ctrl_del.get() == 1:
            msg = 'You are about to delete files! Do you wnat to continue?'
            answer = warning_on_delete = messagebox.askquestion('Confirmation', msg)

            if answer == 'yes':

                try:
                    for i in range(len(duplicated_files)): 
                        if duplicated_files[i] in file_path:
                            shutil.copy(src=duplicated_files[i], dst=destiny_dir)
                        os.remove(duplicated_files[i])
                        count += 1
                except:
                    pass            
                if answer == 'yes':
                    list_box.delete(0, END)
                    list_box.insert(0, '{:=^79}'.format(' REMAINING FILES '))
                    list_box.insert(END, '')

                    for j in range(len(file_path)):
                        item = f"{file_path[j]}  {base_converter(file_size[j])}"
                        list_box.insert(END, item)
            else:
                messagebox.showerror('Message', 'Aborting!')
        else:    
            pass            
        if ctrl_rep.get() == 1:
            report_generator(destiny_dir,duplicated_files, sizes, base_converter)
            
        if ctrl_del.get() == 0 and ctrl_rep.get() == 0:
            msg = 'Please, you must choose an option!'
        else:
            msg = 'Success!'
            list_box.delete(0, END)
        messagebox.showinfo('Message', msg)
    else:
        path = input_.get()
        if not path:    
            messagebox.showinfo('Message', 'Please, select directory!')
            




#   COMMANDS    #
dir_btn = gui.select_directory.config(command=get_directory)
run_btn = gui.run_btn.config(command=remove_duplicated_files)


root.mainloop()
