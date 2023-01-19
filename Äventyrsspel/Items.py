import random
# class Item:
#   def __init__(self, namn, bonus_strength):
#     self.namn = namn
#     self.bonus_strength = bonus_strength  
# svärd = Item("Svärd", 10)
# spjut = Item("Spjut", 10)
# pilbåge = Item("Pilbåge",8)
# sten = Item("Sten", 2)
# Slangbella=Item("Slangbella",3)
# Kannon=Item("Kannon",5)
# Gremlin=Item("Gremlin",7)

# kista = [svärd, spjut, pilbåge, sten, Slangbella, Kannon, Gremlin]
# def öppna_kista():
#   valt_item = random.choice(kista)

kista = [
    {"item": "Svärd", "strength_bonus": 10},
    {"item": "Spjut", "strength_bonus": 10},
    {"item": "Pilbåge", "strength_bonus": 8},
    {"item": "Sten", "strength_bonus": 2},
    {"item": "Slangbella", "strength_bonus": 3},
    {"item": "Kannon", "strength_bonus": 5},
    {"item": "Gremlin", "strength_bonus": 7}


]
random_kista2 = random.choice(kista)
random_kista3 = random.choice(kista)
random_kista4 = random.choice(kista)
random_kista5 = random.choice(kista)
random_kista = random.choice(kista)
print("You found a chest containing a " + random_kista["item"] + " with a strength bonus of " + str(random_kista["strength_bonus"]))




kista = [svärd, spjut, pilbåge, sten, Slangbella, Kannon, Gremlin]
valt_item = random.choice(kista)