class Monster():
    def ___init__(self,namn,HP,STR):
        self.namn=namn
        self.HP=HP
        self.STR=STR



m = Monster("Elliot", 100, 100)
martin = Monster("Martin", 10, 10)

print(martin.HP)

martin.HP = martin.HP -5
