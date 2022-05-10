import random
from collections import defaultdict

catlist = ["muffins", "cupcake", "flour", "sugar", "pepper",
             "chocolate", "oatmeal", "cereal", "puffs", "cookie", "brownie", "cannoli", "hershey", "butterscotch", "licorice", "maple", "honey", "mochi", "mousse", "nutmeg", "cinnamon", "smores", "shortcake", "butters", "waffle", "pancake", "toffee", "pumpkin", "marshmallow"]


randomNames = random.choices(catlist, k=10)
target = {39: None, 91: None, 93: None}
#randomNamesCleaned = (str(randomNames).translate(target))
#randomNamesCleaned = randomNamesCleaned.replace(',', '')
#print(randomNamesCleaned)



d = defaultdict(list)
for i in randomNames:
    d["names"].append(i)
print(d)