from enum import Enum

#Enums for categorizing recipes
class Category(Enum):
    BREAKFAST = "Breakfast"
    DINNER = "Dinner"

#Enums to categorize units
class Units(Enum):
    GRAMS = "g"
    MILLILITERS = "ml"
    UNITS = ""


class Groceries:
    def __init__(self, recipebook):
        self.recipebook = recipebook

    def print_recipes(self):
        for recipe in self.recipebook:
            print(recipe.name, recipe.category)

    def choose_recipes(selfs):
        choice = input("Choose recipes by typing the number: ")

    def create_groceries(self):
        print("Groceries")



class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)
        return recipe

    def total_recipes(self):
        for recipe in self.recipes:
            print(recipe.name, ": ",  recipe.category.value)


class Recipe:
    #name
    def __init__(self, name, category, ingredients):
        self.name = name
        self.category = category
        self.ingredients = ingredients
        # Automatically add the recipe to the recipe book
        #self.recipe_book = RecipeBook()
        #self.recipe_book.add_recipe(self)


    #def __str__(self):


recipe_book = RecipeBook()

nalesniki = Recipe("Naleśniki", Category.BREAKFAST,
(("Mehl", 500, Units.GRAMS),
    ("Milch", 200, Units.MILLILITERS),
    ("Eier", 2, Units.UNITS),
    ("Zucker", 200, Units.GRAMS),
    ("Salz", 4, Units.GRAMS)
))



spaghetti_carbonara = Recipe("Spaghetti Carbonara", Category.DINNER,
                             (("Speck", 100, Units.GRAMS),
                              ("Spaghetti", 200, Units.GRAMS),
                              ("Parmiggano", 50, Units.GRAMS),
                              ("Eier", 3, Units.UNITS)
))

garlic_pasta = Recipe("Garlic Pasta", Category.DINNER,
                      (("Garlic", 3, Units.UNITS)

))

fried_rice = Recipe("Fried Rice", Category.DINNER,
                    (
    ("Reis", 200, Units.GRAMS),
    ("Eier", 2, Units.UNITS),
    ("Soja-Sauce", 40, Units.MILLILITERS),
    ("Gemüse", ),
    ("Salz", 5, Units.GRAMS)
))

varsketukai = Recipe("Varsketukai", Category.BREAKFAST,
                     (("Quark", 650, Units.GRAMS),
                      ("Eier", 2, Units.UNITS),
                      ("Zucker", 50, Units.GRAMS),
                      ("Salz", 3, Units.GRAMS),
                      ("Mehl", 312, Units.GRAMS),
                      ("Butter", 500, Units.GRAMS),
                      ("Schmand", 50, Units.GRAMS)

))

french_toast = Recipe("French Toast", Category.BREAKFAST,
                       (
    ("Toast", 4, Units.UNITS),
    ("Eier", 2, Units.UNITS),
    ("Milch", 100, Units.MILLILITERS),
    ("Zimt", 5, Units.GRAMS),
    ("Zucker", 50, Units.GRAMS)
))

mexican_rice = Recipe("Mecican Rice", Category.DINNER,
    (("Rice", 2, Units.UNITS),
     ("Bohnen", 200, Units.GRAMS),
     ("Mais", 200, Units.GRAMS),
     ("Passata", 200, Units.GRAMS)
    )
)

fleisch_pasta = Recipe



chilli_can_carne = Recipe("Chilli Con Carne", Category.DINNER,
    (("Bohnen", 250, Units.GRAMS),
    ("Mais", 250, Units.GRAMS),
    ("Cayanne-Pfeffer", 5, Units.GRAMS),
    ("Tomaten-Passata", 200, Units.GRAMS),
    ("Rind-")

))

recipe_book.add_recipe(chilli_can_carne)
recipe_book.add_recipe(french_toast)
recipe_book.add_recipe(varsketukai)
recipe_book.total_recipes()
