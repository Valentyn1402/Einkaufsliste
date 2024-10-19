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
        self.geometry('1200x600')
        self.title("Editor")

        # define the grid of main window frame 
        self.define_grid() 
        
        # create frames 
        self.define_scrollable_frame()
        self.define_frame()

        # define variables
        self.ingredientsvar = tk.StringVar()
        
        # define all the widgets
        self.create_widgets()

        # create widgets
        # self.create_widgets()

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
        
    def define_frame(self):
        
        self.frame_2 = ctk.CTkFrame(master=self, fg_color="white")
        self.frame_2.grid(column = 3, row = 1, rowspan = 2, columnspan = 1)
        
        self.frame_2.columnconfigure(0, weight=1)
        self.frame_2.columnconfigure(1, weight=1)
        
        self.frame_2.rowconfigure(0, weight=1, minsize=20)
        self.frame_2.rowconfigure(1, weight=1, minsize=20)
        self.frame_2.rowconfigure(2, weight=1, minsize=20)
        self.frame_2.rowconfigure(3, weight=1, minsize=20)
        self.frame_2.rowconfigure(4, weight=1, minsize=20)
        
    
    def define_scrollable_frame(self): 
        # create frames 
        self.frame = ctk.CTkScrollableFrame(master=self, width= 600, height=400, fg_color="white")
        self.frame.grid(column = 1, row = 1, rowspan = 2, columnspan = 2)
        
        # create a grid for the scrollable frame
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)       
        
    def create_combobox(self):
        self.combobox_1 = ctk.CTkComboBox(self.frame_2)
        self.combobox_2 = ctk.CTkComboBox(self.frame_2)

    def create_buttons(self):
        
        # add buttons to the frame 
        self.button_1 = ctk.CTkButton(self, text = "Edit Recipe")
        self.button_2 = ctk.CTkButton(self, text = "Remove Recipe")
        
        # define 4 Buttons for the header
        # self.button_3 = ctk.CTkButton(master=self.frame, text = "Nothing", fg_color="white", 
        #               border_color="white", border_width=2, command=lambda: print("Button"))
        self.button_4 = ctk.CTkButton(master=self.frame, text = "Author", hover_color="red", 
                      border_color="white", border_width=2, command=lambda: print("Button"))
        self.button_5 = ctk.CTkButton(master=self.frame, text = "Date ", hover_color="red", 
                      border_color="white", border_width=2, command=lambda: print("Button"))
        self.button_6 = ctk.CTkButton(master=self.frame, text = "Rating", hover_color="red", 
                      border_color="white", border_width=2, command=lambda: print("Button"))
        
        self.button_7 = ctk.CTkButton(master=self.frame_2, text= "Change Name", text_color="black", 
                                     fg_color="white", hover_color="red")
        
        self.button_8 = ctk.CTkButton(master=self.frame_2, text= "Remove Ingredient", text_color="black", 
                                     fg_color="white", hover_color="red")
        
        self.button_9 = ctk.CTkButton(master=self.frame_2, text= "Apply Changes ", text_color="black", 
                                     fg_color="white", hover_color="red")
        
    def create_labels(self):
        # recipe entry labels
        self.label_2 = ctk.CTkLabel(master=self.frame, text= "Valentyn Subotovic", text_color="black")
        self.label_3 = ctk.CTkLabel(master=self.frame, text= "14.02.2024", text_color="black")
        self.label_4 = ctk.CTkLabel(master=self.frame, text= "4 Stars", text_color="black")
        
        # labels for editor menu
        self.label_5 = ctk.CTkLabel(master=self.frame_2, text= "Recipe Name", text_color="black")
        self.label_6 = ctk.CTkLabel(master=self.frame_2, text= "Ingredients", text_color="black")
        self.label_7 = ctk.CTkLabel(master=self.frame_2, text= "Amount", text_color="black")
        self.label_8 = ctk.CTkLabel(master=self.frame_2, text= "Measurement", text_color="black")
        
    def place_combobox(self):
        self.combobox_1.grid(column = 0, row = 3)
        self.combobox_2.grid(column = 1, row = 4)
        
    def place_labels(self):
        self.label_2.grid(column = 1, row = 1)
        self.label_3.grid(column = 2, row = 1)
        self.label_4.grid(column = 3, row = 1)
        
        # place main edit menu labels
        self.label_5.grid(column = 0, row = 0)
        self.label_6.grid(column = 0, row = 2)
        self.label_7.grid(column = 0, row = 4)
        self.label_8.grid(column = 1, row = 4)
        
    def place_buttons(self):
        self.button_1.grid(column = 0, row = 1)
        self.button_2.grid(column = 0, row = 2)
        # place on the scrollable frame 
        # self.button_3.grid(column = 0, row = 0)
        self.button_4.grid(column = 1, row = 0)
        self.button_5.grid(column = 2, row = 0)
        self.button_6.grid(column = 3, row = 0)
        
        self.button_7.grid(column = 1, row = 1)
        self.button_8.grid(column = 1, row = 3)
        self.button_9.grid(column = 0, row = 6)

    def define_canvas(self):
        # add canvas to the frame 
        self.canvas = tk.Canvas(self, height=300, width=600)

    def create_widgets(self):

        # define buttons
        self.create_buttons()

        # create labels
        self.create_labels()
        
        # create combobox
        self.create_combobox()
        
        # define canvas 
        self.define_canvas()
        
        # place butt
        self.place_buttons()
        
        # place labels
        self.place_labels()
        
        # place combobox
        self.place_combobox()

if __name__ == "__main__":
    Editor()

