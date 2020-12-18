from jugador import Jugador
from mazo import  Mazo
from mano import Mano
from carta import Carta
from repartidor import Repartidor
class Juego:
    def __init__(self):
        self.mazo=Mazo()
        self.mazo.barajar()
        self.jugador1=Jugador(self.reparto())
        self.repartidor=Repartidor(self.reparto())
    def jugar(self):
        print(self.jugador1.valormano())
        while(self.jugador1.plantarse(self.jugador1.valormano())!=0):
            self.jugador1.recibir(self.mazo.dar_carta(0))
            self.mazo.cartas.pop(0)
        while(self.repartidor.pedir(self.jugador1.valormano(),self.repartidor.valormano())!=0):
            self.repartidor.recibir(self.mazo.dar_carta(0))
            self.mazo.cartas.pop(0)
        print(self.ganador(self.jugador1.valormano(),self.repartidor.valormano()))


    def ganador(self,vjuga,vrepa):
        if(vrepa>21 and vjuga<21):
            return "ganojugador"
        if (vjuga==vrepa or vrepa>vjuga):
             return "ganorepartidor"
    def reparto(self):
        listajugador = []
        listajugador.append(self.mazo.dar_carta(0))
        listajugador.append(self.mazo.dar_carta(1))

        manojugador = Mano(listajugador)
        self.mazo.cartas.pop(0)
        self.mazo.cartas.pop(1)
        return manojugador
juego=Juego()
juego.jugar()

