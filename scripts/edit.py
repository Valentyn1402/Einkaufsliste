import tkinter as tk
from tkinter import ttk
from tkinter import font
import customtkinter as ctk

class Editor(ctk.CTk):

    def __init__(self) -> None: 
        # initialize the dunder method 
        super().__init__()
        ctk.set_appearance_mode("dark")

        # setup basic layout of the window
        self.geometry('700x400')
        self.title("Editor")

        # define the grid
        self.define_grid() 
        # # create frames 
        # self.frame_1 = ctk.CTkFrame(self, bg_color="black")
        # self.frame_2 = ctk.CTkFrame(self, bg_color="black")
        # self.frame_3 = ctk.CTkFrame(self, bg_color="black")
        # self.frame_1.pack(side="left")
        # self.frame_2.pack(side="left")
        # self.frame_3.pack(side="left")

        # define variables
        self.ingredientsvar = tk.StringVar()
        
        # create widgets
        self.create_widgets()


        self.mainloop()

    def define_grid(self):

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

    def create_buttons(self):
        
        # add buttons to the frame 
        self.button_1 = ctk.CTkButton(self, text = "Edit Recipe")
        self.button_2 = ctk.CTkButton(self, text = "Remove Recipe")

    def define_canvas(self):

        # add canvas to the frame 
        self.canvas = tk.Canvas(self, height=300, width=600)

    def define_treeview(self):

        # styling for treeview 
        s = ttk.Style()
        s.theme_use('clam')

        # Configure the style of Heading in Treeview widget
        s.configure('Treeview.Heading', background="green3", font=("Open Sans", 12, "bold"))
        s.configure("Treeview", rowheight = 30, background = "blue", font=("Open Sans", 14))

        # treeview
        columns = [0, 1, 2]
        self.treebox = ttk.Treeview(self, columns = columns, height=20)

        # Define our column headings
        self.treebox.heading("0", text="Author")
        self.treebox.heading("1", text="Date")
        self.treebox.heading("2", text="Rating")

        self.treebox.insert("", 0, "widget", text = "Widget Tour")
        self.treebox.insert("", 1, "sd", text = "Widget Tour")

    def create_widgets(self):

        # define buttons
        self.create_buttons()

        # define canvas 
        self.define_canvas()

        # define treeview
        self.define_treeview()

        frame = tk.Frame(self.canvas, bg="black")
        button = ctk.CTkButton(self, fg_color="blue", text = "Edit")
        self.canvas.create_window(50, 50, window=button, anchor="nw")

        #add the listbox 
        self.listbox = tk.Listbox(self, listvariable=self.ingredientsvar,
                                   height=20, width=100)
        #create a scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        
        self.listbox.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        self.button_1.grid(column = 0, row = 1)
        self.button_2.grid(column = 0, row = 2)
        # self.listbox.grid(column = 1, row = 1, columnspan = 2, rowspan = 2 )
        # self.canvas.grid(column = 1, row = 1, columnspan = 2, rowspan = 2)
        self.treebox.grid(column = 1, row = 1, columnspan = 2, rowspan = 2)
        # self.scrollbar.pack(expand=True)


if __name__ == "__main__":
    Editor()

