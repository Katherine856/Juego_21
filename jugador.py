from mazo import Mazo
from mano import Mano
class Jugador:
    def __init__(self,mano):
        self.mano=mano;

    def plantarse(self):
        if self.mano.evaluar()>=18:
           return True;
        else:
            return False
            # self.pedir(self)
    def pedir(self):
        self.mano.cartas.append()
