import random
class Monster():
    def __init__(self,namn,HP,STR,figur):
        self.namn=namn
        self.HP=HP
        self.STR=STR
        self.figur =figur



    def monster_egenskaper(self):
        print(f"Du har stött på monstret {self.namn}, han är en farlig varelse och här nedan ser du hans status")
        print(f"""{self.figur}""") 
        print(f'Monstrets namn {self.namn}')        
        print(f'Styrka {self.STR}')
        print(f'HP {self.HP}')



Elliot_figur = """
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
"""

Borat_figur = """ 
      @@@@@@@@@
      | ^   ^ |
     @ (o) (o) @
      |   <   |
      |  ===  |
      | \___/ | 
       \_____/
     ____|  |____
    /    \__/    1
   /      ()      1
  /\_/|  /  \  |\_/1
 / /  |  \  /  |  \ 1
( <   |   \/   |   > )
 \ \  |        |  / /
  \ \ |________| / /
   \ \|        |/ /
"""
Gargamel_figur = """ 
        .-----.
       /       1
   __ /   .-.  .1
  /  `\  /   \/  1
  |  _ \/   .==.==.
  | (   \  /____\__1
   \ \      (_()(_()
    \ \            '---._
     \                   \_
  /\ |`       (__)________/
 /  \|     /\___/
|    \     \||VV
|     \     \|,
|      \     ____)
\       \  /`
        \(
"""

Elliot= Monster("Elliot", 100, 45, Elliot_figur )
Borat= Monster("Borat", 90, 60, Borat_figur )
Gargamel= Monster("Gargamel", 60, 35, Gargamel_figur )






print("")