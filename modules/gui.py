from tkinter import (Checkbutton, Button, Entry, Frame, Label, LabelFrame, Grid, 
                    IntVar, Scrollbar, Listbox, Tk, Menu, Toplevel, Text)
from tkinter.constants import INSERT


class MrCleaner():
    def __init__(self, master = None):
        self.master = master

        self.create_frames()
        self.create_widgets()
        self.crate_menubar()
        self.place_widgets()

        #self.master.config(menu=self.menu)
    

    def create_frames(self):
        self.entry_frame = Frame(self.master)
        self.control_frame = Frame(self.master)
        self.output_frame = Frame(self.master)
    

    def create_widgets(self):
        self.ctrl_del = IntVar()
        self.ctrl_rep = IntVar()
        
        #   ENTRY  FRAME
        self.select_directory = Button(self.entry_frame, text="Search",
                            width=12, font="Poppins 9")
        self.input = Entry(self.entry_frame, bg="white", fg="black", 
                            font="Poppins 9", justify="center", 
                            insertbackground='dodgerblue')

        #   CONTROL FRAME
        self.run_btn = Button(self.control_frame, text="Run",
                            width=12, font="Poppins 9")
        self.delete = Checkbutton(self.control_frame, variable=self.ctrl_del,
                            text="Delete Files", font="Poppins 9")

        self.report = Checkbutton(self.control_frame, variable=self.ctrl_rep,
                    text="Generate Report", font="Poppins 9")

        #   OUTPUT  FRAME
        self.scroll_v = Scrollbar(self.output_frame, orient="vertical")
        self.scroll_h = Scrollbar(self.output_frame, orient="horizontal")
        self.list_box = Listbox(self.output_frame, font="Poppins 9",
                                yscrollcommand=self.scroll_v.set, 
                                xscrollcommand=self.scroll_h.set)
        self.scroll_h.config(command=self.list_box.xview)
        self.scroll_v.config(command=self.list_box.yview)


    def crate_menubar(self):
        self.menu = Menu(self.master)
        about_ = Menu(self.menu, tearoff=0)
        about_.add_command(label='Autor')
        about_.add_command(label='Version')
        
        help_ = Menu(self.menu, tearoff=0)
        help_.add_command(label='Turorial', command=self.tutorial_)
        help_.add_command(label="Update")

        self.menu.add_cascade(label='About', menu=about_)
        self.menu.add_cascade(label='Help', menu=help_)
        self.master.config(menu=self.menu)


    def place_widgets(self):
        self.entry_frame.grid(sticky="we", padx=4, pady=2)
        self.control_frame.grid(row=1, sticky="we", padx=4, pady=2)
        self.output_frame.grid(row=2, sticky="news", padx=4, pady=2)
        
        Grid.columnconfigure(self.master, 0, weight=1)
        Grid.rowconfigure(self.master, 2, weight=1)

        Grid.columnconfigure(self.entry_frame, 1, weight=1)
        Grid.columnconfigure(self.output_frame, 1, weight=1)
        Grid.rowconfigure(self.output_frame, 0, weight=1)


        self.select_directory.grid(sticky="we", padx=4, pady=4)
        self.input.grid(row=0, column=1, sticky="we", padx=14, pady=4)

        self.run_btn.grid(row=0, column=0, sticky="ew", padx=4, pady=4)
        self.delete.grid(row=0, column=1, padx=6)
        self.report.grid(row=0, column=2, padx=6)

        self.list_box.grid(columnspan=2,sticky="news", padx=4, pady=4)
        self.scroll_v.grid(row=0, column=2, sticky="ns")
        self.scroll_h.grid(row=1, columnspan=2, sticky="we")

    
    def autor_(self):
        pass
    
    def version_(self):
        pass
    
    def tutorial_(self):
        title = 'How to use me'
        msg = '''
                                How to use me!

    1 - Search button   \n
    It ask for a directory and go throw it in order to search for
    duplicated files. NOTE: It might take a while and stop responding
    depending on how deep the directory tree is, on click, a pop up 
    screen is shown just to keep you informed.

    2 - Delete Files and Report Generator\n
    Mark at least one of the options to be executed when the "Run" button
    is clicked, otherwise a messsage box will be shown informing that.
    If "Delete files" option is marked, it will make the program delete all
    duplicated files into the given directory.
    If "Report Generator" is checked, it will allow the program to generate
    a "Report.txt" having a list of all duplicated files found.

    2 - Run button\n
    This execute the given option and if none is checked a warning message box
    is shown informing that no option where checked to be executed.
        '''
        
        self.top_level_gui(title, msg)
    
    def update_(self):
        pass
    
    def top_level_gui(self, title, msg):
        top = Toplevel(self.master)
        top.minsize(320, 250)
        top.resizable(width=False, height=False)
        top.title(title)
        top.grab_set()
        text_box = Text(top, spacing1=1, spacing2=1, font="Poppins 10")
        text_box.grid(sticky='news', padx=10, pady=10)
        text_box.insert(INSERT, msg)

if __name__ == "__main__":
    root = Tk()
    root.minsize(400, 300)
    root.title("MrCleaner")
    app = MrCleaner(master=root)
    root.mainloop()
