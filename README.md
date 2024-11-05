# Einkaufsliste
Repo für Einkaufszettelgenerierung 

# Using GUI
Install all the necessary libraries using requirements.txt

## Using the Generate Groccerie List Editor
1. Write the amount of days for which you want to generate the shopping list as well as the amount of meals for each day (It is not necessary to fill all the entries in the upcoming window, some of them can be left empty)
2. Once ready a button at the bottom left can be pressed and a pop up window will be generated in which a meal can be inserted for each of the days
3. Once finished button in the button left called "Generate List" can be pressed which will generate a groccerie shop list 

## Using the Add Recipe Editor 
A tab in the middle called "Add Recipe" can be pressed which will open an UI to insert any recipes, to do that follow these steps: 
   1. Enter the recipe name (do not use any special characters)
   2. Enter your name to know from whom the recipe was generated 
   3. (Optional) Enter recipe category either dinner or breakfast
   4. Enter first ingredient name, can either be written or choosen from the menu 
   5. (Optional) Enter the ingredient subcategory if it has one 
   6.  Enter the amount the measurement units for the ingredient amount can be given either as a whole number or a fraction for example 0.25 or 1/4, units can be choosen from the dropdown menu 
   7.  Press the button "Next Ingredient" to enter next ingredient and follow the same 6 previously mentioned steps

Once finished entering all the ingredients, "Add to recipes" button can be pressed to add the recipe to the list, this will reset the window allowing you to enter another recipe 

(Optional) if any of the ingredients were added incorrectly, you can choose the ingredient from the list and enter the details again, to save the changes press "Apply Changes" button

## Using the Edit Recipe Editor 
Edit Recipe Tab provides a user friendly interface to view all stored recipes and allows them to be edited in a simple manner 
To Edit a recipe following options are available
1. **Change Recipe Name:**
   1. Choose the recipe from the list on the left side 
   2. Once choosen the name of the recipe will be loaded to on of the entries
   3. Click on the field where the recipe name is loaded and change it to your liking 
   4. To save and store the name click on the button right next to it called "Change Name"

2. **Remove Ingredient:** 
   1. Choose the recipe from the list as in option 1.
   2. To remove ingredient from the recipe, choose an ingredient from a dropdown menu below the "Ingredients" title 
   3. Once correct ingredient selected, press "Remove Ingredient" button to remove the choosen ingredient 

3. **Change Ingredient** 
   1. Choose the recipe form the list as in option 1.
   2. Choose the ingredient as in option 2. 
   3. Change the amount as well as the measurement unit per your liking 
   4. Press the "Apply Changes" button to apply changes  

4. **Remove Recipe**
   1. Choose the recipe from the list as in option 1.
   2. Click "Remove Recipe" to remove recipe from the list


# Feature Requests 


- Option to add rating to the recipes 
- Input Validation: for Generate Groccerie List, add integer validation, there cannot be 1.5 days or 1.2 meals
- Input Validation: for Add Recipe, add string validation, recipe names and user names can only have basic alphabet letters as well as some special characters like '
for subcategory aswell. Add number validation for the amount that is entered as number can be either an integer, a decimal number or a fraction 
- Input Validation: for Edit Recipe, name should have the same string validation, the amount should have the same validation as in "add recipe" tab