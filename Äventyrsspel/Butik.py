from Player import *
import os 
import time
from Player import Player_1

class Butik_items:
  def __init__(self, namn, bonus_strength, bonus_hp):
    self.namn = namn
    self.bonus_strength = bonus_strength
    self.bonus_hp = bonus_hp
  def __str__(self):
    return f"{self.namn} med styrka {self.bonus_strength}"


#Plåstern lägg inte till ryggsäcken utan Player_1 får bonus_hp direkt efter köpet
  def köp_plåster(self):
    köp_plåster = input(""" 
            
  /==========================1
 / : : : : : |::::| : : : : : 1          |===============|
{ : : : : : :|::::|: : : : : : }         |Namn = plåster |
 \ : : : : : |::::| : : : : : /          |Pris = 20$     |
   ==========================/           |HP_bonus = +10 |
===============================          |===============|
            Vill du köpa?
            1) Köp
            2) Tillbaka
===============================            

                    """)
    while True:
        if köp_plåster == "1":
            if Player_1.pengar < 20:
                os.system('cls')
                print("Du har för lågt saldo!!")
                return Player_1
            else:
                if Player_1.HP >= ursprungliga_HP:
                    os.system('cls')
                    print(f"Ditt HP är max {ursprungliga_HP} du kan inte köpa")
                    input("Tryck [ENTER]")
                    break
                else:
                    os.system('cls')
                    Player_1.pengar -= 20
                    print("Plåstern kostade 20$")
                    print("Du har en plåster nu i din ryggsäck")
                    time.sleep(0.5)
                    Player_1.HP += 10
                    print(f"Du har {Player_1.HP} HP nu")
                    time.sleep(0.5)
                    print(f"Pengar kvar: {Player_1.pengar}")
                    input("Tryck [ENTER]")
                    break
        elif köp_plåster == "2":
            break
        else:
            os.system('cls')
            print("Skriv rätt!!")
    return Player_1
  
  def yxa(self):
    os.system('cls')
    köp_yxa = input("""                             
    /\ 
//`-||-'1)
(|-=||=- |)                          
\L,-||-.//                           |==================|
 \L ||-//                            |Namn =  Yxa       |
    ||                               |Pris = 200$       |
    ||                               |Strength_bonus = 5|
    ||                               |==================|
    ||  
    ||   
    ||
    ()
============================= 
        Vill du köpa?
        1) Köp
        2) Tillbaka
=============================        
            """)
    while True:
        if köp_yxa == "1":
            if Player_1.pengar < 200:
                os.system('cls')
                print("Du har för lågt saldo!!. Du kan inte köpa yxan")
                input("Okej? [ENTER]")
                return Player_1
            else:
                os.system('cls')
                # Player_1.pengar -= 200
                # man betalar ändå om man inte köper der haha
                yxa_info = {"namn":"Yxa", "strength_bonus":5}
                Player.lägg_till_inventoryt(yxa_info, Yxa)
                return Player_1
        elif köp_yxa == "2":
            break
        else:
            köp_yxa = input("Ogiltigt svar, skriv rätt : ")
    return Player_1
  
  def butik(self):
        Alternativ = ["1","2","3","4"]
        val_shelf = ""
        while val_shelf not in Alternativ:
            os.system('cls')
            print(f"Ditt saldo är {Player_1.pengar}$")
            print("""
===================================================
    Välkommnen till Jamal och brödernas butik!
====================================================
====================================================
    Här finnns olika hyllor vilken väljer du? 
====================================================
        1) yxor              3) Tillbaka 
        2) Medicin     
        """)
            val_shelf = input("\n Vad väljer du? ")
            if val_shelf == "1":
                os.system('cls')
                Butik_items.yxa(Player_1)

            elif val_shelf == "2":
                os.system('cls')
                Butik_items.köp_plåster(Player_1)

            elif val_shelf == "3":
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Välj rätt siffta")
            val_shelf = ""



Plåster = Butik_items("Plåster", None, 10)
Yxa = Butik_items("Yxa", 3, None)


    



