# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Rezepte
from Rezepte import Recipe, Units, Category

# %TODO: Create a YAML files which has all the recipes, easier to parse 

list_of_recipes = [
    Recipe("Plovas", Category.DINNER,
                   (("Fleisch", 500, Units.GRAMS),
                    ("Reis", 200, Units.GRAMS),
                    ("Karrotte", 2, Units.UNITS),
                    ("Zwiebel", 1, Units.UNITS),
                    ("Knbolauch", 1, Units.UNITS),
                    ("Öl", 20, Units.MILLILITERS),
                    ("Salz", 10, Units.GRAMS),
                    ("Pfeffer", 4, Units.GRAMS),
                    ("Paprika Gewürz", 10, Units.GRAMS),
                    ("Lorbeerblätter", 2, Units.UNITS),
                    ("Cumin", 10, Units.GRAMS)
                    )),

    Recipe("Naleśniki", Category.BREAKFAST,
                   (("Mehl", 500, Units.GRAMS),
                    ("Milch", 200, Units.MILLILITERS),
                    ("Eier", 2, Units.UNITS),
                    ("Zucker", 200, Units.GRAMS),
                    ("Salz", 4, Units.GRAMS)
                    )),

    Recipe("French Omlette", Category.BREAKFAST,
                   (("Eier", 3, Units.UNITS),
                    ("Schnittlauch", 2, Units.UNITS),
                    ("Salz", 2, Units.GRAMS),
                    ("Pfeffer", 2, Units.UNITS),
                    ("Butter", 20, Units.GRAMS),
                    ("Cheddar", 40, Units.GRAMS)
                    )),

    Recipe("Eggs and Ham Sandwich", Category.BREAKFAST,
                   (("English Muffins", 2, Units.UNITS),
                    ("Bacon", 4, Units.UNITS),
                    ("Cheddar", 40, Units.UNITS),
                    ("Eier", 2, Units.UNITS),
                    ("Salz", 2, Units.GRAMS)
                   )),

    Recipe("Overnight Oats", Category.BREAKFAST,
                   (("Haferflocken", 50, Units.GRAMS),
                    ("Milch", 100, Units.MILLILITERS),
                    ("Joghurt", 50, Units.GRAMS),
                    ("Beeren", 100, Units.GRAMS),
                    ("Honig", 10, Units.GRAMS)
                    )),

    Recipe("Spaghetti Carbonara", Category.DINNER,
             (("Speck", 100, Units.GRAMS),
                      ("Spaghetti", 200, Units.GRAMS),
                      ("Parmiggano", 50, Units.GRAMS),
                      ("Eier", 3, Units.UNITS)
                      )),

    Recipe("Garlic Pasta", Category.DINNER,
                          (("Garlic", 3, Units.UNITS),
                           ("Noodles", 200, Units.GRAMS),
                           ("Reis Vinegar", 50, Units.MILLILITERS)
                          )),

    Recipe("Fried Rice", Category.DINNER,
                   (
                       ("Reis", 200, Units.GRAMS),
                       ("Eier", 2, Units.UNITS),
                       ("Soja-Sauce", 40, Units.MILLILITERS),
                       ("Gemüse",40, Units.GRAMS),
                       ("Salz", 5, Units.GRAMS)
                   )),

    Recipe("Varsketukai", Category.BREAKFAST,
                             (("Quark", 650, Units.GRAMS),
                              ("Eier", 2, Units.UNITS),
                              ("Zucker", 50, Units.GRAMS),
                              ("Salz", 3, Units.GRAMS),
                              ("Mehl", 312, Units.GRAMS),
                              ("Butter", 500, Units.GRAMS),
                              ("Schmand", 50, Units.GRAMS)
                              )
                              ),

    Recipe("French Toast", Category.BREAKFAST,
                          (
                              ("Toast", 4, Units.UNITS),
                              ("Eier", 2, Units.UNITS),
                              ("Milch", 100, Units.MILLILITERS),
                              ("Zimt", 5, Units.GRAMS),
                              ("Zucker", 50, Units.GRAMS)
                          )),

    Recipe("Mexican Rice", Category.DINNER,
                          (("Rice", 2, Units.UNITS),
                           ("Bohnen", 200, Units.GRAMS),
                           ("Mais", 200, Units.GRAMS),
                           ("Passata", 200, Units.GRAMS)
                           )),

    Recipe("Chilli Con Carne", Category.DINNER,
                              (("Bohnen", 250, Units.GRAMS),
                               ("Mais", 250, Units.GRAMS),
                               ("Cayanne-Pfeffer", 5, Units.GRAMS),
                               ("Tomaten-Passata", 200, Units.GRAMS),
                               ("Tomatenmark", 200, Units.GRAMS)
                               )),

    Recipe("Zirniu Sriuba", Category.DINNER,
                   (("Erbsen", 200, Units.GRAMS),
                    ("Kartoffel", 4, Units.UNITS),
                    ("Karoten", 2, Units.UNITS),
                    ("Zwiebel", 2, Units.UNITS),
                    ("Brühe", 20, Units.GRAMS),
                    ("Salz", 10, Units.GRAMS)
                   ))


]

def init_recipies(recipe_book):
    for i in range(len(list_of_recipes)):
        recipe_book.add_recipe(list_of_recipes[i])

def sort_recipes(recipe_book):
    breakfast_list = Rezepte.RecipeBook()
    dinner_list = Rezepte.RecipeBook()

    for recipe in recipe_book:
        if recipe.category is Rezepte.Category.DINNER:
            dinner_list.add_recipe(recipe)
        else:
            breakfast_list.add_recipe(recipe)

    return breakfast_list, dinner_list

def print_groceries(groceries):
    for ingredient in groceries:
        print(ingredient[0] + ": " + str(ingredient[1]) + ingredient[2].value)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Initialize a recipe book
    recipe_book = Rezepte.RecipeBook()
    #Initialize all Recipies
    init_recipies(recipe_book)
    #Sort the recipes by category
    recipe_book.sort_recipes()

    #Enumerate all the recipes
    recipe_book.enumerate_recipes()

    #Print items for breakfast
    print("Breakfast Food:")
    recipe_book.print_breakfast_recipes()

    #Request to input breakfast items to choose:
    breakfast_items = list(map(int, input("Choose beakfast items from the list above: ").split()))
    print(breakfast_items)

    #Print items for dinner
    print("Dinner Food:")
    recipe_book.print_dinner_recipes()

    #Request to input dinner items to choose:
    dinner_items = list(map(int, input("Choose dinner items from the list above: ").split()))
    print(dinner_items)

    #Take list items from and create a grocerie lsit  
    total_items = breakfast_items + dinner_items

    #Go through the list of groceries and convert them to recipes
    groceries = Rezepte.RecipeBook()
    for number in total_items:
        groceries.add_recipe(recipe_book.enum_recipes[number])

    grocery_list = groceries.generate_groceries()

    print("This is an example for a grocery list:")
    for ingredient, [amount, unit] in grocery_list.items():
       print(f"{ingredient}: {amount} {unit.value}")

    # Look the recipe numbers in breakfast_items
    '''for number in breakfast_items:
        #
        recipes = enum_breakfast_list[number]
        ingredients = recipes.ingredients
        for ingredient in ingredients:
            if ingredient[0] not in breakfast_groceries:
                breakfast_groceries.append(ingredient)
    '''

'''
     recipes should contain: 
     - name 
     - ingredients
     - instructions
    
     ingredients should be have identifier:
     name + integer ammount either milliliters or grams
'''