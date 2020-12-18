from mano import Mano
class Repartidor:
    def __init__(self,mano):
        self.mano=mano
    def ganar(self,valor):
        if(self.mano.evaluar()>=valor):
            return False
        return True
    def recibir(self,carta):
        self.mano.cartas.append(carta)
    def valormano(self):
        return self.mano.evaluar()
    def pedir(self,valor,valor2):
        if valor < valor2 :
            return 0
        else:
            return 1