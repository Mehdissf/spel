import random
class Item:
  def __init__(self, namn, bonus_strength):
    self.namn = namn
    self.bonus_strength = bonus_strength
  
svärd = Item("Svärd", 10)
spjut = Item("Spjut", 10)
pilbåge = Item("Pilbåge",8)
sten = Item("Sten", 2)
Slangbella=Item("Slangbella",3)
Kannon=Item("Kannon",5)
Gremlin=Item("Gremlin",7)

kista = [svärd, spjut, pilbåge, sten, Slangbella, Kannon, Gremlin]
def öppna_kista():
  valt_item = random.choice(kista)



#Alternativ på lösning av slumpade items, funkar dock inte än
# kista = {"svärd":10, "spjut":10, "Pilbåge":8 ,"sten":2, "Slangbella":3, "Kannon,":5 ,"Gremlin":7}
# def öppna_kista():
#   item, bonus_strength = random.choice(list(kista.kista()))
#   print(f"Du hitta en {item} med strenght bonus av {bonus_strength} ")
# öppna_kista()

# items = {"Sword": 2, "Axe": 3, "Spear": 1, "Mace": 4, "Dagger": 0}
# def open_chest():
#     item, strength_bonus = random.choice(list(items.items()))
#     print(f"You found a {item} in the chest! it has strength bonus of {strength_bonus}")

# open_chest()
