from mazo import Mazo
from mano import Mano
class Jugador:
    def __init__(self,mano):
        self.mano=mano
    # def recibirinicio(self,carta):
    #     pass

    def plantarse(self,valor):
        if valor >= 18:
           return 0
        else:
            return 1
            # self.pedir(self)
    def recibir(self,carta):
        self.mano.cartas.append(carta)



    def valormano(self):
        return self.mano.evaluar()

