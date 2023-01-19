import random
from monster import*
#Test sida
# from Items import*
# # kista = {"svärd":10, "spjut":10, "Pilbåge":8 ,"sten":2, "Slangbella":3, "Kannon,":5 ,"Gremlin":7}
# # def öppna_kista():
# #   item, bonus_strength = random.choice(list(kista.kista()))
# #   print(f"Du hitta en {item} med strenght bonus av {bonus_strength} ")
# # öppna_kista()

# # items = {"Sword": 2, "Axe": 3, "Spear": 1, "Mace": 4, "Dagger": 0}
# # def open_chest():
# #     item, strength_bonus = random.choice(list(items.items()))
# #     print(f"You found a {item} in the chest! it has strength bonus of {strength_bonus}")

# # open_chest()
# print(random_kista)


# Monster = [
#     {"monster": "Gargamel", "strength": 10},
#     {"monster": "Spjut", "strength_bonus": 10},
#     {"item": "Pilbåge", "strength_bonus": 8},
#     {"item": "Sten", "strength_bonus": 2},
#     {"item": "Slangbella", "strength_bonus": 3},
#     {"item": "Kannon", "strength_bonus": 5},
#     {"item": "Gremlin", "strength_bonus": 7}


# ]
# random_kista = random.choice(kista)
# print("You found a chest containing a " + random_kista["item"] + " with a strength bonus of " + str(random_kista["strength_bonus"]))


# class Monster:
#     def __init__(self):
#         self.name = ""
#         self.description = ""

#     def generate_monster(self):
#         monster_types = ["Dragon", "Goblin", "Troll", "Zombie", "Skeleton"]
#         monster_descriptions = ["a large and fierce", "a small and sneaky", "a towering and intimidating", "a rotting and reanimated", "a bony and undead"]
#         self.name = random.choice(monster_types)
#         self.description = random.choice(monster_descriptions)
        
#     def __str__(self):
#         return self.description + " " + self.name

# class Door:
#     def __init__(self):
#         self.monster = Monster()
        
#     def open(self):
#         self.monster.generate_monster()
#         print("You open the door and a " + str(self.monster) + " appears!")

# door = Door()
# door.open()


# lista =[Elliot, Hitler, Gargamel]
# valtt_monster = random.choice(lista)


class Monster:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.hp = 0
        self.damage = 0
        
    def generate_monster(self):
        monster_types = ["Dragon", "Goblin", "Troll", "Zombie", "Skeleton"]
        monster_descriptions = ["a large and fierce", "a small and sneaky", "a towering and intimidating", "a rotting and reanimated", "a bony and undead"]
        self.name = random.choice(monster_types)
        self.description = random.choice(monster_descriptions)
        self.hp = random.randint(50,100)
        self.damage = random.randint(10,20)

    def __str__(self):
        return self.description + " " + self.name

monster = Monster()
monster.generate_monster()
print(monster)
print("HP: " + str(monster.hp))
print("Damage: " + str(monster.damage)) 

class Monster():
    def __init__(self,namn,HP,STR,figur):
        self.namn=namn
        self.HP=HP
        self.STR=STR
        self.figur =figur

Elliot= Monster("Elliot", 100, 50, Elliot_figur )
Hitler= Monster("Hitler", 90, 30, Hitler_figur )
Gargamel= Monster("Gargamel", 60, 35, Gargamel_figur )
def monster_egenskaper(self):
        print(f"Du har stött på monstret {valtt_monster.namn}, han är en farlig varelse och här nedan ser du hans status")
        print(f"""{valtt_monster.figur}""") #ser knasigt ut
        print(f'Monstrets namn {valtt_monster.namn}')        
        print(f'Styrka {valtt_monster.STR}')
        print(f'HP {valtt_monster.HP}')



lista =[Elliot, Hitler, Gargamel]
valtt_monster = random.choice(lista)
# def genereara_monster():
#     lista =[Elliot, Hitler, Gargamel]
# monster.generate_monster()
# print(monster)
# print(Monster.HP)
# print(Monster.STR)





