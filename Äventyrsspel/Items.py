import random
class Item:
  def __init__(self, namn, bonus_strength):
    self.namn = namn
    self.bonus_strength = bonus_strength
  
svärd = Item("Svärd", 10)
spjut = Item("Spjut", 10)
pilbåge = Item("Pilbåge",8)
sten = Item("Sten", 2)


lista =[svärd, spjut, pilbåge, sten]
slumpat_item = random.choice(lista)
