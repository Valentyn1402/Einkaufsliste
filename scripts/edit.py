import tkinter as tk
from tkinter import ttk
from tkinter import font
from parse_ingredients import Parser
from paths import STAR_IMAGE_PATH
from PIL import Image
import customtkinter as ctk

class Editor(ctk.CTk, Parser):

    def __init__(self, parent) -> None: 
        # initialize the dunder method 
        super(Editor, self).__init__()
        # ctk.set_appearance_mode("dark")

        # loads yaml data to Parser.yaml_dictionary
        self.load_yaml_data()

        # define variables
        self.define_variables()

        # define parent window
        self.parent = parent

        # define the grid of main window frame 
        self.define_grid() 

        # define variables
        self.ingredientsvar = tk.StringVar()
        
        # define all the widgets
        self.create_widgets()

        # append list entries
        self.add_recipes_to_list()

    def define_variables(self):
        self.combvars = [tk.StringVar() for var in range(2)]

    def define_grid(self):
        # define grid for the window
        self.parent.columnconfigure(0, weight=2)
        self.parent.columnconfigure(1, weight=1)

    def add_recipes_to_list(self):
        for recipe_entry in Parser.yaml_dictionary:
            recipe_name = recipe_entry["recipe"]
            recipe_author = recipe_entry["author"]
            recipe_date = recipe_entry["date"]
            rating = recipe_entry["rating"]
            # frame = tk.Frame(master=self.frame, width=600, height=40, highlightcolor = "black")
            frame = ctk.CTkFrame(master=self.frame, width=600, height=40, fg_color="white")
            frame.pack(expand = True, fill = "x")
            ctk.CTkLabel(master=frame, text= recipe_name, 
                         text_color="black", width = 150, fg_color="white").grid(column = 0, row = 0, sticky = "ew")
            ctk.CTkLabel(master=frame, width = 150, text= recipe_author, 
                         text_color="black", fg_color="white").grid(column = 1, row = 0, sticky = "ew")
            ctk.CTkLabel(master=frame, width = 150, text= recipe_date, 
                         text_color="black", fg_color="white").grid(column = 2, row = 0, sticky = "ew")
            self.add_rating(frame = frame, size = rating)
            
            # ctk.CTkButton(master=frame, hover_color="red", width = 600, 
            #           border_color="white", border_width=2, fg_color="transparent", bg_color="transparent",
            #           command=lambda: print("Button")).grid(column = 0, row = 0, columnspan = 4)
            
    def add_rating(self, frame: tk.Frame, size: int = 5):

        frame_2 = ctk.CTkFrame(master=frame, width = 150, fg_color="white", bg_color="white",
                               height = 40)
        frame_2.grid(column = 3, row = 0, sticky = "we")
        # frame_2.columnconfigure((0, 1, 2, 3, 4), weight = 1)

        for i in range(size):
            my_image = ctk.CTkImage(light_image=Image.open(STAR_IMAGE_PATH),
                                    dark_image=Image.open(STAR_IMAGE_PATH),
                                    size=(20, 20))
            
            image_label = ctk.CTkLabel(master=frame_2, width= 30, image=my_image, text="")
            image_label.grid(column = i, row = 0, sticky = "we")    
        
    def define_frame(self):
        
        self.frame_2 = ctk.CTkFrame(master=self.parent)
        self.frame_2.grid(column = 1, row = 0)
        self.frame_2.columnconfigure((0, 1), weight=1)
        self.frame_2.rowconfigure((0, 1, 2, 3, 4), weight=1, minsize=20)
        
    
    def define_header(self):
        frame_3 = ctk.CTkFrame(master=self.frame, fg_color= "white", width = 600, height = 40)
        frame_3.pack(expand = True)
        ctk.CTkButton(master=frame_3, text = "Recipe", hover_color="red", width = 150, 
                      border_color="white", border_width=2, command=lambda: print("Button")).pack(side = "left")
        ctk.CTkButton(master=frame_3, text = "Author", hover_color="red", width = 150, 
                      border_color="white", border_width=2, command=lambda: print("Button")).pack(side = "left")
        ctk.CTkButton(master=frame_3, text = "Date ", hover_color="red", width = 150, 
                      border_color="white", border_width=2, command=lambda: print("Button")).pack(side = "left")
        ctk.CTkButton(master=frame_3, text = "Rating", hover_color="red", width = 150, 
                      border_color="white", border_width=2, command=lambda: print("Button")).pack(side = "left")

    def define_scrollable_frame(self): 
        # create frames 
        self.frame = ctk.CTkScrollableFrame(master=self.parent, width = 600, height=400, fg_color="white")
        self.frame.grid(column = 0, row = 0)    
        self.define_header()
    
    def create_entries(self): 
        self.entry_1 = ctk.CTkEntry(self.frame_2)
        self.entry_2 = ctk.CTkEntry(self.frame_2)
        
    def create_combobox(self):
        self.combobox_1 = ctk.CTkComboBox(self.frame_2, variable=self.combvars[0])
        self.combobox_2 = ctk.CTkComboBox(self.frame_2, values=Parser.MEASUREMENT_OPTIONS,variable=self.combvars[1])

    def create_buttons(self):
        # define 4 Buttons for the header

        self.button_4 = ctk.CTkButton(master = self.frame, text = "Pasta Carbonara", hover_color="red",
                                      fg_color="white", text_color="black", command=lambda: print("yes"))
        self.button_7 = ctk.CTkButton(master=self.frame_2, text= "Change Name", hover_color="red")
        
        self.button_8 = ctk.CTkButton(master=self.frame_2, text= "Remove Ingredient", hover_color="red")
        
        self.button_9 = ctk.CTkButton(master=self.frame_2, text= "Apply Changes ", hover_color="red")
        
    def create_labels(self):
        # labels for editor menu
        self.label_5 = ctk.CTkLabel(master=self.frame_2, text= "Recipe Name", text_color="white")
        self.label_6 = ctk.CTkLabel(master=self.frame_2, text= "Ingredients", text_color="white")
        self.label_7 = ctk.CTkLabel(master=self.frame_2, text= "Amount", text_color="white")
        self.label_8 = ctk.CTkLabel(master=self.frame_2, text= "Measurement", text_color="white")

    def place_entries(self):
        self.entry_1.grid(column = 0, row = 1, padx = 10, pady = 10)
        self.entry_2.grid(column = 0, row = 5, padx = 10, pady = 10)
        
    def place_combobox(self):
        self.combobox_1.grid(column = 0, row = 3, padx = 10, pady = 10)
        self.combobox_2.grid(column = 1, row = 5, padx = 10, pady = 10)
        
    def place_labels(self):
        # place main edit menu labels
        self.label_5.grid(column = 0, row = 0, padx = 10, pady = 10)
        self.label_6.grid(column = 0, row = 2, padx = 10, pady = 10)
        self.label_7.grid(column = 0, row = 4, padx = 10, pady = 10)
        self.label_8.grid(column = 1, row = 4, padx = 10, pady = 10)
        
    def place_buttons(self):
        # place on the scrollable frame 
        # self.button_4.grid(column = 1, row = 0, padx = 10, pady = 10)
        #         
        self.button_7.grid(column = 1, row = 1, padx = 10, pady = 10)
        self.button_8.grid(column = 1, row = 3, padx = 10, pady = 10)
        self.button_9.grid(column = 0, row = 7, padx = 10, pady = 10)

    def define_canvas(self):
        # add canvas to the frame 
        self.canvas = ctk.CTkCanvas(master = self.parent, height=300, width=600)

    def create_widgets(self):
        # create frames 
        self.define_frame()
        self.define_scrollable_frame()

        # define buttons
        self.create_buttons()

        # create labels
        self.create_labels()

        # create entries
        self.create_entries()
        
        # create combobox
        self.create_combobox()
        
        # define canvas 
        self.define_canvas()
        
        # place butt
        self.place_buttons()
        
        # place labels
        self.place_labels()

        # place entries
        self.place_entries()
        
        # place combobox
        self.place_combobox()

if __name__ == "__main__":
    Editor()

