import yaml
import tkinter as tk
from tkinter import ttk
from tkinter import font
import customtkinter as ctk
from paths import INGREDIENT_FILE
from style_template import ENTRY_COLOR, LABEL_COLOR, BUTTON_COLOR


'''
- use customtkinter and ttkbootstrap to style 

TO DO:
- Create a mapping of recipe name to recipe entry 
- Issue with similar entries which have same ingredient but different units 
'''

class Tab_1(ctk.CTk):

    def __init__(self, parent) -> None:

        super().__init__()

        # define frame 
        parent.columnconfigure((0, 1, 2, 3), weight = 1)
        parent.rowconfigure((0, 1, 2, 3), weight = 1)

        # define labels
        self.create_labels(parent)

        # define entries 
        self.create_entries(parent)

        # define buttons
        self.create_buttons(parent)
    
    def create_buttons(self, parent):
        ctk.CTkButton(master = parent, text = "Open Editor", hover_color="red", fg_color=BUTTON_COLOR, 
                      border_color="white", border_width = 2, command=self.open_meal_plan).grid(column = 0, row = 3)

    def create_entries(self, parent):
        ctk.CTkEntry(master = parent, fg_color = ENTRY_COLOR).grid(column = 0, row = 1)
        ctk.CTkEntry(master = parent, fg_color = ENTRY_COLOR).grid(column = 1, row = 1)

    def create_labels(self, parent):
        ctk.CTkLabel(master = parent, corner_radius = 5, fg_color= LABEL_COLOR, text="Amount of Days").grid(column = 0, row = 0)
        ctk.CTkLabel(master = parent, corner_radius = 5, fg_color = LABEL_COLOR, text="Meals per Day").grid(column = 1, row = 0)

    def open_meal_plan(self):
        grocceries = Grocceries()     


class Grocceries():

    recipe_list: list[str]
    recipe_map: dict[str : int]
    recipe_amount: dict[str : int]
    ingredient_dict: dict[str : int]
    recipes: dict

    def __init__(self) -> None:
        #create the main window 
        self.window = tk.Tk()
        self.window.title("Groccery list")

        #list of recipes
        self.recipes = {}
        self.recipe_map = {}
        self.recipe_list = []
        self.recipe_amount = {}
        self.ingredient_dict = {}
        self.combvars = [tk.StringVar() for var in range(21)]

        # add font 
        self.bold = font.Font(family="Helvetica", name='appHighlightFont', size=10, weight='bold')

        #generate recipe list
        self.generate_entries()

        self.define_buttons()
        self.define_combobox()
        self.define_labels()

        # Start the event loop.
        self.window.mainloop()

    def define_buttons(self):
        #define a button 
        button_0 = tk.Button(text="Generate List", command=self.generate_grocceries)
        button_0.grid(row = 7, column = 1, pady=10)

    def define_combobox(self) -> None:
        #define a combobox
        for i in range(21):
            ttk.Combobox(self.window, values=self.recipe_list, textvariable = self.combvars[i])\
            .grid(row = i%3 + 1, column = i%7 + 1, padx = 5, pady= 5)

    def define_labels(self) -> None:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i in range(7):
            tk.Label(self.window, text = days[i]).grid(row=0, column=i + 1, padx=5, pady=5)

        times = ["Breakfast", "Lunch", "Dinner"]
        for i in range(3):
            tk.Label(self.window, text = times[i]).grid(row=i+1, column=0, padx=5, pady=5)

    def generate_entries(self):
        with open(INGREDIENT_FILE, "r") as file:
            self.recipes = yaml.safe_load(file)
        self.recipe_name_to_recipe(self.recipes)
        self.recipe_list = [recipe["recipe"] for recipe in self.recipes]

    def recipe_name_to_recipe(self, recipes: list):
        for index, entry in enumerate(recipes):
            self.recipe_map[entry["recipe"]] = index

    def generate_groccerie_list(self):
        toplevel = tk.Toplevel(self.window)
        toplevel.title("Groccerie List")
        toplevel.geometry("300x200") 
        w = tk.Label(toplevel, text ='Generated List: ', font = self.bold) 
        w.pack() 
        item_list = [f"- {value} {key[0]} {key[1]} \n" for value, key in self.ingredient_dict.items()]
        groccerie_list = "".join(item_list)
        display_text = tk.StringVar(value=groccerie_list)
        f = tk.Message(toplevel, textvariable=display_text, font=self.bold)
        f.pack()

    def generate_grocceries(self):
        self.sort_grocceries()
        print(self.recipe_amount)
        for key, value in self.recipe_amount.items():
            # get the recipe index from the recipe map for a given key
            recipe_index = self.recipe_map[key]
            # get the recipe at the given index 
            recipe = self.recipes[recipe_index]
            ingredients = recipe["ingredients"]
            for i in range(value):
                self.parse_ingredients(ingredients)

        self.generate_groccerie_list()

    def parse_ingredients(self, ingredients):
        for ingredient in ingredients:
            ingredient_name = ingredient["ingredient"] + ingredient["subcategory"]
            # get the amount for an ingredient by splitting it
            ingredient_amount = ingredient["amount"].split(" ")
            ingredient_amount[0] = int(ingredient_amount[0])
            if ingredient_name in self.ingredient_dict.keys():
                amount = self.ingredient_dict[ingredient_name]
                if ingredient_amount[1] == amount[1]:
                    amount[0] += ingredient_amount[0]
                    self.ingredient_dict[ingredient_name] = amount
                else:
                    amount[0] += ingredient_amount[0]
                    self.ingredient_dict[ingredient_name] = amount
            else:
                self.ingredient_dict[ingredient_name] = ingredient_amount

        print(self.ingredient_dict)

    def sort_grocceries(self):
        for recipe in self.combvars:
            # if the recipe is not in the dictionary -> create dictionary entry 
            if recipe.get() in self.recipe_amount:
                self.recipe_amount[recipe.get()] += 1
            elif recipe.get() != "":
                self.recipe_amount[recipe.get()] = 1
            # else increase the ammount of the recipe occurance 

if __name__ == "__main__":
    grocceries = Grocceries()