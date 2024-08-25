import requests as req
import json
from colors import bcolors



url = "https://api.hypixel.net/skyblock/auctions"

with open('cache/pet_list.json', 'r') as openfile:
    pet_list = json.load(openfile)["pet_list"]

pageNum = req.get(url).json()["totalPages"]
print(bcolors.HEADER + "Chaching " + str(pageNum) + bcolors.ENDC)

auction_list = []
pet_auction_list = []

for i in range(pageNum):
    print("Page Number: " + str(i))
    result = req.get(url + '?page=' + str(i)).json()
    
    for auc in result["auctions"]:
        auction_list.append(auc)
        if (auc["item_name"][auc["item_name"].find("]") + 2:] in pet_list):
            pet_auction_list.append(auc)
        
dic = {
    "auctions": auction_list
} 

json_object = json.dumps(dic, indent=4)
with open("cache/cache.json", "w") as outfile:
    outfile.write(json_object)
    
dic = {
    "auctions": pet_auction_list
} 

json_object = json.dumps(dic, indent=4)
with open("cache/pet_cache.json", "w") as outfile:
    outfile.write(json_object)