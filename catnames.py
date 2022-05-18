# Microservice for Dawn's Cat Avatar Project
# Reads "run" from catnames.json
# Prints out object with 10 random cat names

import random
from collections import defaultdict
import json


catlist = ["muffins", "cupcake", "flour", "sugar", "pepper",
             "chocolate", "oatmeal", "cereal", "puffs", "cookie",
           "brownie", "cannoli", "hershey", "butterscotch", "licorice",
           "maple", "honey", "mochi", "mousse", "nutmeg", "cinnamon",
           "smores", "shortcake", "butters", "waffle", "pancake",
           "toffee", "pumpkin", "marshmallow", "bacon", "eggs",
           "pancake", "oreo", "chip", "mittens", "buttercup", "ginger",
           "apple", "tuna", "popcorn"]

random.seed()
writecatnames = open('catnames.json', 'w')
randomNames = random.choices(catlist, k=10)
target = {39: None, 91: None, 93: None}
catnamedict = defaultdict(list)
for names in randomNames:
    catnamedict["names"].append(names)
writecatnames.write(json.dumps(catnamedict))
writecatnames.close()
exit()
