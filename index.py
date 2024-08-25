import numpy as np
from pet_exp_calc import pet_level_to_exp
from colors import bcolors
import json
import re

rarities = ["COMMON", "UNCOMMON", "RARE", "EPIC", "LEGENDARY"]

all_margin = []

with open('cache/pet_cache.json', 'r') as openfile:
    auc_list = json.load(openfile)["auctions"]
with open('cache/pet_list.json', 'r') as openfile:
    pet_list = json.load(openfile)["pet_list"]
with open('cache/pet_blacklist.json', 'r') as openfile:
    pet_blacklist = json.load(openfile)["pets"]

print(bcolors.OKCYAN + "Auction Number: " + str(len(auc_list)) + bcolors.ENDC)
for pet_name in pet_list:
    if pet_name in pet_blacklist:
        continue
    for rarity in rarities:
        pet_margins = []
        pet_prices = []

        low_tier_min = float('inf')
        low_tier_min_lvl = 100
        max_tier_min = float('inf')
        max_tier_min_lvl = 0

        for auc in auc_list:
            if auc["item_name"].endswith(pet_name) and auc["tier"] == rarity and auc["bin"] == True:
                price = auc["starting_bid"]
                
                
                
                # gets the pet level then removes "] " after the pet level to account for [Level 1] to [Level 100]
                pet_level = int(re.sub("[^0-9]", "", auc["item_name"]))
                
                # gets current exp
                if pet_level != 100:
                    exp = auc["item_lore"][(auc["item_lore"].find("§l§m §r §e") + 10):-1]
                    exp = exp[0:(exp.find("§6/"))]
                    exp = exp.replace(",", "")
                    try:
                        exp = float(exp)
                    except:
                        continue
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
          
                         
                pet_margins.append([pet_level_to_exp(rarity=auc["tier"].lower(), level=pet_level, exp=exp), price])

        if low_tier_min == float('inf') or max_tier_min == float('inf'):
            print(bcolors.FAIL + "There were no " + pet_name + "s" + bcolors.ENDC)
            
        # getting the line graph info
        plot_m = (max_tier_min - low_tier_min) / (pet_level_to_exp(rarity=rarity, level=100) - pet_level_to_exp(rarity=rarity, level=1))
        plot_b = max_tier_min - plot_m * (pet_level_to_exp(rarity=rarity, level=100))

        margins = []
        for eman in pet_margins:
            if ((eman[0] * plot_m + plot_b) - eman[1] > 700000) and eman[1] < 20000000 and rarity == "LEGENDARY":
                margins.append([pet_name, rarity, eman[1],  (eman[0] * plot_m + plot_b) - eman[1]])
        
        if len(margins) > 0:
            # margins.sort()
            for m in margins:
                all_margin.append(m)
            # print(bcolors.OKCYAN + rarity + " || " + pet_name + bcolors.ENDC)
            # print(margins)

all_margin.sort(key=lambda x: x[3])
for marg in all_margin:
    print(marg)