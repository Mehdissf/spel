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
def Players_item():
    print("Välj en utrustning: ")
    urval = input("1.Rustning \n 2.Svärd")
    if urval == "1":
        HP_bonus = Player_1.HP + 20
        print("Du har tagit rustningen")
        print(f"Ditt HP har nu ökat med +20. Nuvarande HP är: {HP_bonus}")
    if urval == "2":
        STR_bonus = Player_1.STR + 20 
        print("Du har nu valt svärd")
        print(f"Din styrka har nu ökat med +20. Nuvarande styrka är: {STR_bonus}")


class Item():
    def __init__(self,STR_bonus,HP_bonus,K):
        self.STR=STR_bonus
        self.HP=HP_bonus

    def HP_bonus(self):
        print(self.HP)

    def STR_bonus(self):
        print(self.STR)
