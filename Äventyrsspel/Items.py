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

lista =[svärd, spjut, pilbåge, sten]
slumpat_item = random.choice(lista)
def kista():
    kista=["Slangbella","Kannon","Gremlin"]
    kista=random.randint(0,2)

