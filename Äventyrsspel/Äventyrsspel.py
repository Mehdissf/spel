import random
import time
import os
# from Items import *
# from Loot import *
from Butik import *
from Player import *
from monster import *
from fälla import *
os.system('cls')


#Mehdi : jag är inte helt klar med detta vi får jobba på det senare
def fälla_scen():
    os.system('cls')
    fälllistan = [Lava, Helvete,Spökhus]
    random.choice(fälllistan)
    print(f"""
============================================================================
Du har hamnat i{fälllistan} nu i Boräs på grund av alla dina oförlåtna synder
============================================================================


    """)
    #Spelaren ska hinna med att skriva någonting väldigt fort för att kunna överleva från fällan ------>>
    #splearen dör/förlorar HP beroende av vilken typ av fälla
    #Fälllor ska slumpvis lottas ut vid varje gång 
    print("För att komma undan denna fälla så ska skriva så snabbt som möjligt det ordet som dykes upp nu")
    time.sleep(0,3)
    LVL1_ord = ["Hej", "Teknik", "Ellior", "Mehdi"]
    ord = random.choice(LVL1_ord)
    starttid = time.time()
    hej = print("Du har 3 sekunder på dig att skriva ordet: {} \n" .format(ord))
    
    while time.time() - starttid > 3 or hej != ord:
        print(f"Tiden är ute nu du förlorade{Fälla.skada}")
        print(f"Ditt HP nu är {Player_1.HP - Fälla.skada}")
        if Player_1.HP == 0 or Player_1.HP < 0:
                print("Vila i frid min broder")
        starttid = time.time()
    print("Bra jobbat!! Du kom undan fällan")
    print("Varsågod!! Du får 20$ pris")  #Här behövs det att 20$ ska läggas till de pengar spelaren har :)
    
def monster_scen():
    os.system('cls')
    print("""
=================================================================
Du hittade nu ett mörkt läskigt rum med ett fasansfullt monster
=================================================================
    """)
    print(f"OObbsiii du har stött på ett monstret{Elliot.namn} han är en farlig varelse och här nedan ser du hans status")
    time.sleep(0,1)
    print(f'Monstret heter{Elliot.namn}')        
    print(f'Styrka {Elliot.STR}')
    print(f'HP {Elliot.HP}')  
def kista_scen():

    os.system('cls')
    print("""
=======================================    
Denna dörr leder dig till guldkista
=======================================
    """) 

#En utgång till dörr funktionen behövs så spelaren kan backa till start funktionen
#Jag (Mehdi) har försökt lösa det men lcykades inte vi får fixa det senare
def dörrar():
    
    while True:
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
        print("""OBS! Det kan antingen finnas ett monster/ en fälla eller en kista bakom dörrarna
        
        Tillbaka till förra sidan [b]
        """)
        val = input("Ditt val: ")
        val = random.randint(1, 3)
        if val == "1":
            fälla_scen()
        elif val =="2":
            monster_scen()
        elif val =="3":
            kista_scen()
        elif val == "b": # funkar inte
            start()
        else:
            os.system('cls')
            print("Välj rätt värde '1', '2, '3' eller 'b'") #Funkar inte       
def start():
                startsida_alternativ = ["1","2","3","4"]
                Players_val2 = ""
                while Players_val2 not in startsida_alternativ:  
                    os.system('cls')
                    print("""       
===========================================================================================
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
                        dörrar()
                    elif Players_val2 == "2":
                        os.system('cls')
                        main()
                    elif Players_val2 == "3":
                        os.system('cls')
                        print(f"HP {Player_1.HP}")
                        print(f"Styrka {Player_1.STR}")
                        print(f"Level {Player_1.LVL}")
                        print(f"Dina pengar {Player_1.pengar}$")
                        input("okej? [Tryck enter].")
                        start()
                        os.system('cls')
                    elif Players_val2 == "4":
                        os.system('cls')               #Det är ett grovt allvarligt problem här 
                        butik()           
                    else: 
                        print("Skriv rätt siffra ")
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
 
        Players_val = input("\n Ange ditt alternativ här: ")
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
            os.system('cls')
            print("""


================================================================================================================
    OBS!!!! 
    Du får endast skriva in siffrorna "1", "2", "3" 
    för att gå vidare 
    Så skriv in rätt nu tack 
    HAJJJWAAANN!!!
================================================================================================================
                """)
                       
main() 


