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

class Ingredient(Enum):
    MILK = ""
    BUTTER = ""
    PASTA = ""
    MEAT = ""
    RICE = ""
    ONION = ""
    OIL = ""
    SPICES = ""
    GARLIC = ""
    FLOUR = ""
    EGGS = ""
    SUGAR = ""
    CHEESE = ""

    def __init__(self, category: Enum, subcategory: str = None):
        self._category = category
        self._subcategory = subcategory

#Ingredient class which can also have subcategory 

class Recipe:
    #name
    def __init__(self, name, category, ingredients):
        self.name = name
        self.category = category
        self.ingredients = ingredients
        # Automatically add the recipe to the recipe book
        #self.recipe_book = RecipeBook()
        #self.recipe_book.add_recipe(self)

    def custom_sort_key(self):
        if self.category == Category.BREAKFAST:
            return 0
        else:
            return 1

class RecipeBook:
    def __init__(self):
        #super().__init__()
        self.number = 1
        self.recipes = []
        self.grocery_list = []
        self.enum_recipes = {}

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)
        return recipe

    #Sorts recipes by category
    def sort_recipes(self):
        self.recipes.sort(key=lambda x: x.category.value)

    def total_recipes(self):
        index = len(self.recipes)
        for index, item in enumerate(self.recipes, start=1):
            print(f"{index}. {item.name}")

    #Enumerate all the objects  in the recipe list to get an number -> recipe
    def enumerate_recipes(self):
        number = 1
        for recipe in self.recipes:
            self.enum_recipes[number] = recipe
            number += 1

        return self.enum_recipes
    #
    def print_breakfast_recipes(self):
        for recipe in self.recipes:
            if recipe.category == Category.BREAKFAST:
                print(f"{self.number}. {recipe.name}")
                self.number += 1

    def print_dinner_recipes(self):
        for recipe in self.recipes:
            if recipe.category == Category.DINNER:
                print(f"{self.number}. {recipe.name}")
                self.number += 1

    def sort_ingredients(self, ingredients):
        print(ingredients)

    def generate_groceries(self):
        grocery_list = {}
        #Go through each recipe in the list
        for recipe in self.recipes:
            iterable_tuple = recipe.ingredients

            for ingredient, amount, unit in recipe.ingredients:
                if ingredient not in grocery_list:
                    grocery_list[ingredient] = [amount, unit]
                else:
                    add = grocery_list[ingredient][0]
                    grocery_list[ingredient] = [add + amount, unit]
        return grocery_list

    def __iter__(self):
        return iter(self.recipes)

class Groceries(RecipeBook):
    def __init__(self):
        super().__init__()

    def choose_recipes(self):
        choice = input("Choose recipes by typing the number: ")

    def create_groceries(self):
        print("Groceries")

