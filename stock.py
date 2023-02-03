from numpy import trunc
from yahoo_fin.stock_info import get_live_price
import time
import json

dictionary = {}

with open("results.json", "r") as infile:
    dictionary = json.load(infile)
    infile.close()

price = get_live_price(dictionary["stock_name"])
dji = get_live_price('^dji')

if not dictionary["initialized"]:
    # get quantity
    dictionary["quantity"] = trunc(dictionary["init_money"]/price)
    dictionary["money_spent"] = dictionary["quantity"] * price

    dictionary["initialized"] = True
    dictionary["init_price"] = price 
    dictionary["init_dji"] = dji
else:
    dictionary["latest_price"] = price 
    dictionary["latest_dji"] = dji

timeline = dictionary["timeline"]
timeline[time.time()] = {"dowjones": dji, "price": price}

json_object = json.dumps(dictionary, indent=4)

with open("results.json", "w") as outfile:
    outfile.write(json_object)
    outfile.close()
