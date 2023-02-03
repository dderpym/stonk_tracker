import json
from time import ctime

dictionary = {}

with open("results.json", "r") as infile:
    dictionary = json.load(infile)
    infile.close()

def process(price, init_price):
    return str(price) + " (" + str(price/init_price * 100 - 100) + "%)"

timeline = dictionary["timeline"]
init_price = dictionary["init_price"]
init_dji = dictionary["init_dji"]
latest_price = dictionary["latest_price"]
latest_dji = dictionary["latest_dji"]

for time in timeline:
    vals = timeline[time]
    print("at " + ctime(float(time)) + " => MRK: " + process(vals["price"], init_price) + " ||| DJI: " + process(vals["dowjones"], latest_dji))

print("In aggregate, MRK is at " + process(dictionary["latest_price"], dictionary["init_price"]) + ", compared to Dow Jones " + process(dictionary["latest_dji"], dictionary["init_dji"]))
print("Earnings: $" + str(dictionary["latest_price"] * dictionary["quantity"] - dictionary["money_spent"]))
