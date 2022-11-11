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




# Spleren ska kunna ha tillgång till olika utrustningar för att kunna slåss mot monstern
list.item = ["rustning, sköld, svärd"]
print("Du hittar tre vappen i en buske")
item = input("Välj en utrustning: ")