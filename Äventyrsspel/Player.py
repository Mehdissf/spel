from Items import *
class Player():
    def __init__(self,HP,STR,LVL,pengar):
        
        self.HP=HP
        self.STR=STR
        self.LVL=LVL
        self.pengar=pengar
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
    
    def get_total_STR(self):
        total_STR = self.strength
        for item in self.inventory:
            total_STR += item.bonus_strength
        return total_STR

Player_1=Player(100,20,1,100)
ursprungliga_HP = Player_1.HP

