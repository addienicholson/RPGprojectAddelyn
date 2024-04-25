#creates the class Recipe which serves to remind the user what items they still need from Publix and how long to cook the dish
from Food import *

class Recipe(Food): 
    def __init__(self):
        Food.__init__(self)
        self.recipe = {self.get_food_name(): [self.list_ingredients(), self.get_cook_time]}
    
    def remove_ingredient(self, input_): #remvoes the ingredient from the recipe once it is grabbed off of the shelf
        self.ingredients.remove(input_)