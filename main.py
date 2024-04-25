"""
Author:         Addelyn Nicholson
Date:           04/05/2024
Assignment:     Project 02
Course:         CPSC1050
Lab Section:    SECTION 001

CODE DESCRIPTION: This project utilizes various classes, methods, and functions to create a terminal based RPG escape game. The premise of the game is that Remi from Ratatouille is recaptured by the villain, Skinner. 
GITHUB: https://github.com/addienicholson/RPGprojectAddelyn.git
"""

from Food import *
from Recipe import *
from PublixMap import *
from Aisle import *

def start_statement():
    """prints the starting prompt for the game. declutters main function.

        args: none
        return: none, only prints
    """
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
    """checks if the user's input is exit. this function will exit the game if so. Serves to declutter the main function.
    args: 
        input: the user's input to a given prompt.
    return: nothing. exits the program.
    """
    if input_ == "Exit" or input_ == 'exit':
        exit(1)

def print_map(line1, line2):
    """prints the map of publix which displays what items are in each aisle.
    args:
        line1: the first aisle and its contents(refrigerator or shelves)
        line2: the second aisle and its contents
    return: nothing. just prints
    """
    print("----------------------MAP OF PUBLIX-------------------------")
    print("------------------------------------------------------------")
    print(line1)
    print(line2)
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")

def print_recipe(user_input, recipe):
    """makes sure the user opts to open recipe and prints the recipe
        args:
            user_input: string of the user's response to a prompt.
            recipe: the recipe for the chosesn dish
        return: nothing just prints
    """
    if user_input == 'open recipe book' or user_input == 'open recipe':
        print(recipe)

def check_alternate_input_bool(user_input, refrigerator, shelves, recipe):
    """creates a bool for the condition that the map should be open
        args:
            user_input: user's string
            refrigerator: class aisle with the refrigerators contents
            shelves: class aisle with the shelve's contents
            recipe: class recipe with the chosen dishes ingredients
        return:
            boolean that triggers the map opening
    """

    if user_input == 'open map':
        print_map(refrigerator, shelves)
        return True

    if user_input == 'open recipe book' or user_input == 'open recipe':
        print(recipe)
        return True

def check_alternate_input(user_input, refrigerator, shelves, recipe):
    """makes sure the user hasn't input open recipe. then skips the entire loop.
        args:
            user_input: user's string
            refrigerator: class aisle with the refrigerators contents
            shelves: class aisle with the shelve's contents
            recipe: class recipe with the chosen dishes ingredients
        return:
            nothing. skips looop.
    """

    if user_input == 'open map':
        print_map(refrigerator, shelves)

    if user_input == 'open recipe book' or user_input == 'open recipe':
        x = 0
        #skips because the recipe will be printed at each iteration of the loop
        
        

class IngredientError(Exception):
    """custom error for the case that the ingredient the player asks for is in the grocery store but is in the wrong aisle."""
    pass

