import tkinter as tk

outfits_closet = [
    {"max_temp": 32, "top": "Heavy Coat", "bottoms": "Pants", "shoes": "Sneakers"},
    {"max_temp": 45, "top": "Jacket", "bottoms": "Pants", "shoes": "Sneakers"},
    {"max_temp": 60, "top": "Hoodie", "bottoms": "Pants", "shoes": "Sneakers"},
    {"max_temp": 75, "top": "Long Sleeve Shirt", "bottoms": "Shorts", "shoes": "Sneakers"},
    {"max_temp": 89, "top": "Short Sleeve Shirt", "bottoms": "Shorts", "shoes": "Sneakers"},
    {"max_temp": 120, "top": "Tank Top", "bottoms": "Shorts", "shoes": "Flip Flops"},
    {"max_temp": 100000, "top": "No Shirt", "bottoms": "Underwear", "shoes": "Barefoot"}
]

def fitgenerator():
    try:
        temp = int(enter_temp.get())
        condition = weather.get()
        result = find_outfit(temp, condition)
        output.config(text= result)
    except ValueError:
        output.config(text = "Please Enter A Valid Number!")

def find_outfit(temp, condition):
    final_outfit = []
    for i in outfits_closet:
        if temp <= i["max_temp"]:
            final_outfit = [i["top"], i["bottoms"], i["shoes"]]
            break

    if condition == "Rainy":
        final_outfit[0] = "Rain Jacket"
        final_outfit[2] = "Rain Boots"
    elif condition =="Snowy":
        if temp > 35:
            return "Too warm for Snow! Check the Weather Again!!"
        else:
            final_outfit[0] = "Snow Coat"
            final_outfit[2] = "Snow Boots"

    message = "Here is your Fit --> "
    for i in range (len(final_outfit)):
        message += final_outfit[i].upper()
        if i < len(final_outfit) - 1:
            message += ", "
    return message

root = tk.Tk()
root.title("Outfit Generator")
root.geometry("425x350")
root.configure(bg="SteelBlue2")

tk.Label(root, text = "Temperature Outside(F): ", bg="SteelBlue2", font = ("Comic Sans MS", 12)).pack(pady=10)
enter_temp = tk.Entry(root)
enter_temp.pack()

tk.Label(root, text = "Current Weather Conditions: ", bg="SteelBlue2", font = ("Comic Sans MS", 12)).pack(pady=10)
weather = tk.StringVar(value="Sunny")
dropdown = tk.OptionMenu(root, weather, "Sunny", "Rainy", "Snowy")
dropdown.config(bg="SteelBlue2", font = ("Comic Sans MS", 10))
dropdown.pack(pady=10)

tk.Button(root, text= "Press to make your fit ", command = fitgenerator, bg = "green2", fg = "black", font = ("Comic Sans MS", 12)).pack(pady=20)
output = tk.Label(root, text = "", font = ("Comic Sans MS", 10), bg="SteelBlue2")
output.pack()

root.mainloop()
