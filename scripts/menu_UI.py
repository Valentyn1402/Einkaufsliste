import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from grocceries_UI import Grocceries, Tab_1
from recipe_UI import Recipe

'''
Important Widgets
'''

class App(ctk.CTk):
    
    def __init__(self) -> None:

        super().__init__()
        
        # create modern fonts
        self.font_1 = ctk.CTkFont("Anona", 16, "bold")

        # create tab view
        self.create_tabview()

        # create the layout for tab 1 
        Tab_1(parent=self.tab_1)

        # create labels 

        ctk.set_appearance_mode("dark")
    
        self.geometry('700x400')
        self.configure(font = self.font_1)
        self.title("Food App")

        # initialize variables 
        self.groccerie_ui = None
        
        # initialize mainloop
        self.mainloop()

    def create_tabview(self):
        self.tabview = ctk.CTkTabview(master=self, width=600, height=300, anchor="w")
        self.tabview.pack(padx=20, pady=20)

        self.tab_1 = self.tabview.add("Generate Groccerie List")  # add tab at the end
        self.tab_2 = self.tabview.add("Add Recipe")  # add tab at the end
        self.tab_3 = self.tabview.add("Edit Recipe")  # add tab at the end
        self.tabview.set("Generate Groccerie List")  # set currently visible tab
        
    def open_groccerie_generator(self):
        self.groccerie_ui = Grocceries()

    def open_add_recipe(self):
        self.groccerie_ui = Recipe()



if  __name__ == "__main__" :
    ui = App()
