from Items import *
from fälla import *
from monster import *
from Butik import *
import random
import time
import os
import sys
class Player():
    def __init__(self,HP,STR,LVL,pengar):
        self.HP=HP
        self.STR=STR
        self.LVL=LVL
        self.pengar=pengar
        self.inventory = []
    
    def lägg_till_inventoryt(self, item):
        if len(Player_1.inventory) < 5:
            Player_1.inventory.append(item)
            Player_1.STR += item.bonus_strength #vet ej om detta funkar
            print(f"Du fick {item.namn} i din ryggsäck som ger dig +{item.bonus_strength} STR")
                # if item from butik:
                #     Player_1.pengar -= item.pris
                #     print("blablabla")
                #     print(f"{item.namn} kostade {item.pris}$")
                #     time.sleep(0.5)
                #     print(f"{item.namn} lades till din ryggsäck")
                #     input("Tryck [ENTER]")
            input("Aight? [ENTER]")
            os.system('cls')
        else:
            while True:
                print("Din ryggsäck verkar vara full, vill du byta ut en item i din ryggsäck?")
                utbyte = input("(ja/nej ")
                if utbyte.lower() == "ja":
                    for i, b in enumerate(Player_1.inventory):
                        print(f"{i+1}. {b}")
                    val = int(input("Vilket föremål vil du byta ut? (Skriv in nummret)"))
                    Player_1.inventory[val-1] = item
                    print(f"Item {val} utbyttes med {item}")
                    input("Aight? [ENTER]")
                    os.system('cls')
                    return Player_1
                elif utbyte.lower() == "nej":
                    os.system('cls')
                    print("Alright! ")
                    print("You do you!!")
                    break
                else:
                    os.system('cls')
                    print("Ogiltigt val!!!!")
            return Player_1

    def player_egenskaper(self):
        print(f"HP {Player_1.HP}")
        print(f"Styrka {Player_1.STR}")
        print(f"Level {Player_1.LVL}")
        print(f"Dina pengar {Player_1.pengar}$")
        Player.ryggsäck(Player_1)

    def falla(self):
        fälllistan = [Lava, Helvete, Spökhus]
        vald_fälla = random.choice(fälllistan)
        ord = ["Hej", "Teknik", "Elnur", "Johannes"]
        target_ord = random.choice(ord)
        print(f"""
===========================================================================================
Du har hamnat i ''''{vald_fälla.namn}''' nu i Boräs på grund av alla dina oförlåtna synder
===========================================================================================
        """)
        time.sleep(1)
        print (f"Du har 5 sekunder på dig att skriva ordet: \n {target_ord}")
        start_tid = time.time()
        while time.time() - start_tid < 5:
            sekunder_kvar = 5 - (time.time() - start_tid)
            print(f"Sekunder kvar: {sekunder_kvar:.0f}")
            print("SKriv!!!!!!!")
            inp = input()
            if inp == target_ord and time.time() - start_tid <= 5:
                os.system('cls')
                print("Grattis!!!!! du kom undan fällan")
                time.sleep(0.5)
                Player_1.pengar += 300
                print(f"Det tog dig {time.time() - start_tid:.0f} sekunder")
                print("Du får 300$")
                input("Tryck [ENTER]: ")
                os.system('cls')
                return Player_1
                
            elif time.time() - start_tid > 5: 
                if vald_fälla == "Lava": #Här vet jag fan inte vad jag ska göra efter man dör asså
                    os.system('cls')
                    Player_1.HP -= Lava.skada
                    input("Tryck [ENTER]:")
                    os.system('cls')
                    return Player_1
                elif vald_fälla.namn == "Helvete":
                    os.system('cls')
                    print(f"Helvete har gett dig {Helvete.skada} skada")
                    print(f"Ditt HP är nu {Player_1.HP - Helvete.skada}")
                    Player_1.HP -= Helvete.skada
                    input("Tryck [ENTER]: ")
                    os.system('cls')
                    return Player_1
                elif vald_fälla.namn == "Spökhus":
                    os.system('cls')
                    print(f"Spökhus gav dig {Spökhus.skada}")
                    print(f"Ditt HP är nu {Player_1.HP - Spökhus.skada}")
                    Player_1.HP -= Spökhus.skada
                    input("Tryck [ENTER]: ")
                    os.system('cls')
                    return Player_1
                return Player_1
            else: #funkar inmt
                print("Försök igen ")
        if Player_1.HP <= 0:
            print("Spelaren har dött! Spelet är över.")
            sys.exit()
        else:
            return Player_1

    def strid(self, valtt_monster):
        while True:
            Player.player_egenskaper(Player_1)
            Monster.monster_egenskaper(valtt_monster)
            print(valtt_monster)
            print("""
=================================================================
    Vad väljer du?
        1) Slåss
        2) Fly
=================================================================
            """)
            val = input()
            if val == "1":
                if valtt_monster.STR > Player_1.STR:
                    os.system('cls')
                    Player_1.HP -= 10
                    print(f"Du förlorade striden mot {valtt_monster.namn}", f"{Player_1.HP} HP kvar nu")
                    input()
                    os.system('cls')
                    return Player_1

                elif valtt_monster.STR < Player_1.STR:
                    os.system('cls')
                    Player_1.LVL += 1
                    print("Du vann striden mot monstret! Du gick upp ett LVL och är nu LVL", Player_1.LVL)
                    print(valtt_monster.namn + " dog.")
                    input()
                    os.system('cls')
                    return Player_1
                else:
                    os.system('cls')
                    print("Striden resulterar i en oavgjord match.")
                    return Player_1
            elif val == "2":
                os.system('cls')
                break
            elif Player_1.HP <= 0:
                print("Du dog.")
                if Player_1.pengar > 500:
                    betala_fortsätta = input("Vill du betala 500$ för att komma tillbaka till livet?: (ja/nej) ")
                    if betala_fortsätta.lower() == "ja":
                        Player_1.pengar -= 500
                        Player_1.HP += 100
                        return Player_1
                    elif betala_fortsätta.lower() == "nej":
                        sys.exit()
                    else:
                        print("Ogiltigt val.")
                sys.exit()
            else:
                print("Ogiltigt val.")
    
    def kista_scen(self):
        os.system('cls')
        print("Du har hittat en kista!!!")
        input("Fortsätt till kistan?? [ENTER]")
        os.system('cls')
        valt_item_info = {f"namn: {valt_item.namn}", f"STR_bonus: {valt_item.bonus_strength}"}
        Player.lägg_till_inventoryt(valt_item_info, valt_item)

    def ryggsäck (self):
        print("Din ryggsäck: ")
        for i in range(len(Player_1.inventory)):
            print(f"{i + 1}. {Player_1.inventory[i]}")


    
Player_1=Player(100,25,1,100)
ursprungliga_HP = Player_1.HP

