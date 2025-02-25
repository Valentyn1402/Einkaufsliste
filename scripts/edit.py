import tkinter as tk
from tkinter import ttk
from tkinter import font
from parse_ingredients import Parser
from paths import STAR_IMAGE_PATH, INGREDIENT_FILE
from style_template import LIGHT_GREY, BLUE_COLOR
from PIL import Image
import customtkinter as ctk
from validation import validate_input_number, validate_input_string


'''
create a dictionary which maps the entries of the list entries to recipe names 

- add remove recipe button 

'''




class EditorFunctions(Parser):

    def __init__(self) -> None:
                
        pass
        # self.parent = parent
        # self.current_recipe: str = current_recipe
        # self.current_label: tk.Label = current_label
        # self.value_list = value_list

        # self.define_grid()

        # self.define_variables()
        # self.padx = 10

    def change_name(self, recipe_name: str, current_recipe: str, current_label: tk.Label) -> None:
        '''
        add the function to change the label text in the edit tab 
        '''
        # get new recipe name 
        new_name = recipe_name
        # validate the recipe name
        validate_input_string(new_name)
        # get the recipe name and position
        id = Parser.recipe_to_id[current_recipe]
        recipe = Parser.yaml_dictionary[id]
        recipe["recipe"] = new_name
        # set the label to new_name
        current_label.configure(text = new_name)
        # write new name to the recipe
        self.write_to_yaml(file = INGREDIENT_FILE, data = Parser.yaml_dictionary)
    
    def change_ingredient(self, ingredient_name: str, current_recipe: str, unit_parts: str, amount: str) -> None: 
        # get the recipe name and position
        id = Parser.recipe_to_id[current_recipe]
        # load the recipe
        recipe = Parser.yaml_dictionary[id]
        # get the ingredient list
        ingredients = recipe["ingredients"]
        # set ingredient id to 0
        ingredient_id = 0
        for i, ingredient in enumerate(ingredients):
            if ingredient["ingredient"] == ingredient_name:
                ingredient_id = i
                break
        # removes ingredient at specified position
        new_ingredient = ingredients[ingredient_id]
        new_ingredient["ingredient"] = ingredient_name
        unit = unit_parts.split(" ")
        unit = unit[1].replace("(", "").replace(")", "")
        # check if the amount is valid number
        validate_input_number(unit)
        # define the new amount 
        new_ingredient["amount"] = f"{amount} {unit}"
        # write changes to the recipe 
        self.write_to_yaml(file = INGREDIENT_FILE, data = Parser.yaml_dictionary)

    def remove_ingredient(self, combobox_1: ctk.CTkComboBox, combobox_2: ctk.CTkComboBox, var_1: ctk.StringVar, 
                           ingredient_name: str, current_recipe: str, value_list: list) -> None:
        # get the recipe name and position
        id = Parser.recipe_to_id[current_recipe]
        # load the recipe
        recipe = Parser.yaml_dictionary[id]
        # get the ingredient list
        ingredients = recipe["ingredients"]
        # set ingredient id to 0
        ingredient_id = 0
        for i, ingredient in enumerate(ingredients):
            if ingredient["ingredient"] == ingredient_name:
                ingredient_id = i
                break
        # removes ingredient at specified position
        ingredients.pop(ingredient_id)
        value_list.remove(ingredient_name)
        combobox_1.configure(values = value_list)
        # reset ingredients
        self.reset_ingredients(combobox_1, combobox_2, var_1)

        # write changes to the recipe 
        self.write_to_yaml(file = INGREDIENT_FILE, data = Parser.yaml_dictionary)

    def reset_recipe_view(self, recipe_view_frame: ctk.CTkFrame):
        # Destroy all child widgets of the frame
        for widget in recipe_view_frame.winfo_children():
            widget.destroy()

    def reset_ingredients(self, combobox_1: ctk.CTkComboBox, combobox_2: ctk.CTkComboBox, var_1: ctk.StringVar) -> None:
        combobox_1.set("")
        combobox_2.set("")
        var_1.set("")

