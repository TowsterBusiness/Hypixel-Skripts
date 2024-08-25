import requests as req
import json
from colors import bcolors
from threading import Thread
from time import sleep

# Variables used in the porgram
url = "https://api.hypixel.net/skyblock/auctions"
pageNum = req.get(url).json()["totalPages"]
pages_completed = 0
pet_auction_list = []
auction_list = []
    
def add_auction(pN):
    global auction_list
    global url
    global pages_completed
    global pageNum
    global pet_list
    global pet_auction_list
    
   
    result = req.get(url + '?page=' + str(pN)).json()
    
    for auc in result["auctions"]:
        if auc["bin"]:
            auction_list.append(auc)
            if (auc["item_name"][auc["item_name"].find("]") + 2:] in pet_list):
                pet_auction_list.append(auc)
        
    pages_completed += 1
    # Checks if all pages were checked
    if (pages_completed >= pageNum):
        # Writes to the cache.json file with the full auctions list
        dic = {
            "auctions": auction_list
        } 

        json_object = json.dumps(dic, indent=4)
        
        with open("cache/cache.json", "w") as outfile:
            outfile.write(json_object)
            
        # Writes to the pet_chache.json with only the pet auctions list
        dic = {
            "auctions": pet_auction_list
        } 
