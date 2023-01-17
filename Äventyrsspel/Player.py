from Items import *
from fälla import *
from monster import *
from Butik import *
import itertools
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
        self.inventory = [0,4]

    def lägg_till_inventoryt(self, item):
        self.inventory.append(item)
    
    def ryggsäck(self):           
        
        if len(Player_1.inventory) == 5:
            print("")
        elif len(Player_1.inventory) >5:
            print("Du fick ett till vapen")
    
    def total_STR(self):
        total_STR = self.strength
        for item in self.inventory:
            total_STR += item.bonus_strength
        return total_STR

    def player_egenskaper(self):
        print(f"HP {Player_1.HP}")
        print(f"Styrka {Player_1.STR}")
        print(f"Level {Player_1.LVL}")
        print(f"Dina pengar {Player_1.pengar}$")
      
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

    def strid(self):
        while True:
            lista =[Elliot, Hitler, Gargamel]
            # valtt_monster = random.choice(lista)
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
                    print("Monstret var starkare därför förlorade du. Du har nu", Player_1.HP, "HP kvar.")
                    return Player_1

                elif valtt_monster.STR < Player_1.STR:
                    os.system('cls')
                    Player_1.LVL += 1
                    print("Du vann striden mot monstret! Du gick upp ett LVL och är nu LVL", Player_1.LVL)
                    print(valtt_monster.namn, "är död.")
                    time.sleep(0.5)
                    print("Du fick följande items av monstret!")
                    # item = slumpat_item.namn
                    # Player_1.lägg_till_inventoryt(item)
                    # Player_1.STR += slumpat_item.bonus_strength
                    #Player ska få loot
                    #Är inte säker på hur exakt detta kommer att funka
                    return Player_1
                else:
                    os.system('cls')
                    print("Striden resulterar i en oavgjord match.")
                    return Player_1

            elif val == "2":
                os.system('cls')
                break
            #vet inte hur jag ska avsluta spelet om spelarens HP går mot 0
            elif  Player_1.HP <= 0:
                print("Du har dött.")
                if  Player_1.pengar > 500:
                    Vill_du_betala_för_att_köra_igen = input("Betla 500$ för att fortsätta spela: \n Ja/Nej: ")
                    if Vill_du_betala_för_att_köra_igen == "Ja":
                        Player_1.pengar -= 500
                        Player_1.HP += 100
                        return Player_1
                    elif Vill_du_betala_för_att_köra_igen == "Nej":
                        sys.exit()
                    else:
                        print("Fel! skriv rätt!!")
                sys.exit()       
            else:
                os.system('cls')
                print("Ogiltigt val! Skriv rätt")
        return Player_1
    
    def kista_scen(self):
        os.system('cls')
        print("""
    =======================================    
    Du har hittat en kista!!
    Tryck på (Enter) för att öppna
    =======================================
        """)
        input()
        os.system('cls')
        random_kista = random.choice(kista)
        print("Du har hittat en/ett " + random_kista["item"] + "med strength_bonus  " + str(random_kista["strength_bonus"]))
        # if len(Player_1.inventory) >5:
        #     os.system('cls')
        #     print("Grattis du fick ett nytt vapen")
        # elif len(Player_1.inventory) == 5:
        #  val=input()
        #  print("Vill du byta ut vapnet? a)Jo men absolut b)Nej skit på dig")
        #  if val =="a":
        #     os.system('cls')
        # elif val =="b":
        #     os.system('cls')
        return Player_1
        
        



        return Player_1
    




Player_1=Player(100,20,1,100)
ursprungliga_HP = Player_1.HP

