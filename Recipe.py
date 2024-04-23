from Food import *

class Recipe(Food): 
    def __init__(self):
        Food.__init__(self)
        self.recipe = {self.get_food_name(): [self.list_ingredients(), self.get_cook_time]}

    def open_recipe_book(self):
        is_recipe_book_open = True
        return is_recipe_book_open
    
    def remove_ingredient(self, input_): #make sure you validate this input that it is exactly "cross out blank"
        self.ingredients.remove(input_)