class EditRecipe(ctk.CTkFrame, EditorFunctions):
    def __init__(self, value_list: list[str], parent: ctk.CTkFrame) -> None:
        # initialize the parent class 
        super().__init__(parent)

        print("This is the self of EditRecipe: ", self)

        self.configure(width = 300, height = 400)

        # self.current_recipe: str = current_recipe
        # self.current_label: tk.Label = current_label
        self.value_list = value_list

        self.current_ingredients: dict = {}
        self.padx = 10

        self.define_grid()

        self.define_variables()

        self.create_widgets()
        self.pack()

    
    def create_widgets(self) -> None:
        # define buttons
        self.create_buttons()

        # create labels
        self.create_labels()

        # create entries
        self.create_entries()

        # create combobox
        self.create_combobox()

        # place combobox
        self.place_combobox()
        
        # place butt
        self.place_buttons()
        
        # place labels
        self.place_labels()

        # place entries
        self.place_entries()
    
    def set_recipe_name(self, recipe_name: str):
        self.vars[0].set(recipe_name)

    def set_combobox(self, values: list[str]):
        self.combobox_1.configure(values=values)
    
    def load_widgets(self, event):
        print("load widget method: ", self.value_list)
        ingredient_name = self.combobox_1.get()
        amount, unit, subcategory = self.current_ingredients[ingredient_name]
        self.vars[1].set(amount)
        self.vars[2].set(subcategory)
        self.combobox_2.set(Parser.MEASUREMENT_MAP[unit])

    def define_grid(self) -> None:
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1) # , minsize=20) 

    def define_variables(self):
        self.combvars = [tk.StringVar() for var in range(2)]
        self.vars = [tk.StringVar() for var in range(3)]
    
    def create_entries(self) -> None: 
        self.entry_1 = ctk.CTkEntry(self, textvariable=self.vars[0])
        self.entry_2 = ctk.CTkEntry(self, textvariable=self.vars[1])
        self.entry_3 = ctk.CTkEntry(self, textvariable=self.vars[2])
    
    def place_entries(self) -> None:
        self.entry_1.grid(column = 0, row = 1, padx = self.padx, pady = 10)
        self.entry_2.grid(column = 0, row = 6, padx = self.padx, pady = 10)
        self.entry_3.grid(column = 0, row = 4, padx = self.padx, pady = 10)


    def create_combobox(self) -> None:
        self.combobox_1 = ctk.CTkComboBox(self, variable=self.combvars[0], values=self.value_list, command=self.load_widgets)
        self.combobox_2 = ctk.CTkComboBox(self, values=Parser.MEASUREMENT_OPTIONS,variable=self.combvars[1])

    def place_combobox(self) -> None:
        self.combobox_1.grid(column = 0, row = 3, padx = self.padx, pady = 10)
        self.combobox_2.grid(column = 1, row = 6, padx = self.padx, pady = 10)

    def create_buttons(self) -> None:
        # define 4 Buttons for the header
        self.button_6 = ctk.CTkButton(master=self, text= "Remove Recipe", hover_color="red")
        self.button_7 = ctk.CTkButton(master=self, text= "Change Name", hover_color="red", 
                                      command=lambda: self.change_name(recipe_name = self.vars[0].get(), current_recipe = self.current_recipe,\
                                                                       current_label = self.current_label))
        self.button_8 = ctk.CTkButton(master=self, text= "Remove Ingredient", hover_color="red", command= lambda: 
                                      self.remove_ingredient(combobox_1 = self.combobox_1, combobox_2 = self.combobox_2, var_1 = self.vars[1], ingredient_name = self.combobox_1.get()
                                                             ,current_recipe = self.current_recipe, value_list = self.value_list))
        self.button_9 = ctk.CTkButton(master=self, text= "Apply Changes ", hover_color="red", command = lambda: 
                                      self.change_ingredient(ingredient_name = self.combobox_1.get(), current_recipe = self.current_recipe
                                                             ,unit_parts = self.combobox_2.get(), amount = self.vars[1].get()))

    def place_buttons(self) -> None:
        # place on the scrollable frame 
        self.button_6.grid(column = 1, row = 7, padx = self.padx, pady = 10)
        self.button_7.grid(column = 1, row = 1, padx = self.padx, pady = 10)
        self.button_8.grid(column = 1, row = 3, padx = self.padx, pady = 10)
        self.button_9.grid(column = 0, row = 7, padx = self.padx, pady = 10)

    def create_labels(self) -> None:
        # labels for editor menu
        self.label_4 = ctk.CTkLabel(master=self, text= "Subcategory", text_color="white")
        self.label_5 = ctk.CTkLabel(master=self, text= "Recipe Name", text_color="white")
        self.label_6 = ctk.CTkLabel(master=self, text= "Ingredients", text_color="white")
        self.label_7 = ctk.CTkLabel(master=self, text= "Amount", text_color="white")
        self.label_8 = ctk.CTkLabel(master=self, text= "Measurement", text_color="white")

    
    def place_labels(self) -> None:
        # place main edit menu labels
        self.label_4.grid(column = 1, row = 4, padx = self.padx, pady = 10)
        self.label_5.grid(column = 0, row = 0, padx = self.padx, pady = 10)
        self.label_6.grid(column = 0, row = 2, padx = self.padx, pady = 10)
        self.label_7.grid(column = 0, row = 5, padx = self.padx, pady = 10)
        self.label_8.grid(column = 1, row = 5, padx = self.padx, pady = 10)


