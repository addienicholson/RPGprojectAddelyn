#Food class that establishes each food's name, cook time, and ingredients which will be used to determine if the user wins or not

class Food:
    
    def __init__(self):
        self.name = ''
        self.cook_time = 0
        self.ingredients = []
    
    def set_food_name(self, name): #sets name
        if name == 'Spaghetti':
            self.name = 'Spaghetti'
        elif name == 'Pizza':
            self.name = 'Pizza'
        elif name == 'Breadsticks':
            self.name = 'Breadsticks'

    def get_food_name(self): #returns name to be used main
        return self.name

    def set_cook_time(self, name): #sets cooktime based on name
        if name == 'Spaghetti':
            self.cook_time = 25
        elif name == 'Pizza':
            self.cook_time = 20
        elif name == 'Breadsticks':
            self.cook_time = 40
    
    def get_cook_time(self): #returns cooktime to be used in main
        return self.cook_time

    
    def set_ingredients(self, name): #sets each dish's ingredients based on the name
        if name == 'Spaghetti':
            self.ingredients = ['Noodles','Marinara','Meatballs']
        elif name == 'Pizza':
            self.ingredients = ['Dough', "Marinara", 'Cheese']
        elif name == 'Breadsticks':
            self.ingredients = ['Dough', 'Garlic', 'Butter']
    
    def get_ingredients(self): #returns ingredients for use below and in main
        return self.ingredients

    def list_ingredients(self): #creates a string of the list of ingredients
        return_str = ''
        for ingredient in self.ingredients:
            return_str += f'{ingredient}, '
        return return_str
    
    def __str__(self): #creates printable format of the object
        return f"{self.get_food_name()}: Need: {self.list_ingredients()}Cook for {self.get_cook_time()} minutes."