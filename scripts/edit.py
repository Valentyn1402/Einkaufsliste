import tkinter as tk
from tkinter import ttk
from tkinter import font
from parse_ingredients import Parser
from paths import STAR_IMAGE_PATH
from PIL import Image
import customtkinter as ctk


'''
create a dictionary which maps the entries of the list entries to recipe names 

'''

class Editor(ctk.CTk, Parser):


    def __init__(self, parent) -> None: 
        # initialize the dunder method 
        super(Editor, self).__init__()
        # ctk.set_appearance_mode("dark")

        self.parent_frame: tk.Frame = None

        self.current_recipe: str = None

        self.current_ingredients: dict[str, list[str]] = {}
 
        # loads yaml data to Parser.yaml_dictionary
        self.load_yaml_data()
        
        # load recipe names to recipe dictionary 
        self.recipe_names_to_recipes()

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
        self.vars = [tk.StringVar() for var in range(2)]

    def define_grid(self):
        # define grid for the window
        self.parent.columnconfigure(0, weight=2)
        self.parent.columnconfigure(1, weight=1)

    def highlight_frame(self, event: tk.Event):
        if isinstance(event.widget, tk.Label):
            label_path = event.widget.winfo_parent()
            # Split the path into components
            path_components = label_path.split('.')
    
            # Remove the last component to get the parent path
            parent_path_components = path_components[:-1]
            
            # Reconstruct the parent path
            parent_path = ".".join(parent_path_components)

            # get the parent widget (frame widget)
            parent_widget = self.parent.nametowidget(parent_path)

            # retrieve the first widget in the row 
            label_widget = parent_widget.grid_slaves(column = 0, row = 0)


            # get the label widget at row = 0, column = 0
            label = label_widget[0]
            print(label.cget("text"))            

            # reset the hightlight from everything else 
            if self.parent_frame is not None:
                self.highlight_frame_widgets(color="white", frame_path=self.parent_frame)

            # highlight everything in the frame 
            self.highlight_frame_widgets(color = "red", frame_path=parent_widget)

            self.load_recipe_data(recipe_name=label.cget("text"))

            label_name = label.cget("text")
            print(len(Parser.name_to_recipe))
            
            self.current_recipe = label.cget("text")

            self.parent_frame = parent_widget

    def load_widgets(self, event):
        ingredient_name = self.combobox_1.get()
        amount, unit = self.current_ingredients[ingredient_name]
        self.vars[1].set(amount)
        self.combobox_2.set(Parser.MEASUREMENT_MAP[unit])

    def load_recipe_data(self, recipe_name: str):

        recipe = Parser.name_to_recipe[recipe_name]
        # self.entry_1.configure(text = recipe_name)
        self.vars[0].set(recipe_name)
        value_list: list[str] = []

        # create a dictionary which maps the ingredients to the correspoding amounts 
        ingredients = recipe["ingredients"]
        for ingredient in ingredients:
            name = ingredient["ingredient"]
            amount, unit = ingredient["amount"].split()
            self.current_ingredients[name] = [amount, unit]
            value_list.append(name)

        self.combobox_1.configure(values = value_list)


    def highlight_frame_widgets(self, color: str, frame_path: tk.Frame):
        frame_path.configure(fg_color = color)
        children_widgets = frame_path.winfo_children()
        for child_widget in children_widgets:
            child_widget.configure(fg_color = color)


    def add_recipes_to_list(self):
        for recipe_entry in Parser.yaml_dictionary:
            recipe_name = recipe_entry["recipe"]
            recipe_author = recipe_entry["author"]
            recipe_date = recipe_entry["date"]
            rating = recipe_entry["rating"]
            frame = ctk.CTkFrame(master=self.frame, corner_radius= 5, width=600, height=40, fg_color="white")
            frame.pack(expand = True, fill = "x")
            frame.bind("<Button-1>", self.highlight_frame)
            label_1 = ctk.CTkLabel(master=frame, corner_radius= 5, text= recipe_name, 
                         text_color="black", width = 150, fg_color="white")
            label_1.grid(column = 0, row = 0, sticky = "ew")
            label_1.bind("<Button-1>", self.highlight_frame)
            label_2 = ctk.CTkLabel(master=frame, corner_radius= 5, width = 150, text= recipe_author, 
                         text_color="black", fg_color="white")
            label_2.grid(column = 1, row = 0, sticky = "ew")
            label_2.bind("<Button-1>", self.highlight_frame)
            label_3 = ctk.CTkLabel(master=frame, corner_radius= 5, width = 150, text= recipe_date, 
                         text_color="black", fg_color="white")
            label_3.grid(column = 2, row = 0, sticky = "ew")
            label_3.bind("<Button-1>", self.highlight_frame)
            self.add_rating(frame = frame, size = rating)
           
    def add_rating(self, frame: tk.Frame, size: int = 5):
        frame_2 = ctk.CTkFrame(master=frame, width = 150, fg_color="white", bg_color="white",
                               height = 40)
        frame_2.grid(column = 3, row = 0, sticky = "we")
        frame_2.bind("<Button-1>", self.highlight_frame)
        # frame_2.columnconfigure((0, 1, 2, 3, 4), weight = 1)

        for i in range(size):
            my_image = ctk.CTkImage(light_image=Image.open(STAR_IMAGE_PATH),
                                    dark_image=Image.open(STAR_IMAGE_PATH),
                                    size=(20, 20))
            
            image_label = ctk.CTkLabel(master=frame_2, corner_radius=5, width= 30, image=my_image, text="")
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
        self.entry_1 = ctk.CTkEntry(self.frame_2, textvariable=self.vars[0])
        self.entry_2 = ctk.CTkEntry(self.frame_2, textvariable=self.vars[1])
        
    def create_combobox(self):
        self.combobox_1 = ctk.CTkComboBox(self.frame_2, variable=self.combvars[0], command= self.load_widgets)
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

