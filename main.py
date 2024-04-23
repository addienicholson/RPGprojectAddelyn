
from Food import *
from Recipe import *
from PublixMap import *
from Aisle import *

def start_statement():
    print("Welcome to Remi's Delicious Escape! Please enter any key to continue.")
    x = input()
    print("You wake up dazed and confused, handcuffed to a large bread stick. Your little rat fingers are cold and you wonder how long you've been here in Publix. Suddenly, you notice him. SKINNER! He's mad you make better ratatouille than him.")
    print()
    print("\"Good morning Remi. You've pissed me off so much that I'm going to turn you into my own dinner!\"")
    print()
    print("You know what you have to do. It's time to escape!")
    print("To win, you must steal the ingredients from Publix to ensure Skinner can't cook you. Enter any key to acknowledge this.")
    x = input()
    print("It's time to begin. You may forfeit and turn yourself into soup at any time by entering 'exit'. Let's start, enter any key to begin!")
    x = input()
    if x == 'exit':
        exit(1)

def exit_game(input_):
    if input_ == "Exit" or input_ == 'exit':
        exit(1)

def print_map(line1, line2):
    print("----------------------MAP OF PUBLIX-------------------------")
    print("------------------------------------------------------------")
    print(line1)
    print(line2)
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")

def print_recipe(user_input, recipe):
    """makes sure the user opts to open recipe and prints the recipe
    """
    if user_input == 'open recipe book' or user_input == 'open recipe':
        print(recipe)

def check_alternate_input_bool(user_input, refrigerator, shelves, recipe):
    if user_input == 'open map':
        print_map(refrigerator, shelves)
        return True

    if user_input == 'open recipe book' or user_input == 'open recipe':
        print(recipe)
        return True

def check_alternate_input(user_input, refrigerator, shelves, recipe):
    if user_input == 'open map':
        print_map(refrigerator, shelves)

    if user_input == 'open recipe book' or user_input == 'open recipe':
        x = 0
        #skips because the recipe will be printed at each iteration of the loop
        
        

class IngredientError(Exception):
    #custom error for the case that the ingredient the player asks for is in the grocery store but is in the wrong aisle.
    pass

