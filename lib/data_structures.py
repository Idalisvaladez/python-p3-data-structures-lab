spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
# When accessing data in dictionaries {} use bracket notation & key for the value you want
def get_names(spicy_foods):
    name_list = [food["name"] for food in spicy_foods ] #doing list comprehension
    #gets the name of our food in the list of dicts
    return name_list

# list comprehension to return food with heat greater than 5
def get_spiciest_foods(spicy_foods):
    spiciest_list = [food for food in spicy_foods if (food["heat_level"] > 5)]
    return spiciest_list


#for loop instead of list comprehention if more than one line of code
#for loop to print the name, cusine and heatlevel with the emoji
#multiply emoji by heat level number to get the correct number
def print_spicy_foods(spicy_foods):
   for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * '🌶'}")


# for loopget food from list if it == cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

#prints the name, cuisine and heat_level in emojis if heat_level is greater than 5
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * '🌶'}")


#use sum() to add integers of a list
# to get the average divide by the length of our list 
def get_average_heat_level(spicy_foods):
    average_heat = sum([heat["heat_level"] / len(spicy_foods) for heat in spicy_foods])
    return average_heat


# add new food with .append() and return the updated list with existing values still inside
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    
