import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter.scrolledtext import ScrolledText
import os
from parse_ingredients import Parser
from paths import FILE_PATH, INGREDIENT_FILE

'''
TO DO: add a button which indicates when recipe is complete and can be added to the recipe list
- Make sure the amount is given is a number and better an integer
- Add a search function so that each time you type in a word it looks for it in the list
- Make sure that the recipe doesn't have any numbers in it 
- Make sure if the same ingredient is given twice either add to already existing one or throw an error
- Add possibility to remove a recipe from the list
- Possible to change the list of dictionaries to a dictionary which has the recipe name as the key and everything else
as the value
''' 

MEASUREMENT_OPTIONS = ["In Units (u)", "In Grams (g)", "In Mililiters (ml)", 
                           "In Tea-Spoons (Tsp)", "In Table-Spoons(Tbsp)"]

class UI():

    entries: list[tk.Entry]
    ingredient_list: list[str]
    recipe_list: dict[str : str]
    ingredients: str
    listbox: tk.Listbox


    def __init__(self) -> None:

        #create the main window 
        self.create_window()
        #define instance variables
        self.flag: bool = False
        self.ingredient_list = []
        self.ingredients = []
        self.recipe_dict = {}
        self.parser = Parser(INGREDIENT_FILE)
        self.amount: str = ""

        # add font 
        self.bold = font.Font(family="Helvetica", name='appHighlightFont', size=10, weight='bold')

        #define string variables
        self.define_tkinter_variables()

        #parse the file
        self.parse_ingredients(FILE_PATH)
        #define widgets
        self.define_widgets()
        # Start the event loop.
        self.window.mainloop()

    def define_widgets(self) -> None:
        '''
        function which defines all widgets in the GUI
        '''
        #define a scrollbar
        # self.define_scrollbar()
        #position self.entries 
        self.define_entries()
        #bind buttons
        self.bind_button()
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


    def create_window(self) -> None:
        '''
        creates the root window for the GUI
        '''
        self.window = tk.Tk()
        self.window.title("Recipe Book")

    def define_scrolledtext(self) -> None:
        self.scrolled_text_widget = ScrolledText(self.window, width=42, height=10)
        self.scrolled_text_widget.grid(row=8, column=3, padx=5, pady=10)

    # def define_scrollbar(self) -> None:
    #     '''
    #     defines a scrollbar widget 
    #     '''
    #      #create a scrollbar
    #     self.scrollbar = ttk.Scrollbar(self.window, orient=tk.VERTICAL)
    #     self.scrollbar.grid(row = 1, column = 3, sticky="ns")

    def define_tkinter_variables(self) -> None:
        '''
        defines all tkinter variables which are later used to acquire information from 
        '''
        #define string variables
        self.ingredientsvar = tk.StringVar(value = self.ingredients)
        self.vars = [tk.StringVar() for var in range(10)]
        self.combvars = [tk.StringVar() for var in range(3)]

        #define the entries in the window
        self.entries = [tk.Entry(self.window, textvariable=self.vars[i]) for i in range(5)]

    def reset_window(self) -> None:
        '''
        reset function which resets the current window by deleting the any text and reseting the
        state of the buttons 
        '''
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Entry) or isinstance(widget, ttk.Combobox):
                widget.config(state = "normal")
            if isinstance(widget, tk.Entry) or isinstance(widget, ttk.Combobox) or \
            isinstance(widget, tk.Listbox):
                widget.delete(0, "end")

    def define_entries(self) -> None:
        '''
        defines the entries in the GUI
        '''
        self.entries[0].grid(row = 0, column = 1, padx=5, pady=5)
        self.entries[1].grid(row = 3, column = 1, padx=5, pady=5)
        self.entries[2].grid(row = 4, column = 1, padx=5, pady=5)

    def define_labels(self) -> None:
        '''
        defines the labels in the GUI
        '''
        #define the labels in the window
        tk.Label(self.window, text = "Ingredients: ").grid(row=0, column=3, padx=5, pady=5)
        tk.Label(self.window, text = "Description: ").grid(row=7, column=3, padx=0, pady=0)
        tk.Label(self.window, text = "Enter the recipe name: ").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the recipe category: ").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the ingredient: ").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the ingredient subcategory (optional): ").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the amount: ").grid(row=4, column=0, padx=5, pady=5)

    def bind_button(self) -> None: 
        self.window.bind('<Return>', self.handle_button_press)

    def define_combobox(self) -> None:
        #define a combobox
        self.c0 = ttk.Combobox(self.window, values=self.ingredient_list,  textvariable=self.combvars[0])
        self.c1 = ttk.Combobox(self.window, values=["breakfast", "dinner"], textvariable=self.combvars[1])
        self.c2 = ttk.Combobox(self.window, values = MEASUREMENT_OPTIONS, textvariable=self.combvars[2])

        self.c0.grid(row = 2, column = 1)
        self.c1.grid(row = 1, column = 1)
        self.c2.grid(row = 4, column = 2, padx=5, pady=5)

    def define_listbox(self) -> None:
        # defines a listbox on the right side of the panel

        #create a scrollbar
        self.scrollbar = ttk.Scrollbar(self.window, orient=tk.VERTICAL)
        self.scrollbar.grid(row = 1, column = 3, sticky="ns")
        self.listbox = tk.Listbox(self.window, listvariable=self.ingredientsvar,
                                   height=10, width=50, font = self.bold)
        

        self.listbox.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.grid(row = 1, column = 3, rowspan = 6, padx = 50)
        self.scrollbar.grid(row = 1, column = 4, rowspan = 6, sticky="ns")

    def define_buttons(self) -> None:
        #define a button 
        button_0 = tk.Button(text="Next ingredient", command=self.handle_button_press)
        button_1 = tk.Button(text="Add to recipes", command=self.check_entry)
        button_0.grid(row = 7, column = 1, pady=10)
        button_1.grid(row = 7, column = 0, pady=10)

    def parse_ingredients(self, text: str) -> None:
        #open the file
        with open(text, "r", encoding="utf-8") as file:
            for line in file:
                self.ingredient_list.append(line.strip())

    def get_state(self, entry):
        pass

    def check_entry(self):
        self.parser.parse_recipe_dictionary(self.recipe_dict)
        self.reset_window()
        
    def add_to_list(self) -> None:
        string_entry = f"ingredient: {self.combvars[0].get()} {self.vars[1].get()}, {self.amount}"
        #updates the ingredients list asweel as the ingredientsvar
        self.ingredients.append(string_entry)
        print(string_entry)
        self.listbox.insert(tk.END, string_entry)

    def add_to_recipes(self) -> None:
        if self.flag is False:
            self.recipe_dict["recipe"] = self.vars[0].get()
            self.recipe_dict["category"] = self.combvars[1].get()
            self.recipe_dict["description"] = self.scrolled_text_widget.get('1.0', 'end_1c')
            self.recipe_dict["ingredients"] = []
            # disable the state of the self.entries and combobox
            self.entries[0].config(state="disabled")
            self.c1.config(state="disabled")
            self.flag = True

        # get the unit amount 
        unit = self.combvars[2].get().split(" ")
        unit = unit[2].replace("(", "").replace(")", "")
        self.amount = f"{self.vars[2].get()} {unit}"

        entry_dictionary = {"ingredient" : self.combvars[0].get(), "subcategory" : self.vars[1].get(),
                            "amount" : self.amount}
        self.recipe_dict["ingredients"].append(entry_dictionary)

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
        
        self.add_to_recipes()

        self.add_to_list()

        print(self.recipe_dict)

        [entry.delete(0, tk.END) for entry in self.entries[1:]]

        #disable the buttons and self.entries and clear them 

if __name__ == "__main__":
    ui_instance = UI()