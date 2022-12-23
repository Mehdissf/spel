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
def fälla_scen(Player_1):
    os.system('cls')
    fälllistan = [Lava, Helvete,Spökhus]
    vald_fälla = random.choice(fälllistan)
    print(f"""
============================================================================
Du har hamnat i {vald_fälla.namn} nu i Boräs på grund av alla dina oförlåtna synder
============================================================================
    """)
    limittid = 5
    starttid = time.time()
    sluttid = time.time()
    LVL1_ord = ["Hej", "Teknik", "Elnur", "Mehdi"]
    ord = random.choice(LVL1_ord)
    elapsed_tid = sluttid - starttid
    if vald_fälla.namn == "Lava":
        print("Du har hamnat i lava nu om du inte lyckas komma undan den så dör du!!! Följ instruktionerna tydligt")
        print("För att komma undan denna fällan måste du skriva så snabbt som möjligt det ordet som dykes upp nu")
        print(f"Du har 5 sekunder på dig att skriva ordet: \n {ord}")
        time.sleep(1)    
        user_input = input("Skriv ordet nu: ")
        if user_input == ord and elapsed_tid <= limittid:
            print("Grattis!! Du kom undan lavan")
            Player_1.pengar += 300
            print("Du fick 300$")
            return Player_1
        else:
            print("Du misslyckades att komma undan fällan, du dog nu")
            Player_1.HP -= Lava.skada
            return Player_1
            
    return Player_1


       

        # while time.time() - starttid > 3:
        #     print(f"Tiden är ute nu du förlorade{vald_fälla.namn}")
        #     print(f"Ditt HP nu är {Player_1.HP - vald_fälla.skada}")
        #     if Player_1.HP == 0 or Player_1.HP < 0:
        #             print("Vila i frid min broder, du dog!!!")
        #             inp = input("Tryck [Enter]")
        #             if inp == "":
        #                 start()
                    
                    
        #             #Här ska splearen kunna ha möjligheten att komma tillbaka till startsidan
        #     starttid = time.time()
        # else:
        #     print("Bra jobbat!! Du kom undan fällan")
        #     print("Varsågod!! Du får 20$ pris")  #Här behövs det att 20$ ska läggas till de pengar spelaren har :)

def monster_scen(Player_1):
    os.system('cls')
    while True: 
        print("""
=================================================================
    Du hittade nu ett mörkt läskigt rum med ett fasansfullt monster
    Vad väljer du?
    1) Slåss
    2) Fly
=================================================================
        """)
        monster_val= input("Ditt val: ")
        if monster_val=="1":
            print(f"Opsiii du har stött på monstret {valt_monster.namn}, han är en farlig varelse och här nedan ser du hans status")
            print(f'Monstret heter {valt_monster.namn}')        
            print(f'Styrka {valt_monster.STR}')
            print(f'HP {valt_monster.HP}') 

            if valt_monster.HP>0:
                valt_monster.HP -= Player_1.STR
                print(f'{valt_monster.namn} har HP {valt_monster.HP}')
            elif valt_monster.HP <= 0:
                print('Du vann')
                Player_1.pengar= Player_1.pengar + 50
                Player_1.LVL=Player_1.LVL + 1
        elif monster_val== "2":
            return Player_1
        else:
            os.system('cls')
            print("Välj mellan 1 eller 2")
        return Player_1

def kista_scen():

    os.system('cls')
    print("""
=======================================    
Du har hittat en kista!!
Tryck [Enter] för att fortsätta till kistan!
=======================================
    """)
    input("Skriv") #tillfällig kod

#En utgång till dörr funktionen behövs så spelaren kan backa till start funktionen
#Jag (Mehdi) har försökt lösa det men lcykades inte vi får fixa det senare
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
            fälla_scen()
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


