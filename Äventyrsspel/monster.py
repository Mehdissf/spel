import random
class Monster():
    def __init__(self,namn,HP,STR):
        self.namn=namn
        self.HP=HP
        self.STR=STR
Elliot= Monster("Elliot",100,100)
Hitler= Monster("Hitler",90,110)
Gargamel= Monster("Gargamel", 60,120)

lista =[Elliot, Hitler, Gargamel]
x=lista[random.randint(0,2)]


