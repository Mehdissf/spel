from Player import *
import os 
import time

def butik(Player_1):
    os.system('cls')
    Alternativ = ["1","2","3","4"]
    val_shelf = ""
    while val_shelf not in Alternativ:
        print(f"Ditt saldo är {Player_1.pengar}$")
        print("""
===============================================
    Välkommnen till Jamal och brödernas butik!
    Kika på våra fantastiska vapen!
===============================================
===============================================
    Här finnns olika hyllor vilken väljer du? 
===============================================
    1) yxor              3) Medicin 
    2) Skjutvapen        4) tillbaka 
    """)
        val_shelf = input("\n Vad väljer du? ")
        if val_shelf == "1":
            os.system('cls')
            print("""
    Yxor:                               
        /\ 
    //`-||-'1\'
    (|-=||=- |)                          |==================|
    \L,-||-.//                           |Namn = Mehdis Yxa |
    `   ||  '                            |Pris = 200$       |
        ||                               |Strength_bonus = 5|
        ||                               |==================|
        ||  
        ||   
        ||
        ()

            """)
            input("sijdbsovnodnvs")
            os.system('cls')
            return Player_1
        
        if val_shelf == "2":
            os.system('cls')
            print("""
    Skjutvapen:

            _________
            /'        /|
            /         / |_
        /         /  //|                 |====================|
        /_________/  ////|               |Namn = KSP 58       |
        |   _ _    | 8o////|             |Pris = 1000$        |                  
        |   _ _    | 8o////|             |Strength_bonus = +20|   
        | /'// )_  |   8///|             |====================|
        |/ // // ) |   8o///|                
        / // // //,|  /  8//|           
        / // // /// | /   8//|
    / // // ///__|/    8//|
    /.(_)// /// |       8///|
    (_)' `(_)//| |       8////|___________
    (_) /_\ (_)'| |        8///////////////
    (_) \"/ (_)'|_|         8/////////////
    (_)._.(_) d' Hb         8oooooooopb'
    `(_)'  d'  H`b
            d'   `b`b
            d'     H `b
        d'      `b `b
        d'           `b
        d'             `b
           
        |
        
        |======|
            """)
            input("Hjsicndaonca")
            os.system('cls')
            return Player_1

        if val_shelf == "3":
            os.system('cls')
            köp_plåster = input(""" 
            
  /==========================1
 / : : : : : |::::| : : : : : 1          |===============|
{ : : : : : :|::::|: : : : : : }         |Namn = plåster |
 \ : : : : : |::::| : : : : : /          |Pris = 20$     |
  \==========================/           |HP_bonus = +10 |
                                         |===============|
            Vill du köpa?
            1) Köp
            2) Tillbaka
            """)
            
            while True:
                if köp_plåster == "1":
                    if Player_1.pengar < 20:
                        os.system('cls')
                        print("Du har för lågt saldo!!")
                        break
                    else:
                        if Player_1.HP >= ursprungliga_HP:
                            os.system('cls')
                            print(f"Ditt HP får ej överstiga {ursprungliga_HP}")
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
                            input("Tryck enter för att gå vidare")
                            break
                elif köp_plåster == "2":
                    break
                
                else:
                    os.system('cls')
                    print("Skriv rätt!!")
            val_shelf = ""
              
        if val_shelf == "4":
            os.system('cls')
            return Player_1
        else:
            os.system('cls')
            print("Välj rätt siffta")
    
    







