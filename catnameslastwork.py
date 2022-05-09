# Microservice for Dawn's Cat Avatar Project
# Reads "run" from catnames.json
# Prints out object with 10 random cat names

import random
import time


catlist = ["muffins", "cupcake", "flour", "sugar", "pepper",
             "chocolate", "oatmeal", "cereal", "puffs", "cookie", "brownie", "cannoli", "hershey", "butterscotch", "licorice", "maple", "honey", "mochi", "mousse", "nutmeg", "cinnamon", "smores", "shortcake", "butters", "waffle", "pancake", "toffee", "pumpkin", "marshmallow"]

random.seed()
while True:
    time.sleep(3)
    readcatnames = open('catnames.json', 'r')
    entry = readcatnames.readline()
    readcatnames.close()
    if entry == 'run':
        break

writecatnames = open('catnames.json', 'w')
if entry == 'run':
    randomNames = random.choices(catlist, k = 10)
    target = {39: None, 91: None, 93: None}
    randomNamesCleaned = (str(randomNames).translate(target))
    randomNamesCleaned = randomNamesCleaned.replace(',','')
    writecatnames.write(format(randomNamesCleaned))
writecatnames.close()