def main():

    publix_map = PublixMap() #creates instances of each class
    recipe = Recipe()
    start_statement()
    
    shelves = Aisle('Shelves',['Noodles', 'Garlic', 'Marinara'])
    refrigerator = Aisle('Refrigerator', ['Meatballs', 'Cheese', 'Butter', 'Dough'])

    publix_map.add_section(shelves) #adds aisles to the map
    publix_map.add_section(refrigerator)

    print("You must first get out of these handcuffs. Enter 1 if you plead Skinner to take them off. Enter 2 if you want to gnaw them off yourself.")
    exit_choice = input()
    while exit_choice not in ['1','2', 'Exit', 'exit']: #validates exit input
        print("Please enter a valid choice: 1 or 2")
        exit_choice = input().title()
        exit_game(exit_choice)
    exit_game(exit_choice)

    if exit_choice == '1': #condition one. picks spaghetti for the user
        print("You beg Skinner to take them off of you and he takes pity, but he says you're pathetic and weak and decides you're unfit to choose your death dish. He decides you will be spaghetti.")
        meal_choice = 'Spaghetti'
    else: #condition 2. user picks their own dish
        print("You gnaw yourself out of captivity with your rat teeth and Skinner is impressed with your indomitable rodent spirit. He decides you will pick the dish. Your options are: Spaghetti, Pizza, or Breadsticks.")
        print("Please enter your choice.")
        meal_choice = input().strip().title()
        exit_game(meal_choice)
        while meal_choice not in ['Spaghetti','Pizza','Breadsticks']:
            print("Please enter a valid choice: Spaghetti, Pizza, or Breadsticks")
            meal_choice = input().strip().title() 
            exit_game(meal_choice)
        print(f"If you don't hurry, you will be turned into {meal_choice}!")

    dish = Food() #creates food instance
    dish.set_food_name(meal_choice)
    dish.set_cook_time(meal_choice)
    dish.set_ingredients(meal_choice)
    
    #sets the items for the recipe based on the chosen dish
    recipe.set_food_name(meal_choice)
    recipe.set_cook_time(meal_choice)
    recipe.set_ingredients(meal_choice)

    print()
    print("Excited to eat you for dinner, Skinner accidentally drops a recipe book and a map of Publix. You may open them at any time.") #prompts user to open recipe book and map
    user_input = input().strip().lower()
    exit_game(user_input)
    
    while user_input !=  'open recipe' and user_input != 'open recipe book': #validates input
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
                
                if item in inventory:
                    print("You only need one of this ingredient!")
                    continue
                
                if item in shelves.get_ingredients() or item in refrigerator.get_ingredients():
                    if item not in refrigerator.get_ingredients():
                        raise IngredientError
                
            
            elif user_input == 'shelves':
                
                chosen_aisle = Aisle('Shelves',['Noodles', 'Garlic', 'Marinara'])
                print("You are now in the shelves aisle with items: Noodles, Garlic, Marinara.")
                print("Which item would you like to grab?")
                item = input().strip().title()
                
                if item in inventory: #case for if the same ingredient is requested more than once
                    print("You only need one of this ingredient!")
                    continue
                
                exit_game(item)
                if item in shelves.get_ingredients() or item in refrigerator.get_ingredients():    
                    if item not in shelves.get_ingredients():
                        raise IngredientError
                        continue
                else: #case for if the item isn't in the selected dishes ingredient list
                    print(f"{item} is not on the ingredients list for {meal_choice}. Check your menu again!")
                    continue
        
        except IngredientError: #error raised if the customer asks for an item on a different aisle
            if user_input == 'refrigerator':
                print(f"Wrong aisle! Check for {item} in Shelves. Leaving refrigerator...")
            else:
                print(f"Wrong aisle! Check for {item} in Refrigerator. Leaving shelves...")

        if item not in inventory: #only runs if the item hasn't been requested
            try:
                recipe.remove_ingredient(item.title()) #Removes the ingredient from the recipe 
            except ValueError:
                print(f"{item} is not on the ingredients list for {meal_choice}. Check your menu again!")


        if item in dish.get_ingredients() and item in chosen_aisle.get_ingredients() and item not in inventory:
            with open('output.txt', 'a') as output_text: #appends the item into the output text which holds 
                output_text.write(f"{item};")
            inventory.append(item) #appens to the inventory in this file used to guess if the item has been requested
            print()
            print(f"{item} removed from recipe and in inventory!") #removes item from the recipe. the user no longer needs it
            
        print(recipe)

        item = None #makes item null incase some of the assignments are skipped due to input errors / exceptions so that the item isn't put in ouput text more than once

    #inventory done. now time to decide if the user wins or not.

    print()
    print(f"Congrats! You have all the necessary ingredients to create {meal_choice}")
    print(f"Now, cook your meal to make sure Skinner can't steal them back from you! For how many minutes would you like to cook your {meal_choice}?")
    cook_time = input()
    while not cook_time.isdigit(): #validating input
        print("Invalid input. Please enter a number.")
        cook_time = input()
    cook_time = int(cook_time)

    if cook_time < dish.get_cook_time(): #case where the ingredients are undercooked
        print(f"OH NO !!! you undercooked your {meal_choice}! Skinner simply placed you inside the raw contents and you died. Game over. ")
    elif cook_time > dish.get_cook_time(): #case where the ingredients are burnt
        print(f"OH NO !!! your {meal_choice} was so overdone that Skinner lit you on fire and burnt you to a crisp so that you blend right in. Game over.")
    else:
        f = open('output.txt') #opens output text and assigns each item with a local variable to be read in the final statement.
        contents = f.read()
        contents = contents.split(";")
        item1 = contents[0] 
        item2 = contents[1]
        item3 = contents[2]
        print(f"Congratulations! You stole {item1}, {item2}, and {item3} from Skinner before he could cook you! You win!")
        f.close()
        
if __name__ == '__main__':
    main()