class ViewRecipe(ctk.CTkFrame): 

    def __init__(self, parent: ctk.CTkFrame) -> None: 

        # initialize the dunder method 
        super().__init__(parent)

        self.configure(width = 300, height = 400)

        print("Initializing ViewRecipe class!!")
        # define the framework for the list of ingredients
        self.define_listbox()

        self.pack()
    
    def define_listbox(self) -> None:
        """Define listbox onto the GUI
        """
        self.scrollable_frame = ctk.CTkScrollableFrame(master=self, width= 270, height=400, fg_color="white")
        # self.scrollable_frame.grid(row = 1, column = 3, rowspan = 6, padx = 50)
        self.scrollable_frame.pack()
        self.define_header()

    def define_header(self) -> None:
        frame_1 = ctk.CTkFrame(master = self.scrollable_frame, fg_color="white", bg_color="white",
                            width = 240, height = 30, corner_radius=20)
        frame_1.pack(expand = True)
        ctk.CTkLabel(master = frame_1, width = 90, corner_radius= 5, fg_color = BLUE_COLOR, text_color="white", 
        text = "Ingredient: ").pack(side="left", padx = 3)
        ctk.CTkLabel(master = frame_1, width = 90, corner_radius= 5, fg_color = BLUE_COLOR, text_color="white", 
        text = "Subcategory: ").pack(side = "left", padx = 3)
        ctk.CTkLabel(master = frame_1, width = 90, corner_radius= 5, fg_color = BLUE_COLOR, text_color="white", 
        text = "Amount: ").pack(side = "left", padx = 3)

    def add_to_scrollable_frame(self, ingredient_name, subcategory, amount):
        frame_1 = ctk.CTkFrame(master = self.scrollable_frame, fg_color="white",
                            width = 390, height = 30, corner_radius=20)
        frame_1.pack(expand = True)
        label_1 = ctk.CTkLabel(master=frame_1, width = 90, text=ingredient_name, 
        text_color="black")
        label_1.grid(column = 0, row = 0, sticky = "ew")
        label_2 = ctk.CTkLabel(master=frame_1, width = 90, text=subcategory, 
        text_color="black")
        label_2.grid(column = 1, row = 0, sticky = "ew")
        label_3 = ctk.CTkLabel(master=frame_1, width = 90, text=amount, 
        text_color="black")
        label_3.grid(column = 2, row = 0, sticky = "ew")

    def load_recipe_view(self, ingredients: list):
        for ingredient in ingredients:
            self.add_to_scrollable_frame(ingredient_name = ingredient["ingredient"],\
                                         subcategory = ingredient["subcategory"], amount = ingredient["amount"])

    def reset_recipe_view(self):
        # Destroy all child widgets of the frame
        children = self.scrollable_frame.winfo_children()

        for widget in children[1:]:
            widget.destroy()

