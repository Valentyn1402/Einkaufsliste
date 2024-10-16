import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class Editor(ctk.CTk):

    def __init__(self) -> None: 
        # initialize the dunder method 
        super().__init__()
        ctk.set_appearance_mode("dark")

        # setup basic layout of the window
        self.geometry('700x400')
        self.title("Editor")

        # create frames 
        self.frame_1 = ctk.CTkFrame(self, bg_color="black")
        self.frame_2 = ctk.CTkFrame(self, bg_color="black")
        self.frame_3 = ctk.CTkFrame(self, bg_color="black")
        self.frame_1.pack(side="left")
        self.frame_2.pack(side="left")
        self.frame_3.pack(side="left")

        # define variables
        self.ingredientsvar = tk.StringVar()
        
        # create widgets
        self.create_widgets()


        self.mainloop()


    def create_widgets(self):

        # add buttons to the frame 
        self.button_1 = ctk.CTkButton(self.frame_1, text = "Edit Recipe")
        self.button_2 = ctk.CTkButton(self.frame_1, text = "Remove Recipe")

        # add canvas to the frame 
        self.canvas = tk.Canvas(self.frame_2, height=20, width=100)


        #add the listbox 
        self.listbox = tk.Listbox(self.frame_2, listvariable=self.ingredientsvar,
                                   height=20, width=100)
        #create a scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame_3, orient=tk.VERTICAL)
        
        self.listbox.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        self.button_1.pack(expand = True, pady = 20)
        self.button_2.pack(expand = True, pady = 20)
        self.listbox.pack()
        self.canvas.pack()
        # self.scrollbar.pack(expand=True)


if __name__ == "__main__":
    Editor()

