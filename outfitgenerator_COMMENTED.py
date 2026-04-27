# Code Created by Vincent Alberico and Andrew Wang

import tkinter as tk # importing tkinter in order to make the guis
# Vincent Alberico
outfits_closet = [ # list of dictionaries for the different outfits
    {"max_temp": 32, "top": "Heavy Coat", "bottoms": "Pants", "shoes": "Sneakers"}, # outfit for less than 32 degrees
    {"max_temp": 45, "top": "Jacket", "bottoms": "Pants", "shoes": "Sneakers"}, # outfit from 32 to 45
    {"max_temp": 60, "top": "Hoodie", "bottoms": "Pants", "shoes": "Sneakers"}, # outfit from 46 to 60
    {"max_temp": 75, "top": "Long Sleeve Shirt", "bottoms": "Shorts", "shoes": "Sneakers"}, # outfit from 61 to 75
    {"max_temp": 89, "top": "Short Sleeve Shirt", "bottoms": "Shorts", "shoes": "Sneakers"}, # outfit from 76 to 89
    {"max_temp": 120, "top": "Tank Top", "bottoms": "Shorts", "shoes": "Flip Flops"}, # outfit from 90 to 120
    {"max_temp": 100000, "top": "No Shirt", "bottoms": "Underwear", "shoes": "Barefoot"} # outfit for above 120 degrees
]
# Andrew Wang
def fitgenerator(): # function that generates the outfit based on the weather
    try: # tests all integers
        # following 2 lines co created with Gemini AI
        temp = int(enter_temp.get()) # converts the string value inputted into an integer value that is easeir to read by the program
        condition = weather.get() # the weather options: Sunny, Rainy, Snowy
        result = find_outfit(temp, condition) # the final result of the fit generator is the find outfit function involving the temperature and the weather condition
        output.config(text = result)# the output is the output being found 
    except ValueError: # if an integer value is not read, then output
        output.config(text = "Please Enter A Valid Number!") # output if an integer number is not input
# Vincent Alberico
def find_outfit(temp, condition): # outfit finder function with parameters on temperature and weather condition
    final_outfit = [] 

# co created with Gemini AI
    for i in outfits_closet: # Iterates through the list of dictionaries to find the first match for the temperature range
        if temp <= i["max_temp"]: # checks the max temp of each output, if the input temp is less than or equal to the max temp
            final_outfit = [i["top"], i["bottoms"], i["shoes"]] # then the final output is printed based on the parameters of the temperature
            break # stops searching for different outfits
# end co creation with Gemini AI

# Vincent Alberico
    if condition == "Rainy": # exceptions for the rain
        final_outfit[0] = "Rain Jacket" # the final outfit top changes to a rain jacket
        final_outfit[2] = "Rain Boots" # teh final outfit shoes change to rain boots
    elif condition =="Snowy": # if not sunny or rainy, and it is snowy
        if temp >= 35: # does not work if snow is clicked with more than 35 degrees outside
            return "Too warm for Snow! Check the Weather Again!!"
        else: # if less than 32, then outfit gives snow coat and snow boots
            final_outfit[0] = "Snow Coat" # outfit top changes to snow coat despite whatever it is
            final_outfit[2] = "Snow Boots" # outfit shoes change to the snowboots
# Andrew Wang
    message = "Here is your Fit --> " # the final message output that is always there
    for i in range (len(final_outfit)):  # Iterates through the list by index to concatenate string values into a single output message
        message += final_outfit[i].upper() # what is displayed is hte message above along with the outfit
        if i < len(final_outfit) - 1: # if the position in the final outfit is less than teh total amount of objects in the list
            message += ", " # a comma is placed between each word
    return message # the final message is returned to the user
# Vincent Alberico
root = tk.Tk() # builds the GUI
root.title("Outfit Generator") # Title of the GUI
root.geometry("425x350") # GUI Dimensions
root.configure(bg="SteelBlue2") # Background Color the GUI

tk.Label(root, text = "Temperature Outside(F): ", bg="SteelBlue2", font = ("Comic Sans MS", 12)).pack(pady=10) # builds the temperature outside label text changes the color and font
enter_temp = tk.Entry(root) # this temperature entry is entered into the gui
enter_temp.pack()

tk.Label(root, text = "Current Weather Conditions: ", bg="SteelBlue2", font = ("Comic Sans MS", 12)).pack(pady=10) # customizaiton of weather conditions

#co created with Gemini AI
weather = tk.StringVar(value="Sunny")# first available selection
dropdown = tk.OptionMenu(root, weather, "Sunny", "Rainy", "Snowy") # other dropdown options
dropdown.config(bg="SteelBlue2", font = ("Comic Sans MS", 10)) # dropdown configurations
dropdown.pack(pady=10) # packs
# end co creatiion with Gemini AI
# Vincent Alberico
tk.Button(root, text= "Press to make your fit ", command = fitgenerator, bg = "green2", fg = "black", font = ("Comic Sans MS", 12)).pack(pady=20) # fit generator button
output = tk.Label(root, text = "", font = ("Comic Sans MS", 10), bg="SteelBlue2") # configuration of the output text
output.pack()

root.mainloop() # keeps gui on screen
