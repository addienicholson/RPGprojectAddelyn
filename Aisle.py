from Food import *

class Aisle:
    def __init__(self, aisle, ingredients):
        self.aisle = aisle
        self.ingredients = ingredients

    def get_aisle(self):
        return self.aisle
    
    def get_ingredients(self):
        return self.ingredients

    def list_ingredients(self):
        return_str = ''
        for ingredient in self.ingredients:
            return_str += f"{ingredient}, "
        return return_str

    def __str__(self):
        return f'{self.get_aisle()}: {self.list_ingredients()}'