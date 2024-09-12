import yaml
import tkinter as tk
from tkinter import ttk
from paths import INGREDIENT_FILE


'''
TO DO: create an user friendly interface which allows for choosing 
option for other should be available 
- Create a mapping of recipe name to recipe entry 



'''

class Grocceries():

    recipe_list: list[str]
    recipe_map: dict[str : int]
    recipe_amount: dict[str : int]
    ingredient_list: dict[str : int]
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
        self.ingredient_list = {}
        self.combvars = [tk.StringVar() for var in range(21)]

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

    def generate_grocceries(self):
        self.sort_grocceries()
        print(self.recipe_amount)
        print(self.recipes)

        for list_entry in self.recipes:
            for key, value in self.recipe_amount:
                recipe_index = self.recipe_map[key]
                recipe = self.recipes[recipe_index]
                ingredients = recipe["ingredients"]
                for ingredient in ingredients:
                    
                    pass





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