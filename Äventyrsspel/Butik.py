from Player import *
import os 
# import Äventyrsspel


#Det går inte använda denna funk i spelet vi får lösa det
def butik():
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
        if val_shelf == "3":
            os.system('cls')
            print(""" 
            
  /==========================1
 / : : : : : |::::| : : : : : 1          |===============|
{ : : : : : :|::::|: : : : : : }         |Namn = plåster |
 \ : : : : : |::::| : : : : : /          |Pris = 20$     |
  \==========================/           |HP_bonus = +10 |
                                         |===============|
            """)
            input("jnsidbcbdscbdsc")
            os.system('cls')

        if val_shelf == "4":
            os.system('cls')
            butik()
            return butik()
        else:
            print("Välj rätt siffta")
        return butik() #går inte att kalla på denna funktion från startlistna







