# Microservice for Dawn's Cat Avatar Project
# Reads "run" from catnames.json
# Prints out object with 10 random cat names

import random
import time

from Tools.scripts.make_ctype import values

catlist = { 'names' : ["muffins", "cupcake", "flour", "sugar", "pepper",
             "chocolate", "oatmeal", "cereal", "puffs", "cookie",
           "brownie", "cannoli", "hershey", "butterscotch", "licorice",
                   "maple", "honey", "mochi", "mousse", "nutmeg", "cinnamon", "smores", "shortcake", "butters", "waffle", "pancake", "toffee", "pumpkin", "marshmallow"]}

print(type(catlist))

#keys = catlist.values()
#random.shuffle(values)
#for names in keys:
#    print(names, catlist[values])

new_catlist = list()