def main():

    publix_map = PublixMap()
    recipe = Recipe()
    start_statement()
    
    shelves = Aisle('Shelves',['Noodles', 'Garlic', 'Tomato Sauce'])
    refrigerator = Aisle('Refrigerator', ['Meatballs', 'Cheese', 'Butter', 'Dough'])

    publix_map.add_section(shelves)
    publix_map.add_section(refrigerator)

    print("You must first get out of these handcuffs. Enter 1 if you plead Skinner to take them off. Enter 2 if you want to gnaw them off yourself.")
    exit_choice = input()
    while exit_choice not in ['1','2', 'Exit', 'exit']:
        print("Please enter a valid choice: 1 or 2")
        exit_choice = input().title()
        exit_game(exit_choice)
    exit_game(exit_choice)

    if exit_choice == '1':
        print("You beg Skinner to take them off of you and he takes pity, but he says you're pathetic and weak and decides you're unfit to choose your death dish. He decides you will be spaghetti.")
        meal_choice = 'Spaghetti'
    else:
        print("You gnaw yourself out of captivity with your rat teeth and Skinner is impressed with your indomitable rodent spirit. He decides you will pick the dish. Your options are: Spaghetti, Pizza, or Breadsticks.")
        print("Please enter your choice.")
        meal_choice = input().strip().title()
        exit_game(meal_choice)
        while meal_choice not in ['Spaghetti','Pizza','Breadsticks']:
            print("Please enter a valid choice: Spaghetti, Pizza, or Breadsticks")
            meal_choice = input().strip().title() 
            exit_game(meal_choice)
        print(f"If you don't hurry, you will be turned into {meal_choice}!")

    dish = Food()
    dish.set_food_name(meal_choice)
    dish.set_cook_time(meal_choice)
    dish.set_ingredients(meal_choice)
    
    recipe.set_food_name(meal_choice)
    recipe.set_cook_time(meal_choice)
    recipe.set_ingredients(meal_choice)

    print()
    print("Skinner hands you a recipe book and a map of Publix. You may open them at any time.")
    user_input = input().strip().lower()
    exit_game(user_input)
    
    while user_input !=  'open recipe' and user_input != 'open recipe book':
        print("Try opening the recipe book to get an idea of the ingredients you need to find!")
        user_input = input()
        exit_game(user_input)
 
    else:
        print()
        print_recipe(user_input, recipe)

    print("Now try opening the map!")

    user_input = input().strip().lower()
    while user_input != 'open map' and user_input != 'open publix map':
        print("Try opening the map so you can navigate to the ingredients you need!")
        user_input = input().strip().lower()
        exit_game(user_input)
    
    print_map(refrigerator, shelves)
  
    print("Now that you know what ingredients you need and where to get them! It's time to go get them!")
    
    #begins the inventory process
    inventory = []
    while len(inventory) < 3:
        
        try:
            
            print("Which aisle do you wish to go to? Enter shelves or refrigerator.")
            user_input = input().strip().lower()
            exit_game(user_input)
            while user_input != 'shelves' and user_input != 'refrigerator' and user_input != 'open recipe book' and user_input != 'open recipe' and user_input != 'open map':
                print("Please enter a valid input.")
                user_input = input().strip().lower()
                exit_game(user_input)
            
            if check_alternate_input_bool(user_input, refrigerator, shelves, recipe):
                check_alternate_input(user_input, refrigerator, shelves, recipe)
                continue

            if user_input == 'refrigerator':
                chosen_aisle = Aisle('Refrigerator', ['Meatballs', 'Cheese', 'Butter', 'Dough'])
                print("You are now in the refrigerator aisle with items : Meatballs, Cheese, Butter, and Dough.")
                print("Which item would you like to grab?")
                item = input().title().strip()
                exit_game(item)
                if item in shelves.get_ingredients() or item in refrigerator.get_ingredients():
                    if item not in refrigerator.get_ingredients():
                        raise IngredientError
            
            elif user_input == 'shelves':
                chosen_aisle = Aisle('Shelves',['Noodles', 'Garlic', 'Tomato Sauce'])
                print("You are now in the shelves aisle with items: Noodles, Garlic, Tomato Sauce.")
                print("Which item would you like to grab?")
                item = input().strip().title()
                exit_game(item)
                if item in shelves.get_ingredients() or item in refrigerator.get_ingredients():    
                    if item not in shelves.get_ingredients():
                        raise IngredientError
                        continue
                else:
                    print(f"{item} is not on the ingredients list for {meal_choice}. Check your menu again!")
                    continue
        
        except IngredientError:
            if user_input == 'refrigerator':
                print(f"Wrong aisle! Check for {item} in Shelves. Leaving refrigerator...")
            else:
                print(f"Wrong aisle! Check for {item} in Refrigerator. Leaving shelves...")

        try:
            recipe.remove_ingredient(item.title())
        except ValueError:
            print(f"{item} is not on the ingredients list for {meal_choice}. Check your menu again!")

        if item in dish.get_ingredients() and item in chosen_aisle.get_ingredients():
            with open('output.txt', 'a') as output_text:
                output_text.write(f"{item}\n")
            inventory.append(item)
            print()
            print(f"{item} removed from recipe and in inventory!")
            
        print(recipe)

        item = None 

    print()
    print(f"Congrats! You have all the necessary ingredients to create {meal_choice}")
    print(f"Now, cook your meal to make sure Skinner can't steal them back from you! For how many minutes would you like to cook your {meal_choice}?")
    cook_time = input()
    while cook_time.isalpha():
        print("Invalid input. Please enter a number.")
        cook_time = input()
    cook_time = int(cook_time)

    if cook_time < dish.get_cook_time():
        print(f"OH NO !!! you undercooked your {meal_choice}! Skinner simply placed you inside the raw contents and you died. Game over. ")
    elif cook_time > dish.get_cook_time():
        print(f"OH NO !!! your {meal_choice} was so overdone that Skinner lit you on fire and burnt you to a crisp so that you blend right in. Game over.")
    else:
        f = open('output.txt')
        contents = f.readlines()
        print(f"Congratulations! You stole {contents} from Skinner before he could cook you! You win!")
        f.close()
        
    #need to fix file reading
    #need to add comments

if __name__ == '__main__':
    main()

