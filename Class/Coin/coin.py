import random
class Coin:
    #class attribute
    HEAD = 0
    TAIL = 1
    def __init__(self, face):
        #instance attribute
        self.__face = face

    def flip(self):
        flip = random.randint(0,1)
        self.__face = flip

    def get_face(self):
        return self.__face

    def __str__(self):
        if self.__face == 0:
            return "Tura"
        else:
            return "Yazi"



coin_1 = Coin(Coin.HEAD)
print(coin_1)

coin_2 = Coin(Coin.TAIL)


