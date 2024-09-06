import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from parse_ingredients import Parser
from paths import FILE_PATH, INGREDIENT_FILE
'''
TO DO: add a button which indicates when recipe is complete and can be added to the recipe list
add a visible window which show all already ingredients 
- Make sure the amount is given is a number and better an integer
- Make sure that the recipe doesn't have any numbers in it 
- Make sure if the same ingredient is given twice either add to already existing one or throw an error
- Make sure that the igredient list is a list of dictionaries
- Possibility to add a description of the recipe if you forget or to remind 
''' 
class UI():

    entries: list[tk.Entry]
    ingredient_list: list[str]
    recipe_list: dict[str : str]
    ingredients: str
    listbox: tk.Listbox

    def __init__(self) -> None:

        #create the main window 
        self.window = tk.Tk()
        self.window.title("Recipe Book")
        
        #define instance variables
        self.flag: bool = False
        self.i = 0
        self.ingredient_list = []
        self.ingredients = []
        self.recipe_dict = {}
        self.parser = Parser(INGREDIENT_FILE)

        #convert ingredients to StringVar
        self.ingredientsvar = tk.StringVar(value = self.ingredients)

        #parse the file
        self.parse_ingredients(FILE_PATH)

        #define string variables for the entries 
        self.vars = [tk.StringVar() for var in range(10)]
        self.combvar = tk.StringVar()
        self.combvar1 = tk.StringVar()

        #define the entries in the window
        self.entries = [tk.Entry(self.window, textvariable=self.vars[i]) for i in range(5)]

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
    
        # Start the event loop.
        self.window.mainloop()

    def define_entries(self) -> None:
        self.entries[0].grid(row = 0, column = 1, padx=5, pady=5)
        self.entries[1].grid(row = 3, column = 1, padx=5, pady=5)
        self.entries[2].grid(row = 4, column = 1, padx=5, pady=5)
        self.entries[3].grid(row = 5, column = 1, padx=5, pady=5)
        self.entries[4].grid(row = 6, column = 1, padx=5, pady=5)

    def define_labels(self) -> None:
        #define the labels in the window
        tk.Label(self.window, text = "Ingredients: ").grid(row=0, column=3, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the recipe name: ").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the recipe category: ").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the ingredient: ").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the ingredient subcategory (optional): ").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the amount: ").grid(row=4, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "in g").grid(row = 4, column = 2)
        tk.Label(self.window, text = "in ml").grid(row = 5, column = 2)
        tk.Label(self.window, text = "in units").grid(row = 6, column= 2)

    def bind_button(self) -> None: 
        self.window.bind('<Return>', self.handle_button_press)

    def define_combobox(self) -> None:
        #define a combobox
        self.c0 = ttk.Combobox(self.window, values=self.ingredient_list,  textvariable=self.combvar)
        self.c1 = ttk.Combobox(self.window, values=["breakfast", "dinner"], textvariable=self.combvar1)

        self.c0.grid(row = 2, column = 1)
        self.c1.grid(row = 1, column = 1)

    def define_listbox(self) -> None:
        # defines a listbox on the right side of the panel
        self.listbox = tk.Listbox(self.window, listvariable=self.ingredientsvar, height=10, width=40)
        self.listbox.grid(row = 1, column = 3, rowspan = 6, padx = 50)

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
        
    def add_to_list(self) -> None:
        string_entry = f"ingredient: {self.combvar.get()} subcategory: {self.vars[1].get()}"
        amount = ""
        #check which ammount is added
        if self.vars[2].get() != "":
            amount = "amount: " + self.vars[2].get() + " g \n"
        elif self.vars[3].get() != "":
            amount = "amount: " + self.vars[3].get() + " ml \n"
        elif self.vars[4].get() != "":
            amount = "ammount: " + self.vars[4].get() + " units \n"

        string_entry += amount 
        #updates the ingredients list asweel as the ingredientsvar
        self.ingredients.append(string_entry)
        print(string_entry)
        self.listbox.insert(tk.END, string_entry)

    def add_to_recipes(self) -> None:
        if self.flag is False:
            self.recipe_dict["recipe"] = self.vars[0].get()
            self.recipe_dict["category"] = self.combvar1.get()
            self.recipe_dict["ingredients"] = []
            # disable the state of the self.entries and combobox
            self.entries[0].config(state="disabled")
            self.c1.config(state="disabled")
            self.flag = True

        ingredient = {"ingredient " : self.combvar.get()}
        subcategory = {"subcategory " : self.vars[1].get()}
        if self.vars[2].get() != "":
            amount = f"{self.vars[2].get()} g"
        elif self.vars[3].get() != "":
            amount = f"{self.vars[3].get()} ml"
        elif self.vars[4].get() != "":
            amount = f"{self.vars[4].get()} units"

        entry_dictionary = {"ingredient" : self.combvar.get(), "subcategory" : self.vars[1].get(),
                            "amount" : amount}
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
            [self.vars[0].get(), self.combvar1.get(), self.combvar.get()]]):
            messagebox.showwarning("Warning", "Please fill in all fields!")
            return
        
        self.add_to_recipes()

        self.add_to_list()

        print(self.recipe_dict)

        [entry.delete(0, tk.END) for entry in self.entries[1:]]

        #disable the buttons and self.entries and clear them 

if __name__ == "__main__":
    ui_instance = UI()