class EditorWindow(ctk.CTkFrame, EditorFunctions):

    def __init__(self, parent: ctk.CTkFrame) -> None: 

        # initialize the dunder method 
        super().__init__(parent)

        # define a frame where the tabview is going to be placed
        self.define_frame()
        # define a scrollable frame for the scrollable view of the recipes
        self.define_scrollable_frame()
        # create tabview for the recipe editor and recipe view
        self.create_tabview()
        
        self.padx = 5

        self.value_list: list[str] = []

        self.parent_frame: tk.Frame = None

        self.current_recipe: str = None

        self.current_label: tk.Label = None

        self.recipe: dict = None

        self.ingredients: list = None

        self.current_ingredients: dict[str, list[str]] = {}
 
        # loads yaml data to Parser.yaml_dictionary
        self.load_yaml_data()
        
        # load recipe names to recipe dictionary 
        self.recipe_names_to_recipes()

        # define recipe to number dictionary
        self.define_recipe_to_id()

        # define variables
        self.define_variables()
        
        # define the grid of main window frame 
        self.define_grid() 

        # define variables
        self.ingredientsvar = tk.StringVar()

        # append list entries
        self.add_recipes_to_list()

        self.edit_recipe = EditRecipe(value_list = self.value_list, parent=self.tab_1)
        self.recipe_view = ViewRecipe(parent=self.tab_2)
        self.pack(fill = ctk.BOTH, expand = True)

    def create_tabview(self):
        """creates tabview for edit recipe and view recipes tabs 
        """
        self.tabview = ctk.CTkTabview(master=self.frame_2, width=300, height=400, anchor="w")
        self.tabview.pack(padx=20, pady=20, side = ctk.TOP)
        self.tab_1 = self.tabview.add("Edit Recipe")  # add tab at the end
        self.tab_2 = self.tabview.add("View Recipes")  # add tab at the end
        self.tabview.set("View Recipes")  # set currently visible tab

    def define_variables(self):
        """define variables for combobox and entry widgets 
        """
        self.combvars = [tk.StringVar() for var in range(2)]
        self.vars = [tk.StringVar() for var in range(3)]

    def define_grid(self):
        """define grid for the editor window 
        """
        # define grid for the window
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)

    def define_scrollable_frame(self) -> None: 
        """define scrollable frame for viewing the list of recipes 
        """
        # create frames 
        self.frame = ctk.CTkScrollableFrame(master=self, width=600, height=400, fg_color="white")
        self.frame.grid(column = 0, row = 0, sticky = "nsew")    
        self.define_header()

    def define_frame(self) -> None:
        """define frame for second tabview 
        """
        self.frame_2 = ctk.CTkFrame(master=self, height=200)
        self.frame_2.grid(column = 1, row = 0)
    
    def define_header(self) -> None:
        """define header for the scrollable frame 
        """
        frame_3 = ctk.CTkFrame(master=self.frame, fg_color= "white", width = 600, height = 40)
        frame_3.pack(expand = True)
        ctk.CTkButton(master=frame_3, text = "Recipe", hover_color="red", width = 150, 
                      border_color="white", border_width=2).pack(side = "left")
        ctk.CTkButton(master=frame_3, text = "Author", hover_color="red", width = 150, 
                      border_color="white", border_width=2).pack(side = "left")
        ctk.CTkButton(master=frame_3, text = "Date ", hover_color="red", width = 150, 
                      border_color="white", border_width=2).pack(side = "left")
        ctk.CTkButton(master=frame_3, text = "Rating", hover_color="red", width = 150, 
                      border_color="white", border_width=2).pack(side = "left")

    def define_canvas(self) -> None:
        # add canvas to the frame 
        self.canvas = ctk.CTkCanvas(master = self, height=300, width=600)

    def highlight_frame(self, event: tk.Event):

        if isinstance(event.widget, tk.Label):
            # get information about the parent widget 
            label_path = event.widget.winfo_parent()
            # Split the path into components
            path_components = label_path.split('.')

            # Remove the last component to get the parent path
            parent_path_components = path_components[:-1]
            # Reconstruct the parent path
            parent_path = ".".join(parent_path_components)
            # get the parent widget (frame widget)
            parent_widget = self.nametowidget(parent_path)
            # retrieve the first widget in the row 
            label_widget = parent_widget.grid_slaves(column = 0, row = 0)
            # get the label widget at row = 0, column = 0
            self.current_label = label_widget[0]

            print("This is the self.parent_frame: ", self.parent_frame)
            print("This is the parent_frame: ", parent_widget)

            # reset the recipe view 
            self.recipe_view.reset_recipe_view()

            # reset the hightlight from everything else 
            if self.parent_frame is not None:
                self.highlight_frame_widgets(color="white", frame_path=self.parent_frame)
            # highlight everything in the frame 
            self.highlight_frame_widgets(color = "red", frame_path=parent_widget)

            # # reset ingredients, amount, and unit 
            # self.reset_ingredients()

            # load recipe data to the widget fields
            print("this is the current label: ", self.current_label.cget("text"))
            self.load_recipe_data(recipe_name=self.current_label.cget("text"))

            
            self.current_recipe = self.current_label.cget("text")

            self.parent_frame = parent_widget


    # def change_name(self) -> None:
    #     '''
    #     add the function to change the label text in the edit tab 
    #     '''
    #     # get new recipe name 
    #     new_name = self.vars[0].get()
    #     # validate the recipe name
    #     validate_input_string(new_name)
    #     # get the recipe name and position
    #     id = Parser.recipe_to_id[self.current_recipe]
    #     recipe = Parser.yaml_dictionary[id]
    #     recipe["recipe"] = new_name
    #     # set the label to new_name
    #     self.current_label.configure(text = new_name)
    #     # write new name to the recipe
    #     self.write_to_yaml(file = INGREDIENT_FILE, data = Parser.yaml_dictionary)
    
    # def change_ingredient(self) -> None: 
    #      # get new recipe name 
    #     ingredient_name = self.combobox_1.get()
    #     # get the recipe name and position
    #     id = Parser.recipe_to_id[self.current_recipe]
    #     # load the recipe
    #     recipe = Parser.yaml_dictionary[id]
    #     # get the ingredient list
    #     ingredients = recipe["ingredients"]
    #     # set ingredient id to 0
    #     ingredient_id = 0
    #     for i, ingredient in enumerate(ingredients):
    #         if ingredient["ingredient"] == ingredient_name:
    #             ingredient_id = i
    #             break
    #     # removes ingredient at specified position
    #     new_ingredient = ingredients[ingredient_id]
    #     new_ingredient["ingredient"] = self.combobox_1.get()
    #     amount = self.vars[1].get()
    #     unit = self.combobox_2.get().split(" ")
    #     unit = unit[1].replace("(", "").replace(")", "")
    #     # check if the amount is valid number
    #     validate_input_number(unit)
    #     # define the new amount 
    #     new_ingredient["amount"] = f"{amount} {unit}"
    #     # write changes to the recipe 
    #     self.write_to_yaml(file = INGREDIENT_FILE, data = Parser.yaml_dictionary)
    
    # def reset_ingredients(self) -> None:
    #     self.combobox_1.set("")
    #     self.combobox_2.set("")
    #     self.vars[1].set("")

    # def remove_ingredient(self) -> None:
    #     # get new recipe name 
    #     ingredient_name = self.combobox_1.get()
    #     # get the recipe name and position
    #     id = Parser.recipe_to_id[self.current_recipe]
    #     # load the recipe
    #     recipe = Parser.yaml_dictionary[id]
    #     # get the ingredient list
    #     ingredients = recipe["ingredients"]
    #     # set ingredient id to 0
    #     ingredient_id = 0
    #     for i, ingredient in enumerate(ingredients):
    #         if ingredient["ingredient"] == ingredient_name:
    #             ingredient_id = i
    #             break
    #     # removes ingredient at specified position
    #     ingredients.pop(ingredient_id)
    #     self.value_list.remove(ingredient_name)
    #     self.combobox_1.configure(values = self.value_list)
    #     # reset ingredients
    #     self.reset_ingredients()

    #     # write changes to the recipe 
    #     self.write_to_yaml(file = INGREDIENT_FILE, data = Parser.yaml_dictionary)

    # loads recipe data
    def load_recipe_data(self, recipe_name: str):
        # get recipe name 
        self.recipe = Parser.name_to_recipe[recipe_name]
        # self.entry_1.configure(text = recipe_name)

        # set the recipe name
        self.edit_recipe.set_recipe_name(recipe_name)        

        # create a dictionary which maps the ingredients to the correspoding amount 
        self.value_list.clear()

        # get the ingredients of recipe
        self.ingredients = self.recipe["ingredients"]

        # load recipe data to the recipe view window 
        self.recipe_view.load_recipe_view(ingredients=self.ingredients)

        for ingredient in self.ingredients:
            name = ingredient["ingredient"]
            subcategory = ingredient["subcategory"]
            amount, unit = ingredient["amount"].split()
            # self.current_ingredients[name] = [amount, unit, subcategory]
            self.edit_recipe.current_ingredients[name] = [amount, unit, subcategory]
            self.value_list.append(name)

        self.edit_recipe.set_combobox(values = self.value_list)

        print("This is editor value_list: ", self.value_list)


    # def load_recipe_view(self, ingredients: list):
    #     for ingredient in ingredients:
    #         text = f"Ingredient: {ingredient["ingredient"]}, Subcategory: {ingredient["subcategory"]}, Amount: {ingredient["amount"]}"
    #         print("This is the text: ", text)
    #         label = ctk.CTkLabel(master=self.tab_2, text=text, text_color="White")
    #         label.pack(pady=5, padx=10, fill="x")

    def highlight_frame_widgets(self, color: str, frame_path: tk.Frame):
        frame_path.configure(fg_color = color)
        children_widgets = frame_path.winfo_children()
        for child_widget in children_widgets:
            child_widget.configure(fg_color = color)


    def add_recipes_to_list(self):
        for recipe_entry in Parser.yaml_dictionary:
            recipe_name = recipe_entry["recipe"]
            recipe_author = recipe_entry["author"]
            recipe_date = recipe_entry["date"]
            rating = recipe_entry["rating"]
            frame = ctk.CTkFrame(master=self.frame, corner_radius= 5, width=600, height=40, fg_color="white")
            frame.pack(expand = True, fill = "x")
            frame.bind("<Button-1>", self.highlight_frame)
            label_1 = ctk.CTkLabel(master=frame, height= 40, corner_radius= 5, text= recipe_name, 
                         text_color="black", width = 150, fg_color="white")
            label_1.grid(column = 0, row = 0, sticky = "ew")
            label_1.bind("<Button-1>", self.highlight_frame)
            label_2 = ctk.CTkLabel(master=frame, height= 40, corner_radius= 5, width = 150, text= recipe_author, 
                         text_color="black", fg_color="white")
            label_2.grid(column = 1, row = 0, sticky = "ew")
            label_2.bind("<Button-1>", self.highlight_frame)
            label_3 = ctk.CTkLabel(master=frame, height=40, corner_radius= 5, width = 150, text= recipe_date, 
                         text_color="black", fg_color="white")
            label_3.grid(column = 2, row = 0, sticky = "ew")
            label_3.bind("<Button-1>", self.highlight_frame)
            self.add_rating(frame = frame, size = rating)
           
    def add_rating(self, frame: tk.Frame, size: int = 5):
        frame_2 = ctk.CTkFrame(master=frame, corner_radius= 5, width = 150, fg_color="white", bg_color="white",
                               height = 40)
        frame_2.grid(column = 3, row = 0, sticky = "we")
        frame_2.bind("<Button-1>", self.highlight_frame)
        # frame_2.columnconfigure((0, 1, 2, 3, 4), weight = 1)

        for i in range(size):
            my_image = ctk.CTkImage(light_image=Image.open(STAR_IMAGE_PATH),
                                    dark_image=Image.open(STAR_IMAGE_PATH),
                                    size=(20, 20))
            
            image_label = ctk.CTkLabel(master=frame_2, corner_radius=5, width= 30, height= 40, image=my_image, text="")
            image_label.grid(column = i, row = 0, sticky = "we")      
   
        
if __name__ == "__main__":
    Editor()

