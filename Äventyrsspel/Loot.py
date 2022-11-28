import random
def loot():
    loot = ["trolldryck", "gyllene svärd", "legendariska skölden"]
    lootChnas = random.randint(0,2)
    lootDrop = loot[lootChnas]
    return lootDrop