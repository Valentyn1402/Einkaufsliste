# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Rezepte

list_of_recipes = [
    Rezepte.Recipe("Plovas", Rezepte.Category.DINNER,
                   (("Fleisch", 500, Rezepte.Units.GRAMS),
                    ("Reis", 200, Rezepte.Units.GRAMS),
                    ("Karrotte", 2, Rezepte.Units.UNITS),
                    ("Zwiebel", 1, Rezepte.Units.UNITS),
                    ("Knbolauch", 1, Rezepte.Units.UNITS),
                    ("Öl", 20, Rezepte.Units.MILLILITERS),
                    ("Salz", 10, Rezepte.Units.GRAMS),
                    ("Pfeffer", 4, Rezepte.Units.GRAMS),
                    ("Paprika Gewürz", 10, Rezepte.Units.GRAMS),
                    ("Lorbeerblätter", 2, Rezepte.Units.UNITS),
                    ("Cumin", 10, Rezepte.Units.GRAMS)
                    )),

    Rezepte.Recipe("Naleśniki", Rezepte.Category.BREAKFAST,
                   (("Mehl", 500, Rezepte.Units.GRAMS),
                    ("Milch", 200, Rezepte.Units.MILLILITERS),
                    ("Eier", 2, Rezepte.Units.UNITS),
                    ("Zucker", 200, Rezepte.Units.GRAMS),
                    ("Salz", 4, Rezepte.Units.GRAMS)
                    )),

    Rezepte.Recipe("French Omlette", Rezepte.Category.BREAKFAST,
                   (("Eier", 3, Rezepte.Units.UNITS),
                    ("Schnittlauch", 2, Rezepte.Units.UNITS),
                    ("Salz", 2, Rezepte.Units.GRAMS),
                    ("Pfeffer", 2, Rezepte.Units.UNITS),
                    ("Butter", 20, Rezepte.Units.GRAMS),
                    ("Cheddar", 40, Rezepte.Units.GRAMS)
                    )),

    Rezepte.Recipe("Eggs and Ham Sandwich", Rezepte.Category.BREAKFAST,
                   (("English Muffins", 2, Rezepte.Units.UNITS),
                    ("Bacon", 4, Rezepte.Units.UNITS),
                    ("Cheddar", 40, Rezepte.Units.UNITS),
                    ("Eier", 2, Rezepte.Units.UNITS),
                    ("Salz", 2, Rezepte.Units.GRAMS)
                   )),

    Rezepte.Recipe("Overnight Oats", Rezepte.Category.BREAKFAST,
                   (("Haferflocken", 50, Rezepte.Units.GRAMS),
                    ("Milch", 100, Rezepte.Units.MILLILITERS),
                    ("Joghurt", 50, Rezepte.Units.GRAMS),
                    ("Beeren", 100, Rezepte.Units.GRAMS),
                    ("Honig", 10, Rezepte.Units.GRAMS)
                    )),

    Rezepte.Recipe("Spaghetti Carbonara", Rezepte.Category.DINNER,
             (("Speck", 100, Rezepte.Units.GRAMS),
                      ("Spaghetti", 200, Rezepte.Units.GRAMS),
                      ("Parmiggano", 50, Rezepte.Units.GRAMS),
                      ("Eier", 3, Rezepte.Units.UNITS)
                      )),

    Rezepte.Recipe("Garlic Pasta", Rezepte.Category.DINNER,
                          (("Garlic", 3, Rezepte.Units.UNITS),
                           ("Noodles", 200, Rezepte.Units.GRAMS),
                           ("Reis Vinegar", 50, Rezepte.Units.MILLILITERS)
                          )),

    Rezepte.Recipe("Fried Rice", Rezepte.Category.DINNER,
                   (
                       ("Reis", 200, Rezepte.Units.GRAMS),
                       ("Eier", 2, Rezepte.Units.UNITS),
                       ("Soja-Sauce", 40, Rezepte.Units.MILLILITERS),
                       ("Gemüse",40, Rezepte.Units.GRAMS),
                       ("Salz", 5, Rezepte.Units.GRAMS)
                   )),

    Rezepte.Recipe("Varsketukai", Rezepte.Category.BREAKFAST,
                             (("Quark", 650, Rezepte.Units.GRAMS),
                              ("Eier", 2, Rezepte.Units.UNITS),
                              ("Zucker", 50, Rezepte.Units.GRAMS),
                              ("Salz", 3, Rezepte.Units.GRAMS),
                              ("Mehl", 312, Rezepte.Units.GRAMS),
                              ("Butter", 500, Rezepte.Units.GRAMS),
                              ("Schmand", 50, Rezepte.Units.GRAMS)
                              )
                              ),

    Rezepte.Recipe("French Toast", Rezepte.Category.BREAKFAST,
                          (
                              ("Toast", 4, Rezepte.Units.UNITS),
                              ("Eier", 2, Rezepte.Units.UNITS),
                              ("Milch", 100, Rezepte.Units.MILLILITERS),
                              ("Zimt", 5, Rezepte.Units.GRAMS),
                              ("Zucker", 50, Rezepte.Units.GRAMS)
                          )),

    Rezepte.Recipe("Mexican Rice", Rezepte.Category.DINNER,
                          (("Rice", 2, Rezepte.Units.UNITS),
                           ("Bohnen", 200, Rezepte.Units.GRAMS),
                           ("Mais", 200, Rezepte.Units.GRAMS),
                           ("Passata", 200, Rezepte.Units.GRAMS)
                           )),

    Rezepte.Recipe("Chilli Con Carne", Rezepte.Category.DINNER,
                              (("Bohnen", 250, Rezepte.Units.GRAMS),
                               ("Mais", 250, Rezepte.Units.GRAMS),
                               ("Cayanne-Pfeffer", 5, Rezepte.Units.GRAMS),
                               ("Tomaten-Passata", 200, Rezepte.Units.GRAMS),
                               ("Tomatenmark", 200, Rezepte.Units.GRAMS)
                               )),

    Rezepte.Recipe("Zirniu Sriuba", Rezepte.Category.DINNER,
                   (("Erbsen", 200, Rezepte.Units.GRAMS),
                    ("Kartoffel", 4, Rezepte.Units.UNITS),
                    ("Karoten", 2, Rezepte.Units.UNITS),
                    ("Zwiebel", 2, Rezepte.Units.UNITS),
                    ("Brühe", 20, Rezepte.Units.GRAMS),
                    ("Salz", 10, Rezepte.Units.GRAMS)
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