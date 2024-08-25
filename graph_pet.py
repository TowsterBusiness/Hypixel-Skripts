import requests as req
import matplotlib.pyplot as plt
import numpy as np
from pet_exp_calc import pet_level_to_exp
from colors import bcolors
import json
import re 

rarity = "EPIC"

with open('cache/cache.json', 'r') as openfile:
    auc_list = json.load(openfile)["auctions"]
with open('cache/pet_list.json', 'r') as openfile:
    pet_list = json.load(openfile)["pet_list"]

emanList = []

low_tier_min = float('inf')
low_tier_min_lvl = 100
max_tier_min = float('inf')
max_tier_min_lvl = 0

print(bcolors.OKCYAN + "Auction Number: " + str(len(auc_list)) + bcolors.ENDC)

for auc in auc_list:
    if auc["item_name"].endswith("Enderman") and auc["tier"] == rarity and auc["bin"] == True:
        price = auc["starting_bid"]
        
        print("Item: " + auc["item_name"] + " " + str(price))
        
        # gets the pet level then removes "] " after the pet level to account for [Level 1] to [Level 100]
        pet_level = int(auc["item_name"][5:8].replace("]", "").replace(" ", ""))
        
        # gets current exp
        if pet_level != 100:
            exp = auc["item_lore"][(auc["item_lore"].find("§l§m §r §e") + 10):-1]
            exp = exp[0:(exp.find("§6/"))]
            exp = exp.replace(",", "")
            exp = float(exp)
        else: exp = 0
        
        
        if pet_level > max_tier_min_lvl:
            max_tier_min = price
            max_tier_min_lvl = pet_level
        elif pet_level < low_tier_min_lvl:
            low_tier_min = price
            low_tier_min_lvl = pet_level
        elif pet_level == 100:
            max_tier_min = min(max_tier_min, price)
        elif pet_level == 1:
            low_tier_min = min(low_tier_min, price)
            
            
                    
        emanList.append([pet_level_to_exp(rarity=auc["tier"].lower(), level=pet_level, exp=exp), auc["starting_bid"]])

if low_tier_min == float('inf') or max_tier_min == float('inf'):
    print(bcolors.FAIL + "There were no pets of that kind" + bcolors.ENDC)
    
# getting the line graph info
plot_m = (max_tier_min - low_tier_min) / (pet_level_to_exp(rarity=rarity, level=100) - pet_level_to_exp(rarity=rarity, level=1))
plot_b = max_tier_min - plot_m * (pet_level_to_exp(rarity=rarity, level=100))

fig, ax = plt.subplots(figsize=(6, 6))
# naming the x axis
plt.xlabel('Pet Level')
# naming the y axis
plt.ylabel('Price')
# giving a title to my graph
plt.title('Eman Graph')
        
# graphing the supposed scale
if low_tier_min == float('inf'):
    low_tier_min = 0
ax.plot([0, pet_level_to_exp(rarity=rarity, level=100)], [low_tier_min, max_tier_min], label="Line", color="red")

x_plot = []
y_plot = []
color_plot = []
for eman in emanList:
    x_plot.append(eman[0])
    y_plot.append(eman[1])
    if eman[1] < eman[0] * plot_m + plot_b:
        color_plot.append('pink')
    else:
        color_plot.append('blue')
        
# plotting the points
ax.scatter(np.array(x_plot), np.array(y_plot), c=np.array(color_plot))



# function to show the plot
plt.show()
