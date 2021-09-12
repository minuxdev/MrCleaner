from tkinter import (Checkbutton, Button, Entry, Frame, LabelFrame, Grid, 
                    IntVar, Scrollbar, Listbox, Tk)


class MrCleaner():
    def __init__(self, master = None):
        self.master = master

        self.create_frames()
        self.create_widgets()
        self.place_widgets()
    

    def create_frames(self):
        self.entry_frame = Frame(self.master)
        self.control_frame = Frame(self.master)
        self.output_frame = Frame(self.master)
    

    def create_widgets(self):
        self.ctrl_del = IntVar()
        self.ctrl_rep = IntVar()
        
        #   ENTRY  FRAME
        self.select_directory = Button(self.entry_frame, text="Directory",
                            width=12)
        self.input = Entry(self.entry_frame, bg="white", fg="black", 
                            font="Monospace 10", justify="center")

        #   CONTROL FRAME
        self.run_btn = Button(self.control_frame, text="Run",
                            width=12)
        self.delete = Checkbutton(self.control_frame, variable=self.ctrl_del,
                            text="Delete Files")

        self.report = Checkbutton(self.control_frame, variable=self.ctrl_rep,
                    text="Generate Report")

        #   OUTPUT  FRAME
        self.scroll_v = Scrollbar(self.output_frame, orient="vertical")
        self.scroll_h = Scrollbar(self.output_frame, orient="horizontal")
        self.list_box = Listbox(self.output_frame, font="Monospace 10",
                                yscrollcommand=self.scroll_v.set, 
                                xscrollcommand=self.scroll_h.set)
        self.scroll_h.config(command=self.list_box.xview)
        self.scroll_v.config(command=self.list_box.yview)


    def place_widgets(self):
        self.entry_frame.grid(sticky="we", padx=10, pady=4)
        self.control_frame.grid(row=1, sticky="we", padx=10, pady=4)
        self.output_frame.grid(row=2, sticky="news", padx=10, pady=4)
        
        Grid.columnconfigure(self.master, 0, weight=1)
        Grid.rowconfigure(self.master, 2, weight=1)

        Grid.columnconfigure(self.entry_frame, 1, weight=1)
        Grid.columnconfigure(self.output_frame, 1, weight=1)
        Grid.rowconfigure(self.output_frame, 0, weight=1)


        self.select_directory.grid(sticky="we", padx=4, pady=4)
        self.input.grid(row=0, column=1, sticky="we", padx=4, pady=4)

        self.run_btn.grid(row=0, column=0, sticky="ew", padx=4, pady=4)
        self.delete.grid(row=0, column=1, padx=4)
        self.report.grid(row=0, column=2, padx=4)

        self.list_box.grid(columnspan=2,sticky="news", padx=4, pady=4)
        self.scroll_v.grid(row=0, column=2, sticky="ns")
        self.scroll_h.grid(row=1, columnspan=2, sticky="we")


if __name__ == "__main__":
    root = Tk()
    root.minsize(400, 300)
    root.title("MrCleaner")
    app = MrCleaner(master=root)
    root.mainloop()
