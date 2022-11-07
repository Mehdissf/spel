import random
import time
def cls():
    print("\n" * 70)   

def dörrar():

    print("""
#######
Välj en av dörrarna nedan för att gå vidare: 
#######
            __________     __________     __________
           |  __  __  |   |  __  __  |   |  __  __  |       
           |  __  __  |   |  __  __  |   |  __  __  |
           | |  ||  | |   | |  ||  | |   | |  ||  | |
           | |  ||  | |   | |  ||  | |   | |  ||  | |
           | |__||__| |   | |  ||  | |   | |  ||  | |
           | __(1)__()|   | __(2)__()|   | __(3)__()|
           | |  ||  | |   | |  ||  | |   | |  ||  | |
           | |  ||  | |   | |  ||  | |   | |  ||  | |
           | |  ||  | |   | |  ||  | |   | |  ||  | |
           | |  ||  | |   | |  ||  | |   | |  ||  | |
           | |__||__| |   | |  ||  | |   | |  ||  | |
           |__________|   |__________|   |__________|

""")

dörrar()
def meny():
    # time.sleep(0.75)  Vi måte fördröja fraserna
    meny_alternativ = ["1", "2", "3"]
    Players_val = ""
    while Players_val not in meny_alternativ:

        cls()
        print('''Hej och välkomna till äventyrsspelet skapat av Mahdi och Elliot!! \n  

    #### Välj ett av de alternativen nedan ####

            1) Starta spelet 
            2) Lämna spelet 
            3) Hjälp
            
            ''')

        
        Players_val = input("\n \n Ange ditt alternativ här: ")
        # print("Du har valt " + Players_val)
        if Players_val =="1":
            startsida_alternativ = ["1", "2"]
            Players_val2 = ""
            while Players_val2 not in startsida_alternativ:  #vi kan också skapa en ny funkttion för startsidan istället för att skriva allt här i alternativ 1)
                cls()
                print("""       
        ########
        Det är nu sommaren år 2030.                                                                            
        Du och din familj för att ha det kul och gå på semester, 
        åker till Borås för att besöka Elliot som har sedan år 2025 varit bosatt i Borås.                              
        Han bor tillsammans med sina tre moderlösa barn. 
        Informantion om vad det är som hänt med barnens mödrar är ett mysterium och ingen har än idag förstått det. 
        Legender säger att Elliot har aldrig haft någon fru.... Men hur fick han de där tre barnen då??? 
        Ingen vet det.. Skitsamma låt oss gå vidare nu..... 
        ######### 

        ####### 
        Välj ett alternativ: 
        #######
            1) Fortsätt 
            2) Tillbaka till meny

                    """)
                Players_val2 = input("\n\n Ange ditt alternativ här: ")
                if Players_val2 == "1":
                    print(dörrar())
                if Players_val2 =="2":
                    meny()

        if Players_val == "3":
            hjälplistan()
        if Players_val == "2":
            cls()
            print("Hej dååå!!")       
            break 
        
meny()














# time.sleep(0,1)------->>> fördröjer fraserna 

# Splearens HP,STR och LVL visas_
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

def loot():
    loot = ["trolldryck", "gyllene svärd", "legendariska skölden"]
    lootChnas = random.randint(0,2)
    lootDrop = loot[lootChnas]
    return lootDrop



# En class för Items
class Item():
    def __init__(self,STR_bonus,HP_bonus,K):
        self.STR=STR_bonus
        self.HP=HP_bonus

    def HP_bonus(self):
        print(self.HP)

    def STR_bonus(self):
        print(self.STR)

# Detta behöver kompeleteras        
    


# Spleren ska kunna ha tillgång till olika utrustningar för att kunna slåss mot monstern
list.item = ["rustning, sköld, svärd"]
print("Du hittar tre vappen i en buske")
item = input("Välj en utrustning: ")




# Monster
# class goblin(object):
#     namn = "Elliot"
#     HP = 10
#     STR = 2
#     DEF = 3