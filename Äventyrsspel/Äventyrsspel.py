import random
import time
# from Items import *
# from Loot import *
# from Player import *

def cls():
    print("\n" * 70)   
def dörrar():

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
def start():
                startsida_alternativ = ["1", "2","3"]
                Players_val2 = ""
                while Players_val2 not in startsida_alternativ:  #vi kan också skapa en ny funkttion för startsidan istället för att skriva allt här i alternativ 1)
                    cls()
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

            """)
                    Players_val2 = input("\n\n Ange ditt alternativ här: ")
                    if Players_val2 == "1":
                        dörrar()
                    elif Players_val2 == "2":
                        main()







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
                cls()
                start()
        elif Players_val == "3":    #Här kallas der på def hjälplistan()
                hjälplistan()
      
        elif Players_val == "2":    #Spelet avslutas 
                cls()
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
                       
main()






# Monster
# class goblin(object):
#     namn = "Elliot"
#     HP = 10
#     STR = 2
#     DEF = 3