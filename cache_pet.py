import json
import re

pet_list = []

with open('cache/cache.json', 'r') as openfile:
    auc_list = json.load(openfile)["auctions"]

for auc in auc_list:
    if re.search(r'(§8[A-z]* Pet)', auc["item_lore"]):
        pet_name = auc["item_name"]
        pet_name = re.sub(r'\[Lvl [0-9]*\] ', '', pet_name)
        pet_name = pet_name.replace(' ✦', '')
        print(pet_name)
        if (not (pet_name in pet_list)):
            print("==")
            pet_list.append(pet_name)
            
            
print(pet_list)

dic = {
    "pet_list": pet_list
} 

json_object = json.dumps(dic, indent=4)
with open("cache/pet_list.json", "w") as outfile:
    outfile.write(json_object)