import yaml
from bidict import bidict
from paths import FILE_PATH, INGREDIENT_FILE
# class to parse the dictionary entries and either add them to the 
# recipe list or not 
# requires a list of requirements 
# List of requirements:
# Recipe has to have atleast 2 ingredients 
# No two recipes can not have the same name 
# No two recipes can not have identical list of ingredients 
# if yaml file is empty create a list 
# import yaml 

class Parser():

    MEASUREMENT_OPTIONS = ["Units (u)", "Grams (g)", "Mililiters (ml)", 
                           "Tea-Spoons (Tsp)", "Table-Spoons (Tbsp)"]
    
    MEASUREMENT_MAP = {"u" : "Units (u)", "g" : "Grams (g)", "ml" : "Mililiters (ml)", 
                       "Tsp" : "Tea-Spoons (Tsp)", "Tbsp" : "Table-Spoons (Tbsp)"}
    
    BIDIRECT_MEASUREMENT_MAP = bidict(MEASUREMENT_MAP).inverse

    # class level attributes
    yaml_dictionary: list = {}
    name_to_recipe: dict = {}
    recipe_to_id: dict[str, int] = {}


    def __init__(self, file_path = INGREDIENT_FILE) -> None:
        self.file_path = file_path


    def parse_ingredients(self, text: str) -> list[str]:
        #open the file
        ingredient_list = []
        with open(text, "r", encoding="utf-8") as file:
            for line in file:
                ingredient_list.append(line.strip())
        return ingredient_list
    
    def load_yaml_data(self) -> None:
        with open(INGREDIENT_FILE, "r", encoding="utf-8") as file: 
            Parser.yaml_dictionary = yaml.safe_load(file)

    def recipe_names_to_recipes(self) -> None:
        if Parser.yaml_dictionary:
            for entry in Parser.yaml_dictionary:
                recipe_name = entry["recipe"]
                Parser.name_to_recipe[recipe_name] = entry

    def define_recipe_to_id(self) -> None:
        if Parser.yaml_dictionary:
            for id, entry in enumerate(Parser.yaml_dictionary):
                recipe_name = entry["recipe"]
                Parser.recipe_to_id[recipe_name] = id

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
        
    def write_to_yaml(self, file: str, data):
        with open(file, "w", encoding="utf-8") as f:
                yaml.dump(data, f, sort_keys=False)
    
    
    def parse_recipe_dictionary(self, recipe_dictionary: dict[str : str]) -> None:
        list_of_functions = [self.check_ingredient_amount, self.check_recipe_name]

        empty_list = []
        empty_list.append(recipe_dictionary)

        with open(INGREDIENT_FILE, "r", encoding="utf-8") as file: 
            self.ingredient_file = yaml.safe_load(file)

        if self.ingredient_file is None:
            with open(INGREDIENT_FILE, "w", encoding="utf-8") as file:
                yaml.dump(empty_list, file, default_flow_style=False, sort_keys=False)

        elif all(func(recipe_dictionary) for func in list_of_functions): 
            with open(INGREDIENT_FILE, "a", encoding="utf-8") as file:
                yaml.dump(empty_list, file, default_flow_style=False, sort_keys=False)
                
if __name__ == "__main__":
    save = Parser("C:/Users/subotovic/Desktop/Code/Einkaufsliste/ingredient.yaml")