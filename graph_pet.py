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
            