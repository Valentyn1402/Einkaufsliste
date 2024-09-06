import yaml
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

    def __init__(self, file_path) -> None:
        self.file_path = file_path
        with open(self.file_path, "r", encoding="utf-8") as file: 
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
        
    # def check_ingredients(self, recipe: dict[str : str]) -> bool:
    #     for entry in self.ingredient_file:
    #         list_of_ingredients = entry["ingredients"]
    #         recipe_ingredients = recipe["ingredients"]
    #         if any(all(ingredient[key] == recipe_ingredient[key]) \
    #         for key in ["ingredient", "subcategory", "amount"] for ingredient, recipe_ingredient \
    #         in zip(list_of_ingredients, recipe_ingredients)):
    #             return False
    #     return True

    def parse_recipe_dictionary(self, recipe_dictionary: dict[str : str]) -> None:
        list_of_functions = [self.check_ingredient_amount, self.check_recipe_name]

        empty_list = []
        empty_list.append(recipe_dictionary)
        if self.ingredient_file is None:
            with open(self.file_path, "w", encoding="utf-8") as file:
                yaml.dump(empty_list, file, default_flow_style=False)

        elif all(func(recipe_dictionary) for func in list_of_functions): 
            with open(self.file_path, "a", encoding="utf-8") as file:
                yaml.dump(empty_list, file, default_flow_style=False)

        # else:
        #     if all(func(recipe_dictionary) for func in list_of_functions):
        #         with open(self.file_path, "w", encoding="utf-8") as file:
        #             yaml.dump(recipe_dictionary, file)

if __name__ == "__main__":
    save = Parser("C:/Users/subotovic/Desktop/Code/Einkaufsliste/ingredient.yaml")