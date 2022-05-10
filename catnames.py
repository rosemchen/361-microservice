# Microservice for Dawn's Cat Avatar Project
# Reads "run" from catnames.json
# Prints out object with 10 random cat names

import random
import time
from collections import defaultdict
import json


catlist = ["muffins", "cupcake", "flour", "sugar", "pepper",
             "chocolate", "oatmeal", "cereal", "puffs", "cookie",
           "brownie", "cannoli", "hershey", "butterscotch", "licorice", "maple", "honey", "mochi", "mousse", "nutmeg", "cinnamon", "smores", "shortcake", "butters", "waffle", "pancake", "toffee", "pumpkin", "marshmallow"]

random.seed()
while True:
    time.sleep(1)
    readcatnames = open('catnames.json', 'r')
    entry = readcatnames.readline()
    readcatnames.close()
    if entry == 'run':
        writecatnames = open('catnames.json', 'w')
        randomNames = random.choices(catlist, k=10)
        target = {39: None, 91: None, 93: None}
        catnamedict = defaultdict(list)
        for names in randomNames:
            catnamedict["names"].append(names)
        #print(catnamedict)
        #writecatnames.write(format(catnamedict))
        #writecatnames.write(json.dumps(catnamedict))
        #print(json.dumps(catnamedict))
        writecatnames.write(json.dumps(catnamedict))
writecatnames.close()
