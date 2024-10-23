import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter.scrolledtext import ScrolledText
import customtkinter as ctk
import os
import re
from parse_ingredients import Parser
from paths import FILE_PATH, INGREDIENT_FILE
from style_template import LIGHT_GREY

'''
TO DO: add a button which indicates when recipe is complete and can be added to the recipe list
- Add a search function so that each time you type in a word it looks for it in the list
- Make sure if the same ingredient is given twice either add to already existing one or throw an error
- Add possibility to remove a recipe from the list
- Possible to change the list of dictionaries to a dictionary which has the recipe name as the key and everything else
as the value
- remove ingredient at the start of the listbox entry 
''' 

MEASUREMENT_OPTIONS = ["Units (u)", "Grams (g)", "Mililiters (ml)", 
                           "Tea-Spoons (Tsp)", "Table-Spoons (Tbsp)"]

class Recipe(ctk.CTk, Parser):

    entries: list[ctk.CTkEntry]
    ingredient_list: list[str]
    recipe_list: dict[str : str]
    ingredients: list[str]
    listbox: tk.Listbox

    def __init__(self, parent) -> None:
        
        super(Recipe, self).__init__()

        # define parent window
        self.parent = parent

        #define instance variables
        self.flag: bool = False
        self.ingredients = []
        self.recipe_dict = {}
        self.amount: str = ""
        self.ingredient_list = self.parse_ingredients(FILE_PATH)

        # add font 
        self.bold = font.Font(family="Helvetica", name='appHighlightFont', size=10, weight='bold')

        #define string variables
        self.define_tkinter_variables()

        #parse the file
        #define widgets
        self.define_widgets()

    def define_widgets(self) -> None:
        """Function which defines all widgets in the GUI
        """
        #position self.entries 
        self.place_entries()
        #define the labels in the window
        self.define_labels()
        #define a button 
        self.define_buttons()
        #define a combobox
        self.define_combobox()
        #define a listbox
        self.define_listbox()
        #define a scrolledtext
        self.define_scrolledtext()

    def define_scrolledtext(self) -> None:
        """Defines a scrolled text widget to write recipe descriptions 
        """
        self.scrolled_text_widget = ctk.CTkTextbox(master = self.parent, width=400, height=100, fg_color="white", text_color="black")
        self.scrolled_text_widget.grid(row=8, column=3, padx=5, pady=10)

    def define_tkinter_variables(self) -> None:
        """defines all tkinter variables which are later used to acquire information from 
        """
        #define string variables
        self.ingredientsvar = tk.StringVar(value = self.ingredients)
        self.vars = [tk.StringVar() for var in range(10)]
        self.combvars = [tk.StringVar() for var in range(3)]

        #define the entries in the window
        self.entries = [ctk.CTkEntry(self.parent, textvariable=self.vars[i]) for i in range(6)]

    def reset_window(self) -> None:
        """reset function which resets the current window by deleting the any text and reseting the
        state of the buttons 
        """
        for widget in self.parent.winfo_children():
            if isinstance(widget, tk.Entry) or isinstance(widget, ttk.Combobox):
                widget.configure(state = "normal")
            if isinstance(widget, tk.Entry) or isinstance(widget, ttk.Combobox) or \
            isinstance(widget, tk.Listbox):
                widget.delete(0, "end")

    def place_entries(self) -> None:
        """defines the entries in the GUI
        """
        self.entries[0].grid(row = 0, column = 1, padx=5, pady=5)
        self.entries[1].grid(row = 4, column = 1, padx=5, pady=5)
        self.entries[2].grid(row = 5, column = 1, padx=5, pady=5)
        self.entries[3].grid(row = 1, column = 1, padx=5, pady=5)

    def define_labels(self) -> None:
        """defines and places labels on the GUI
        """
        #define the labels in the window
        ctk.CTkLabel(self.parent, text = "Ingredients: ").grid(row=0, column=3, padx=5, pady=5)
        ctk.CTkLabel(self.parent, text = "Description: ").grid(row=7, column=3, padx=0, pady=0)
        ctk.CTkLabel(self.parent, text = "Enter the recipe name: ").grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.parent, text = "Enter your name: ").grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.parent, text = "Enter the recipe category: ").grid(row=2, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.parent, text = "Enter the ingredient: ").grid(row=3, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.parent, text = "Enter the ingredient subcategory (optional): ").grid(row=4, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.parent, text = "Enter the amount: ").grid(row=5, column=0, padx=5, pady=5)

    def define_combobox(self) -> None:
        """Defines comboboxes for the GUI
        """
        #define a combobox
        self.c0 = ctk.CTkComboBox(self.parent, values=self.ingredient_list,  variable=self.combvars[0])
        self.c1 = ctk.CTkComboBox(self.parent, values=["breakfast", "dinner"], variable=self.combvars[1])
        self.c2 = ctk.CTkComboBox(self.parent, values = MEASUREMENT_OPTIONS, variable=self.combvars[2])
    
        # bind the first combobox to a search function
        self.c0.bind("<KeyRelease>", self.search)

        self.c0.grid(row = 3, column = 1)
        self.c1.grid(row = 2, column = 1)
        self.c2.grid(row = 5, column = 2, padx=5, pady=5)

    def define_header(self, parent_frame) -> None:
        frame_1 = ctk.CTkFrame(master = parent_frame, fg_color="white", bg_color="white",
                            width = 390, height = 30, corner_radius=20)
        frame_1.pack(expand = True)
        ctk.CTkLabel(master = frame_1, width = 125, corner_radius = 10, fg_color = LIGHT_GREY, text_color="black", 
        text = "Ingredient: ").pack(side="left")
        ctk.CTkLabel(master = frame_1, width = 125, corner_radius = 10, fg_color = LIGHT_GREY, text_color="black", 
        text = "Subcategory: ").pack(side = "left")
        ctk.CTkLabel(master = frame_1, width = 125, corner_radius = 10, fg_color = LIGHT_GREY, text_color="black", 
        text = "Amount: ").pack(side = "left")

    def define_listbox(self) -> None:
        """Define listbox onto the GUI
        """
        self.scrollable_frame = ctk.CTkScrollableFrame(master=self.parent, width= 400, height=100, fg_color="white")
        self.scrollable_frame.grid(row = 1, column = 3, rowspan = 6, padx = 50)
        self.define_header(parent_frame=self.scrollable_frame)


    def define_buttons(self) -> None:
        """Defines buttons onto the GUI
        """
        #define a button 
        button_0 = ctk.CTkButton(self.parent, text="Next ingredient", command=self.handle_button_press)
        button_1 = ctk.CTkButton(self.parent, text="Add to recipes", command=self.check_entry)
        button_0.grid(row = 8, column = 1, pady=10)
        button_1.grid(row = 8, column = 0, pady=10)

    def search(self, event):
        value = event.widget.get()
        if value == "":
            self.c0["values"] = self.ingredient_list
           
        else:
            data = []
            for item in self.ingredient_list:
                if value.lower() in item.lower():
                    data.append(item)
            self.c0["values"] = data

    def check_entry(self) -> None:
        self.parse_recipe_dictionary(self.recipe_dict)
        self.reset_window()

    def validate_input(self, input: str) -> bool:
        valid_pattern = r'^[a-zA-Z\s\.\,\?\!]+$'
        if not re.match(valid_pattern, input) and input != "":
            return False
        else:
            return True
        
    def add_to_scrollable_frame(self):
        frame_1 = ctk.CTkFrame(master = self.scrollable_frame, fg_color="white",
                            width = 390, height = 30, corner_radius=20)
        frame_1.pack(expand = True)
        ctk.CTkLabel(master=frame_1, width = 125, text=self.combvars[0].get(), 
        text_color="black").pack(side = "left")
        ctk.CTkLabel(master=frame_1, width = 125, text=self.vars[1].get(), 
        text_color="black").pack(side = "left")
        ctk.CTkLabel(master=frame_1, width = 125, text=self.amount, 
        text_color="black").pack(side = "left")

    def add_to_list(self) -> None:
        string_entry = f"ingredient: {self.combvars[0].get()} {self.vars[1].get()} {self.amount}"
        #updates the ingredients list asweel as the ingredientsvar
        self.ingredients.append(string_entry)
        print(string_entry)
        self.add_to_scrollable_frame()
        self.reset_window()

    def add_to_recipes(self) -> None:
        """Function which handles the button press "Next Ingredient"
        """
        if self.flag is False:
            # validate the variables 
            if not all([self.validate_input(var) for var in\
            [self.vars[0].get(), self.combvars[1].get()]]):
                messagebox.showwarning("Warning", "Do not use any special characters or numbers!")
                return
            
            self.recipe_dict["recipe"] = self.vars[0].get()
            self.recipe_dict["author"] = self.vars[3].get()
            self.recipe_dict["category"] = self.combvars[1].get()
            self.recipe_dict["description"] = self.scrolled_text_widget.get('1.0', 'end')
            self.recipe_dict["ingredients"] = []
            # disable the state of the self.entries and combobox
            self.entries[0].configure(state="disabled")
            self.c1.configure(state="disabled")
            self.flag = True

        # get the unit amount 
        unit = self.combvars[2].get().split(" ")
        unit = unit[1].replace("(", "").replace(")", "")
        self.amount = f"{self.vars[2].get()} {unit}"

        if not all([self.validate_input(var) for var in\
        [self.combvars[0].get(), self.vars[1].get()]]):
            messagebox.showwarning("Warning", "Do not use any special characters or numbers!")
            return

        entry_dictionary = {"ingredient" : self.combvars[0].get(), "subcategory" : self.vars[1].get(),
                            "amount" : self.amount}
        self.recipe_dict["ingredients"].append(entry_dictionary)

        # adds the recipe entry to the ingredients list 
        self.add_to_list()

    #after the button is pressed save the variable data in 
    #specific format and reset the inactive windows
    def handle_button_press(self, event = None) -> None:
        #once button is pressed save the variable data to the list
        if not os.path.exists(INGREDIENT_FILE):
            with open(INGREDIENT_FILE, 'w') as f:
                f.write('')  # create an empty file

        #if any of the fields are empty do not execute the function further just return 
        if any([var == "" for var in\
            [self.vars[0].get(), self.combvars[1].get(), self.combvars[0].get()]]):
            messagebox.showwarning("Warning", "Please fill in all fields!")
            return
        
        # creates a recipe entry in the dictionary 
        self.add_to_recipes()

        print(self.recipe_dict)

        [entry.delete(0, tk.END) for entry in self.entries[1:]]

if __name__ == "__main__":
    ui_instance = Recipe()