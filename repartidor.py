from mano import Mano
class Repartidor:
    def __init__(self,mano):
        self.mano=mano
    def ganar(self,valor):
        while(self.mano.evaluar()<valor):
            return True
        return False
