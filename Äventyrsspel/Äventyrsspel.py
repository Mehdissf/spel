import os
from Butik import *
from Player import *
from monster import *
from fälla import *
os.system('cls')
def dörrar(Player_1):
    while True:
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
| Tillbaka till förra sidan [b]          Status [s]        Inventory(i)           |
|================================================================================ |
        """)
        val = input()
        if val == "b":
            os.system('cls')
            print("hej")
            return Player_1
        elif val == "s":
            os.system('cls')
            Player.player_egenskaper(Player_1)
            input("okej? [Tryck enter].")
            os.system('cls')
        elif val == "i":
            os.system('cls')
            Player.player_inventory(Player_1)
            input("okej? [Tryck enter].")
            os.system('cls')
            # print(Inventory_beskrivning)
        elif val == "1":
            os.system('cls')
            Player.falla(Player_1)
        elif val =="2":
            os.system('cls')
            Player.strid(Player_1)
        elif val =="3":
            os.system('cls')
            Player.kista_scen(Player_1)
        else:
            os.system('cls')
            print("Välj rätt värde '1', '2, '3', '[b] för att backa', och [s] för att se din nuvarande status") #Funkar inte       

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
    Legender säger att Elliot har aldrig haft någon fru...
============================================================================================= 

===================== 
    Välj ett alternativ: 
=====================
    1) Fortsätt 
    2) Tillbaka till meny
    3) Se din profil
    4) Butik
            """)
                    Players_val2 = input("\n\n")
                    if Players_val2 == "1":
                        os.system('cls')
                        Player_1 = dörrar(Player_1)
                    elif Players_val2 == "2":
                        os.system('cls')
                        return
                    elif Players_val2 == "3":
                        os.system('cls')
                        Player.player_egenskaper(Player_1)
                        input("okej? [Tryck enter].")
                        continue
                        
                    elif Players_val2 == "4":
                        os.system('cls')
                        Butik_items.butik(Player_1)
                               
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
===================================================================
    Välj ett av de alternativen nedan för att gå vidare
===================================================================

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


