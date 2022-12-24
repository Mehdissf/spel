import random
import time
import os
# from Items import *
# from Loot import *
from Butik import *
from Player import *
from monster import *
from fälla import *
from Player import *
os.system('cls')

#Mehdi : jag är inte helt klar med detta vi får jobba på det senare
   #Spelaren ska hinna med att skriva någonting väldigt fort för att kunna överleva från fällan ------>>
    #splearen dör/förlorar HP beroende av vilken typ av fälla
    #Fälllor ska slumpvis lottas ut vid varje gång 
def falla_scen(Player_1):
    os.system('cls')
    fälllistan = [Lava, Helvete, Spökhus]
    vald_fälla = random.choice(fälllistan)
    ord = ["Hej", "Teknik", "Elnur", "Mehdi"]
    target_ord = random.choice(ord)
    print(f"""
============================================================================
Du har hamnat i ''''{vald_fälla.namn}''' nu i Boräs på grund av alla dina oförlåtna synder
============================================================================
    """)
    print(f"Du har 5 sekunder på dig att skriva ordet: \n {target_ord}" )
    start_tid = time.time()
    while time.time() - start_tid < 5:
        sekunder_kvar = 5 - (time.time() - start_tid)
        print(f"Du har {sekunder_kvar:.0f} sekunder kvar")
        inp = input("Skriv här: ")
        if inp == target_ord and time.time() - start_tid <= 5:
            os.system('cls')
            print("Grattis!!!!! du kom undan fällan")
            time.sleep(0.5)
            Player_1.pengar += 300
            print(f"Det tog dig {time.time() - start_tid:.0f} sekunder")
            print("Du får 300$")
            input("Tryck [ENTER]: ")
            return Player_1
        elif time.time() - start_tid > 5: 
            if vald_fälla == "Lava": #Här vet jag fan inte vad jag ska göra efter man dör asså
                print("Vila i frid!!")
                time.sleep(0.5)
                print("Ingen har lyckats med att hitta din lik, den är förmodligen smält och har omvandlat sig till rök")
                Player_1.HP -= Lava.skada
                input("Tryck [ENTER]:")
                break
            elif vald_fälla.namn == "Helvete":
                print(f"Helvete har gett dig {Helvete.skada} skada")
                print(f"Ditt HP är nu {Player_1.HP - Helvete.skada}")
                Player_1.HP -= Helvete.skada
                input("Tryck [ENTER]: ")
                break
            elif vald_fälla.namn == "Spökhus":
                print(f"Spökhus gav dig {Spökhus.skada}")
                print(f"Ditt HP är nu {Player_1.HP - Spökhus.skada}")
                Player_1.HP -= Spökhus.skada
                input("Tryck [ENTER]: ")
                break
            return Player_1
        else: 
            print("Försök igen ")        
    return Player_1
    
def monster_scen(Player_1):
    os.system('cls')
    while True: 
        print(f"Du har stött på monstret {valt_monster.namn}, han är en farlig varelse och här nedan ser du hans status")
        print(f"""{valt_monster.figur}""")
        print(f'Monstrets namn {valt_monster.namn}')        
        print(f'Styrka {valt_monster.STR}')
        print(f'HP {valt_monster.HP}') 
        print("""
=================================================================
    Vad väljer du?
    1) Fortsätt
    2) Fly
=================================================================
        """)
        monster_val= input()
        if monster_val=="1":
            while Player_1.HP != 0:
                print("EHJ")

        elif monster_val== "2":
            break
        else:
            os.system('cls')
            print("Välj mellan 1 eller 2")
        return Player_1
#Monster scen är oklar
def kista_scen():


    os.system('cls')
    print("""
=======================================    
Du har hittat en kista!!
Tryck [Enter] för att fortsätta till kistan!
=======================================
    """)
    input("Skriv") #tillfällig kod
