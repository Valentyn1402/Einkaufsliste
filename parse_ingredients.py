# class to parse the dictionary entries and either add them to the 
# recipe list or not 
# requires a list of requirements 


# List of requirements:
# Recipe has to have atleast 2 ingredients 
# No two recipes can not have the same name 
# No two recipes can not have identical list of ingredients 

import yaml 

INGREDIENT_FILE = "C:/Users/subotovic/Desktop/Code/Einkaufsliste/ingredient.txt"

class Parser():

    def __init__(self) -> None:

        with open(INGREDIENT_FILE, "r", encoding="utf-8") as file: 
            self.ingredient_file = yaml.safe_load(file)
        

    def check_recipe_name(self, recipe: dict[str : str]) -> bool:
        for entry in self.ingredient_file: 
            if recipe["recipe"] == entry["recipe"]:
                return False
        return True
    
    def check_ingredient_amount(self, recipe: dict[str : str]) -> bool:
        ingredient_list = recipe["ingredients"]
        if len(ingredient_list) >= 2: 
            return True
        else: 
            return False
        
    def check_ingredients(self, recipe: dict[str : str]) -> bool:
        for entry in self.ingredient_file:
            list_of_ingredients = entry["ingredients"]
            recipe_ingrediets = recipe["ingredients"]
            for ingredient in list_of_ingredients: 
                if list_of_ingredients["ingredient"] == recipe_ingrediets["ingredients"] and \
                list_of_ingredients["subcategory"] == recipe_ingrediets["subcategory"] and \
                list_of_ingredients["amount"] == recipe_ingrediets["amount"]:
                    return False
        return True

    def parse_recipe_dictionary(self, recipe_dictionary: dict[str : str]) -> None:
        list_of_functions = [self.check_ingredient_amount, self.check_ingredients, self.check_recipe_name]

        if not any(func(recipe_dictionary) for func in list_of_functions):
            with open(INGREDIENT_FILE, "w", encoding="utf-8") as file:
                yaml.dump(recipe_dictionary, file)