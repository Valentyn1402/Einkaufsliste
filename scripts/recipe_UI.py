import tkinter as tk
from tkinter import messagebox
from tkinter import font
from validation import validate_input_number, validate_input_string
import datetime
import os
import re
import customtkinter as ctk
from parse_ingredients import Parser
from paths import FILE_PATH, INGREDIENT_FILE
from style_template import LIGHT_GREY, BLUE_COLOR

'''
TO DO: add a button which indicates when recipe is complete and can be added to the recipe list
- Add a search function so that each time you type in a word it looks for it in the list
- Make sure if the same ingredient is given twice either add to already existing one or throw an error
- Add possibility to remove a recipe from the list
- Possible to change the list of dictionaries to a dictionary which has the recipe name as the key and everything else
as the value
- remove ingredient at the start of the listbox entry 
''' 

class Recipe(ctk.CTk, Parser):

    entries: list[ctk.CTkEntry]
    ingredient_list: list[str]
    recipe_list: dict[str : str]
    ingredients: list[str]
    listbox: tk.Listbox

    def __init__(self, parent: ctk.CTkFrame) -> None:
        
        super(Recipe, self).__init__()

        # define parent window
        self.parent = parent

        # define a frame 
        self.parent_frame: tk.Frame = None
        #define instance variables
        self.flag: bool = False
        self.ingredients = []
        self.recipe_dict = {}
        self.amount: str = ""
        self.ingredient_list = self.parse_ingredients(FILE_PATH)
        self.current_label: tk.Label = None

        #define string variables
        self.define_tkinter_variables()

        #define widgets
        self.define_widgets()
        
        # set taborder in the app   
        self.define_taborder()

    def define_widgets(self) -> None:
        """function which defines all widgets in the GUI
        """
        # define entries 
        self.define_entries()
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
        #position self.entries 
        self.place_entries()
    
    def define_taborder(self) -> None:
        # reverse the stacking order to show how
        # it affects tab order
        new_order = (self.entries[0], self.entries[3], self.c1, self.c0, self.entries[1], self.entries[2], self.c2)
        for widget in new_order:
            widget.lift()

    def define_tkinter_variables(self) -> None:
        """defines all tkinter variables which are later used to acquire information from 
        """
        #define string variables
        self.ingredientsvar = tk.StringVar(value = self.ingredients)
        self.vars = [tk.StringVar() for var in range(10)]
        self.combvars = [tk.StringVar() for var in range(3)]

    def define_entries(self) -> None:
        """defines entry widgets for the GUI
        """
        #define the entries in the window
        self.entries = [ctk.CTkEntry(self.parent, placeholder_text_color = "white", textvariable=self.vars[i]) for i in range(6)]

    def define_scrolledtext(self) -> None:
        """defines a scrolled text widget to write recipe descriptions 
        """
        self.scrolled_text_widget = ctk.CTkTextbox(master = self.parent, width=400, height=100, fg_color="white", text_color="black")
        self.scrolled_text_widget.grid(row=8, column=3, padx=5, pady=10)

    def define_labels(self) -> None:
        """defines and places labels which are going to be place on the GUI
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
        """defines comboboxes for the GUI
        """
        #define a combobox
        self.c0 = ctk.CTkComboBox(self.parent, text_color_disabled="white", values=self.ingredient_list,  variable=self.combvars[0])
        self.c1 = ctk.CTkComboBox(self.parent, text_color_disabled="white", values=["breakfast", "dinner"], variable=self.combvars[1])
        self.c2 = ctk.CTkComboBox(self.parent, text_color_disabled="white", values = Parser.MEASUREMENT_OPTIONS, variable=self.combvars[2])
    
        # bind the first combobox to a search function
        self.c0.bind("<KeyRelease>", self.search)

        self.c0.grid(row = 3, column = 1)
        self.c1.grid(row = 2, column = 1)
        self.c2.grid(row = 5, column = 2, padx=5, pady=5)

    def define_buttons(self) -> None:
        """defines buttons onto the GUI
        """
        #define a button 
        button_0 = ctk.CTkButton(self.parent, text="Next ingredient", command=self.handle_button_press)
        button_1 = ctk.CTkButton(self.parent, text="Add to recipes", command=self.check_entry)
        button_2 = ctk.CTkButton(self.parent, text="Apply Changes", command=self.change_ingredient_values)
        button_0.grid(row = 8, column = 1, pady=10)
        button_1.grid(row = 8, column = 0, pady=10)
        button_2.grid(row = 8, column = 2, pady=10)
        

    def define_listbox(self) -> None:
        """Define listbox onto the GUI
        """
        self.scrollable_frame = ctk.CTkScrollableFrame(master=self.parent, width= 400, height=100, fg_color="white")
        self.scrollable_frame.grid(row = 1, column = 3, rowspan = 6, padx = 50)
        self.define_header(parent_frame=self.scrollable_frame)

    def define_header(self, parent_frame) -> None:
        frame_1 = ctk.CTkFrame(master = parent_frame, fg_color="white", bg_color="white",
                            width = 390, height = 30, corner_radius=20)
        frame_1.pack(expand = True)
        ctk.CTkLabel(master = frame_1, width = 125, corner_radius= 5, fg_color = BLUE_COLOR, text_color="white", 
        text = "Ingredient: ").pack(side="left", padx = 3)
        ctk.CTkLabel(master = frame_1, width = 125, corner_radius= 5, fg_color = BLUE_COLOR, text_color="white", 
        text = "Subcategory: ").pack(side = "left", padx = 3)
        ctk.CTkLabel(master = frame_1, width = 125, corner_radius= 5, fg_color = BLUE_COLOR, text_color="white", 
        text = "Amount: ").pack(side = "left", padx = 3)

    def place_entries(self) -> None:
        """defines the entries in the GUI
        """
        self.entries[0].grid(row = 0, column = 1, padx=5, pady=5)
        self.entries[1].grid(row = 4, column = 1, padx=5, pady=5)
        self.entries[2].grid(row = 5, column = 1, padx=5, pady=5)
        self.entries[3].grid(row = 1, column = 1, padx=5, pady=5)

    def remove_ingredients(self) -> None:
        widgets = self.scrollable_frame.winfo_children()
        for widget in widgets[1:]:
            widget.destroy()

    def reset_window(self) -> None:
        """reset function which resets the current window by deleting the any text and reseting the
        state of the buttons 
        """
        for widget in self.parent.winfo_children():
            if isinstance(widget, ctk.CTkTextbox):
                widget.delete('1.0', 'end')  # Clear the content of CTkTextbox
            elif isinstance(widget, ctk.CTkEntry):
                widget.configure(state = "normal")
                widget.delete(0, "end")  # Clear the content of CTkEntry
            elif isinstance(widget, ctk.CTkFrame):
                self.remove_ingredients()
            elif isinstance(widget, ctk.CTkComboBox):
                widget.configure(state="normal")  # Set the state to normal
                widget.set("")

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
        # add a message for the user
        messagebox.showinfo("Info", "Recipe has been added")
        self.reset_window()
        # reset the dictionary
        self.recipe_dict.clear()
        # reset the flag
        self.flag = False

    def validate_input(self, input: str) -> bool:
        valid_pattern = r'^[a-zA-Z\s\.\,\?\!]+$'
        if not re.match(valid_pattern, input) and input != "":
            return False
        else:
            return True
        
    def highlight_frame_widgets(self, color: str, frame_path: tk.Frame):
        frame_path.configure(fg_color = color)
        children_widgets = frame_path.winfo_children()
        for child_widget in children_widgets:
            child_widget.configure(fg_color = color)
        
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
            self.current_label = label_widget[0]

            # reset the hightlight from everything else 
            if self.parent_frame is not None:
                self.highlight_frame_widgets(color="white", frame_path=self.parent_frame)

            # highlight everything in the frame 
            self.highlight_frame_widgets(color = "red", frame_path=parent_widget)

            # load recipe data to the widget fields
            self.load_recipe_data(parent=parent_widget)
            
            print("clicked on a label", parent_widget)

            self.parent_frame = parent_widget

    def load_recipe_data(self, parent: tk.Widget) -> None:
        # retrieve the first widget in the row 
        ingredient_amount, ingredient_subcategory, ingredient_name = parent.grid_slaves(row = 0)
        print(ingredient_amount.cget("text"))
        # unpack the amout and units into two variables 
        amount, unit = ingredient_amount.cget("text").split()
        # set the widgets to the ingredient values 
        self.c2.set(value = Parser.MEASUREMENT_MAP[unit])
        self.c0.set(value = ingredient_name.cget("text"))
        self.vars[1].set(value = ingredient_subcategory.cget("text"))
        self.vars[2].set(value = amount)

    def change_ingredient_values(self) -> None:
        # get the unit
        unit = self.c2.get()
        # get the unit
        ingredient = self.c0.get()
        # get the subcategory 
        subcategory = self.vars[1].get()
        # get the amount
        amount = self.vars[2].get()
        # unpack labels from the parent frame 
        amount_label, subcategory_label, name_label = self.parent_frame.grid_slaves(row = 0)
        # set labels to the current values in the widgets
        unit = Parser.BIDIRECT_MEASUREMENT_MAP[unit]
        amount = f"{amount} {unit}"

        name_label.configure(text = ingredient)
        subcategory_label.configure(text = subcategory)
        amount_label.configure(text = amount)

         
    def add_to_scrollable_frame(self):
        frame_1 = ctk.CTkFrame(master = self.scrollable_frame, fg_color="white",
                            width = 390, height = 30, corner_radius=20)
        frame_1.pack(expand = True)
        label_1 = ctk.CTkLabel(master=frame_1, width = 125, text=self.combvars[0].get(), 
        text_color="black")
        label_1.grid(column = 0, row = 0, sticky = "ew")
        label_1.bind("<Button-1>", self.highlight_frame)
        label_2 = ctk.CTkLabel(master=frame_1, width = 125, text=self.vars[1].get(), 
        text_color="black")
        label_2.grid(column = 1, row = 0, sticky = "ew")
        label_2.bind("<Button-1>", self.highlight_frame)
        label_3 = ctk.CTkLabel(master=frame_1, width = 125, text=self.amount, 
        text_color="black")
        label_3.grid(column = 2, row = 0, sticky = "ew")
        label_3.bind("<Button-1>", self.highlight_frame)

    def add_to_list(self) -> None:
        string_entry = f"ingredient: {self.combvars[0].get().lower()} {self.vars[1].get().lower()} {self.amount}"
        #updates the ingredients list asweel as the ingredientsvar
        self.ingredients.append(string_entry)
        print(string_entry)
        self.add_to_scrollable_frame()

        # reset the entry fields 
        self.vars[1].set("")
        self.vars[2].set("")
        self.c2.set("")

    def get_date(self) -> str:
        current_date = datetime.date.today()
        return current_date.strftime("%Y-%m-%d")
    
    def initialize_recipe_dictionary(self) -> None:
        """Initializes the recipe dictionary with the provided input values."""
        self.recipe_dict["recipe"] = self.vars[0].get()
        self.recipe_dict["author"] = self.vars[3].get()
        self.recipe_dict["category"] = self.combvars[1].get()
        self.recipe_dict["description"] = self.scrolled_text_widget.get('1.0', 'end')
        self.recipe_dict["date"] = self.get_date()
        self.recipe_dict["rating"] = 0
        self.recipe_dict["ingredients"] = []
        
    def disable_initial_inputs(self) -> None: 
        """disables the initial widgets, which cannot be changed during the adding recipe process  
        """
        # disable the state of the self.entries and combobox
        self.entries[0].configure(state=tk.DISABLED)
        self.entries[3].configure(state=tk.DISABLED)
        self.c1.configure(state=tk.DISABLED)

    def validate_inputs(self) -> None:
        # validate string entries 
        validate_input_string(input_string = self.vars[0].get())
        validate_input_string(input_string = self.vars[1].get())
        validate_input_string(input_string = self.vars[3].get())
        # validate number entries 
        validate_input_number(input_number = self.vars[2].get())
        # check if the 

    def add_to_recipes(self) -> None:
        """Function which handles the button press "Next Ingredient"
        """
        # check if the flag is set, that means the base for the recipe dictionary is initialized 
        if not self.flag:
            # validate the variables 
            self.validate_inputs()
            # initialize recipe dictionary
            self.initialize_recipe_dictionary()
            # disable the state of the self.entries and combobox
            self.disable_initial_inputs()
            # set flag to true
            self.flag = True

        # get the unit amount 
        unit = self.combvars[2].get().split(" ")
        unit = unit[1].replace("(", "").replace(")", "")
        self.amount = f"{self.vars[2].get()} {unit}"

        # validate inputs before adding to the recipe list
        self.validate_inputs()

        entry_dictionary = {"ingredient" : self.combvars[0].get().lower(), "subcategory" : self.vars[1].get().lower(),
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

        # removes the data from the subcategory and amount entries 

if __name__ == "__main__":
    ui_instance = Recipe()