import random
import time
import os
# from Items import *
# from Loot import *
from Player import *
os.system('cls')

from monster import *

def fälla_scen():
    os.system('cls')
    print("""
============================================================================
Du har hamnat i helvetet(borås) nu på grund av alla dina oförlåtna synder
============================================================================
    """
    #Spelaren ska hinna med att skriva någonting väldigt fort för att kunna överleva från fällan ------>>
    #splearen dör/förlorar HP beroende av typ av fälla
    #Fälllor ska slumpvis lottas ut vid varje gång 
    
    )
def monster_scen():
    os.system('cls')
    print("""
=================================================================
Du hitta nu ett mörkt läskigt rum med ett fasansfullt monster
=================================================================
    """)
    print(f'Monstret heter{monster.namn}')        
    print(f'Styrka {monster.STR}')
    print(f'HP {monster.HP}')
    
def kista_scen():
    os.system('cls')
    print("""
=======================================    
Denna dörr leder dig till guldkista
=======================================
    """)
    
def dörrar():
    os.system('cls')
    print("""
============================================
Välj en av dörrarna nedan för att gå vidare: 
============================================
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
    while True:
        val = input("Vilken dörr väljer du??")
        val = random.randint(1, 3)
        if val == 1:
            fälla_scen()
        elif val =="2":
            monster_scen()
        elif val =="3":
            kista_scen()
        else:
            os.system('cls')
            print("Välj rätt siffra '1', '2' eller '3'")
            
        return

# def bakom_dörrar():
    # val = input("1, 2 eller 3: ")

    # if val == "1":
    #     random.lista(kista, fälla, monster)
    #     print(f"Du träffade {listan} och förlorade 10 hp")
    #         if Player.HP < Monster.HP:
    #             print("Knas monstret har jämnt ut dig med marken")
    #         elif Player.HP > Monster.HP:
    #             print("Yayyyy boyyyy du vann GRATTIS")
    # # elif val == "2": 
    #     random.lista(kista, fälla, monster)
    #     print(f"du har hamnat med{}")
    #         #Playern får endast ta tre items
    #         # Vid användning av item så ska den öka PLayers HP, STR eller DEF beroende av vilken egenskap item har
    # elif val == "3":
    #     print(f" du har hamnar i rum 3 och möter nu {}")
    #     random.lista(kista, fälla, monster)
    #         if Player.HP < Fälla: 
    #             print("Du dog vila i frid min broder")
    #         elif Player.HP > Fälla: #Här ska fällan minska Players HP 
        


        
def start():
                startsida_alternativ = ["1","2","3"]
                Players_val2 = ""
                while Players_val2 not in startsida_alternativ:  #vi kan också skapa en ny funkttion för startsidan istället för att skriva allt här i alternativ 1)
                    os.system('cls')
                    print("""       
===========================================================================================
    Det är nu sommaren år 2050.                                                                            
    Du och din familj för att ha det kul och gå på semester, 
    åker till Borås för att besöka Elliot som har sedan år 2030 varit bosatt i Borås.                              
    Han bor tillsammans med sina tre moderlösa barn. 
    Informantion om vad det är som hänt med barnens mödrar är ett mysterium och ingen har än idag förstått det. 
    Legender säger att Elliot har aldrig haft någon fru.... Men hur fick han de där tre barnen då??? 
    Ingen vet det.. Skitsamma låt oss gå vidare nu..... 
============================================================================================= 

===================== 
    Välj ett alternativ: 
=====================
    1) Fortsätt 
    2) Tillbaka till meny
    3) Profil

            """)
                    Players_val2 = input("\n\n Ange ditt alternativ här: ")
                    if Players_val2 == "1":
                        os.system('cls')
                        dörrar()
                        return
                        
                        
                    elif Players_val2 == "2":
                        os.system('cls')
                        main()
                    elif Players_val2 == "3":
                        os.system('cls')
                        print(f"HP {Player_1.HP}")
                        print(f"Styrka {Player_1.STR}")
                        print(f"Level {Player_1.LVL}")
                        input("Tryck enter för att fortsätta.")
                        os.system('cls')

                        return
                    return

def main():
    # time.sleep(0.75)  Vi måte fördröja fraserna
    while True:
        Players_val = ""
        print('''
==================================================================     
 Hej och välkomna till äventyrsspelet skapat av Mahdi och Elliot------>>>> 
===================================================================
==========================================
    Välj ett av de alternativen nedan 
==========================================

            1) Starta spelet 
            2) Lämna spelet 
            3) Hjälp
            
            ''')
 
        Players_val = input("\n \n Ange ditt alternativ här: ")
        if Players_val =="1":    #Här kallas på def star()
                os.system('cls')
                start()
        elif Players_val == "3":    #Här kallas der på def hjälplistan()
                os.system('cls')
                hjälplistan()
      
        elif Players_val == "2":    #Spelet avslutas 
                os.system('cls')
                print("""
===============
    Hej dååå!!
===============
                """)
                break
        else:
            print("""
================================================================================================================
    OBS!!!! 
    Du får endast skriva in siffrorna "1", "2", "3" för att gå vidare så skriv in rätt nu tack HAJJJWAAANN!!!
================================================================================================================
                """)
                       
main()





