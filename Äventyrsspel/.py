import random

items = {"Sword": 2, "Axe": 3, "Spear": 1, "Mace": 4, "Dagger": 0}

def open_chest():
    item, strength_bonus = random.choice(list(items.items()))
    print(f"You found a {item} in the chest! it has strength bonus of {strength_bonus}")

open_chest()