def dörrar(Player_1):
    
    while True:
        os.system('cls')
        print("""




|============================================|
|Välj en av dörrarna nedan för att gå vidare:|
|============================================|
     __________     __________     __________
    |  __  __  |   |  __  __  |   |  __  __  |       
    |  __  __  |   |  __  __  |   |  __  __  |       
    | |  ||  | |   | |  ||  | |   | |  ||  | |          
    | |  ||  | |   | |  ||  | |   | |  ||  | |        
    | |__||__| |   | |  ||  | |   | |  ||  | |
    |  __  __()|   |  __  ()  |   |  __  __()|
    | |  ||  | |   | |  ||  | |   | |  ||  | |
    | |  ||  | |   | |  ||  | |   | |  ||  | |
    | |  ||  | |   | |  ||  | |   | |  ||  | |
    | |  ||  | |   | |  ||  | |   | |  ||  | |
    | |__||__| |   | |  ||  | |   | |  ||  | |
    |__________|   |__________|   |__________|
    (1)            (2)            (3)
""")
        print("""
|================================================================================ |
| OBS! Det kan antingen finnas ett monster/ en fälla eller en kista bakom dörrarna|
|                                                                                 |
| Tillbaka till förra sidan [b]          Status [s]                               |
|================================================================================ |
        """)
        val = input("Ditt val: ")
        if val == "b":
            os.system('cls')
            print("hej")
            return Player_1

        elif val == "s":
            os.system('cls')
            print(f"HP {Player_1.HP}")
            print(f"Styrka {Player_1.STR}")
            print(f"Level {Player_1.LVL}")
            print(f"Dina pengar {Player_1.pengar}$")
            input("okej? [Tryck enter].")
        elif val == "1":
            os.system('cls')
            falla_scen(Player_1)
        elif val =="2":
            os.system('cls')
            monster_scen(Player_1)
        elif val =="3":
            os.system('cls')
            kista_scen()
        else:
            os.system('cls')
            print("Välj rätt värde '1', '2, '3' eller 'b'") #Funkar inte       
def start(Player_1):
                while True:  
                    os.system('cls')
                    print("""       
==========================================================================================
    Det är nu sommaren år 2050.                                                                            
    Du och din familj för att ha det kul, går på semester.
    Ni åker till Borås för att besöka Elliot som har sedan år 2030 varit bosatt där.                              
    Han bor tillsammans med sina tre moderlösa barn. 
    Informantion om vad det är som hänt med barnens mödrar är ett mysterium och ingen har än idag fått reda på det. 
    Legender säger att Elliot har aldrig haft någon fru.... Men hur fick han de där tre barnen då??? 
    Ingen vet det.. Skitsamma låt oss gå vidare nu..... 
============================================================================================= 

===================== 
    Välj ett alternativ: 
=====================
    1) Fortsätt 
    2) Tillbaka till meny
    3) Se din profil
    4) Butik
            """)
                    Players_val2 = input("\n\n Ditt val: ")
                    if Players_val2 == "1":
                        os.system('cls')
                        Player_1 = dörrar(Player_1)
                        print(Players_val2)
                        continue

                    elif Players_val2 == "2":
                        os.system('cls')
                        return
                    elif Players_val2 == "3":
                        os.system('cls')
                        print(f"HP {Player_1.HP}")
                        print(f"Styrka {Player_1.STR}")
                        print(f"Level {Player_1.LVL}")
                        print(f"Dina pengar {Player_1.pengar}$")
                        input("okej? [Tryck enter].")
                        os.system('cls')
                        
                    elif Players_val2 == "4":
                        os.system('cls')
                        Player_1 = butik(Player_1)
                        continue
                               
                    else: 
                        os.system('cls')
                        print("Skriv rätt siffra 1, 2 eller 3")  #Funkar inte 
                    
                    
def main():
    Player_1=Player(100,20,1,100)
    while True:
        Players_val = ""
        print('''
==================================================================     
 Hej och välkomna till äventyrsspelet skapat av Mahdi och Elliot------>>>> 
===================================================================
==========================================
    Välj ett av de alternativen nedan för att gå vidare
==========================================

            1) Starta spelet 
            2) Lämna spelet 
        
            ''')
 
        Players_val = input("\n Ange ditt alternativ här: ")
        if Players_val =="1":    #Här kallas på def star()
                os.system('cls')
                Player_1 = start(Player_1)
      
        elif Players_val == "2":    #Spelet avslutas 
                os.system('cls')
                print("""
|================|
|   Hej dååå!!   |
|================|
                """)
                break
        else:
            os.system('cls')
            print("""


================================================================================================================
    OBS!!!! 
    Du får endast skriva in siffrorna "1", "2", "3" 
    för att gå vidare 
    Så skriv in rätt nu tack 
================================================================================================================
                """)

main() 


