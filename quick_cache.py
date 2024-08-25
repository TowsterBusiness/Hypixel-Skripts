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