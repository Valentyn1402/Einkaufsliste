import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from grocceries_UI import Grocceries
from recipe_UI import Recipe

'''
Important Widgets
'''

class App(ctk.CTk):
    
    def __init__(self) -> None:

        super().__init__()
        
        # create modern fonts
        self.font_1 = ctk.CTkFont("Anona", 12, "bold")

        ctk.set_appearance_mode("dark")
        
        # add buttons
        self.define_menu_buttons()

        self.geometry('700x400')
        self.title("Food App")

        # initialize variables 
        self.groccerie_ui = None
        
        # initialize mainloop
        self.mainloop()

    def define_menu_buttons(self):
        ctk.CTkButton(self, text = "Generate groccerie list", font=self.font_1, hover_color="red", 
                      border_color="white", border_width=2, command=self.open_groccerie_generator).pack(expand = True, side = "left")
        ctk.CTkButton(self, text = "Add Recipe", font=self.font_1, hover_color="red", 
                      border_color="white", border_width=2, command=self.open_add_recipe).pack(expand = True, side = "right")
        
    def open_groccerie_generator(self):
        self.groccerie_ui = Grocceries()

    def open_add_recipe(self):
        self.groccerie_ui = Recipe()



if  __name__ == "__main__" :
    ui = App()
