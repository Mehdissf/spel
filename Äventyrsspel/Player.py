class Player():
    def __init__(self,HP,STR,LVL,DEF):
        self.HP=HP
        self.STR=STR
        self.LVL=LVL
        # self.DEF=DEF

Player_1=Player(100,20,0,10)
print(f"HP {Player_1.HP}")
print(f"Styrka {Player_1.STR}")
print(f"Level {Player_1.LVL}")