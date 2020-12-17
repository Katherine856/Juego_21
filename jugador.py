from mazo import Mazo
from mano import Mano
class Jugador:
    def __init__(self):
        print("entro")


    def plantarse(self,valor):

        if valor >= 18:
           return 0
        else:
            return 1
            # self.pedir(self)
    def pedir(self):
        self.mano.cartas.append()

    def pedir(self,valor):
        if valor < 18:
            return 0
        else:
            return 1
