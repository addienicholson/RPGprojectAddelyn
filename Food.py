class Food:
    
    def __init__(self):
        self.name = ''
        self.cook_time = 0
        self.ingredients = []
    
    def set_food_name(self, name):
        if name == 'Spaghetti':
            self.name = 'Spaghetti'
        elif name == 'Pizza':
            self.name = 'Pizza'
        elif name == 'Breadsticks':
            self.name = 'Breadsticks'

    def get_food_name(self):
        return self.name

    def set_cook_time(self, name):
        if name == 'Spaghetti':
            self.cook_time = 25
        elif name == 'Pizza':
            self.cook_time = 20
        elif name == 'Breadsticks':
            self.cook_time = 40
    
    def get_cook_time(self):
        return self.cook_time

    
    def set_ingredients(self, name):
        if name == 'Spaghetti':
            self.ingredients = ['Noodles','Tomato Sauce','Meatballs']
        elif name == 'Pizza':
            self.ingredients = ['Dough', "Tomato Sauce", 'Cheese']
        elif name == 'Breadsticks':
            self.ingredients = ['Dough', 'Garlic', 'Butter']
    
    def get_ingredients(self):
        return self.ingredients

    def list_ingredients(self):
        return_str = ''
        for ingredient in self.ingredients:
            return_str += f'{ingredient}, '
        return return_str
    
    def __str__(self):
        return f"{self.get_food_name()}: Need: {self.list_ingredients()}Cook for {self.get_cook_time()} minutes."