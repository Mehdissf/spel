import random
class Monster():
    def __init__(self,namn,HP,STR,figur):
        self.namn=namn
        self.HP=HP
        self.STR=STR
        self.figur =figur 

Elliot_figur = ["""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMM
MMMMMMMMMMMMWNK0kxddddxkO0XWMMMMMMMMMMMM
MMMMMMMMWKxl;'...,,;;,,'...,cd0NMMMMMMMM
MMMMMWKd;.   ,oOXNWWWWWX0xc.  .'lONWMMMM
WMMWXo.    'kNMMMMMMMMMMMMW0c.   .;OWWWM
MMW0,     :KMMMMMMWWWMMMMMWWNd.    .oNWM
MW0'     ;KMMMMMMMMMMMMMMMMMWWd.    .oNM
MX:     .kMMMMMMMMMMMMMMMMMMMMX:     .kM
Mk.     ;XMMMMMMMMMMMMMMMMMMMWMx.     lW
Mx.     lWMMMMMMMMMMMMMMMMMMMMMO'     :N
Mx.     lWMMMMMMMMMMMMMMMMMMMWMO.     :N
MK,     cNMMMMMMMMMMMMMMMMMMMMMx.     dM
MWd.    .OMMMMMMMMMMMMMMMMMMWMNc     ;KM
MMNl.    :XMMMMMMMMMMMMMMMWMMWx.    ,0WW
MMMNx.    cXMMMMMMMMMMMMMMMWWk.   .cKMMM
MMMWWKo'   ,xXWMMMMMMMMMMMW0c.  .:ONMMWM
O0WWWMWXkl,..'l0MMMMMMMMNx;..':dKWMWWMXk
:.xKNWWWWWNKd. lWMMMMMMMO..c0XWWWWWNKO:'
c  .',;;;;,;,. :XMMMMMWMx. .;,;,,,,'.. .
l              ,KMMMMMMMo              .
x,'''''''''''''lKMMMMMMWx,'''''''''''''c
WWNNWNWWWWWWWWWWWMMMMMMMWNNWWNWWWWWNNWWW
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
"""]

Hitler_figur = [""" 
      *********
      | ^   ^ |
     @ (o) (o) @
      |   <   |
      |  #### |
      |  ___  | 
       \_____/
     ____|  |____
    /    \__/    1
   /              1
  /\_/|        |\_/1
 / /  |        |  \ 1
( <   |        |   > )
 \ \  |        |  / /
  \ \ |________| / /
   \ \|
"""]
Gargamel_figur = [""" 
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
|      \     ______)
\       \  /`
        \(
"""]

Elliot= Monster("Elliot",100,100,Elliot_figur)
Hitler= Monster("Hitler",90,110,Hitler_figur)
Gargamel= Monster("Gargamel",60,120,Gargamel_figur)

lista =[Elliot, Hitler, Gargamel]
valt_monster = lista[random.randint(0,2)]


