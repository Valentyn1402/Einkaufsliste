import yaml
import tkinter as tk
from PIL import Image
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

    meal_amount: tk.StringVar
    day_amount: tk.StringVar

    def __init__(self, parent) -> None:

        super().__init__()

        # define integer variables
        self.meal_amount = tk.StringVar()
        self.day_amount = tk.StringVar()

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
        ctk.CTkEntry(master = parent, fg_color = ENTRY_COLOR, textvariable=self.day_amount).grid(column = 0, row = 1)
        ctk.CTkEntry(master = parent, fg_color = ENTRY_COLOR, textvariable=self.meal_amount).grid(column = 1, row = 1)

    def create_labels(self, parent):
        ctk.CTkLabel(master = parent, corner_radius = 5, fg_color= LABEL_COLOR, text="Amount of Days").grid(column = 0, row = 0)
        ctk.CTkLabel(master = parent, corner_radius = 5, fg_color = LABEL_COLOR, text="Meals per Day").grid(column = 1, row = 0)

    def open_meal_plan(self):
        Grocceries(self.meal_amount, self.day_amount)   

class Grocceries(ctk.CTkToplevel):

    recipe_list: list[str]
    recipe_map: dict[str : int]
    recipe_amount: dict[str : int]
    ingredient_dict: dict[str : int]
    recipes: dict

    def __init__(self, meal_amount: tk.StringVar, day_amount: tk.StringVar) -> None:

        super().__init__()
        #create the main window 
        self.title("Groccery list")
        self.resizable(False, False)
        # self.geometry("500x400")

        #list of recipes
        self.recipes = {}
        self.recipe_map = {}
        self.recipe_list = []
        self.recipe_amount = {}
        self.ingredient_dict = {}
        self.combvars = [tk.StringVar() for var in range(21)]

        # retrieve integers from the meal_amount and day_amount 
        values = self.retrieve_integers(meal_amount, day_amount)
        self.meal_amount = values[0]
        self.day_amount = values[1]

        # add font 
        # self.bold = font.Font(family="Helvetica", name='appHighlightFont', size=10, weight='bold')

        #generate recipe list
        self.generate_entries()
        self.define_buttons()
        self.define_combobox()
        self.define_labels()

    def retrieve_integers(self, var1: tk.StringVar, var2: tk.StringVar):
        try: 
            meal_amount = int(var1.get())
            day_amount = int(var2.get())
            return meal_amount, day_amount
        except ValueError as exc: 
            raise ValueError("Both StringVars must contain only integers") from exc
            
    def define_buttons(self):
        #define a button 
        button_0 = ctk.CTkButton(self, text="Generate List", command=self.generate_grocceries)
        button_0.grid(row = 7, column = 1, pady=10)

    def define_combobox(self) -> None:
        #define a combobox
        grid_value = self.meal_amount*self.day_amount
        for i in range(grid_value):
            ctk.CTkComboBox(self, values=self.recipe_list, variable = self.combvars[i])\
            .grid(row = i%self.meal_amount + 1, column = i%self.day_amount + 1, padx = 5, pady= 5)

    def define_labels(self) -> None:
        days = [f"Day {i + 1}" for i in range(self.day_amount)]
        for i in range(self.day_amount):
            ctk.CTkLabel(self, text = days[i]).grid(row=0, column=i + 1, padx=5, pady=5)

        times = [f"Meal {i + 1}" for i in range(self.meal_amount)]
        for i in range(self.meal_amount):
            ctk.CTkLabel(self, text = times[i]).grid(row=i+1, column=0, padx=5, pady=5)

    def generate_entries(self):
        with open(INGREDIENT_FILE, "r") as file:
            self.recipes = yaml.safe_load(file)
        self.recipe_name_to_recipe(self.recipes)
        self.recipe_list = [recipe["recipe"] for recipe in self.recipes]

    def recipe_name_to_recipe(self, recipes: list):
        for index, entry in enumerate(recipes):
            self.recipe_map[entry["recipe"]] = index

    def generate_groccerie_list(self):
        GroccerieList(ingredient_dict=self.ingredient_dict)

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
            ingredient_name = f"{ingredient["subcategory"]} {ingredient["ingredient"]}"
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


class GroccerieList(ctk.CTkToplevel):

    def __init__(self, ingredient_dict: dict) -> None:

        super().__init__()

        self.title("Groccerie List")
        # self.geometry("300x200")
        # self.resizable(False, False)
        self.minsize(width = 300, height=200)

        # importing custom image
        image_path = "./icons/list-check.png"
        self.img = Image.open(image_path)

        ctk.CTkLabel(self, text ='Generated List: ' , image=ctk.CTkImage(light_image=self.img, dark_image=self.img),
                    fg_color=LABEL_COLOR,compound="left", corner_radius = 10, padx = 10, pady = 10).pack()

        self.generate_list_entries(ingredient_dict)

    def generate_list_entries(self, ingredient_dict):
        item_list = [f"{value} {key[0]} {key[1]} \n" for value, key in ingredient_dict.items()]
        for item in item_list:
            ctk.CTkLabel(self, text = item, width=40, anchor="center", padx = 10, pady = 10).pack()

if __name__ == "__main__":
    grocceries = Grocceries()