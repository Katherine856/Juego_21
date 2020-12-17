from jugador import Jugador
from mazo import  Mazo
from mano import Mano
from carta import Carta
from repartidor import Repartidor
class Juego:
    def jugar(self):
        mazo=Mazo()
        mazo.barajar()
        listajugador=[]
        listajugador.append(mazo.dar_carta(0))
        listajugador.append(mazo.dar_carta(1))
        manojugador=Mano(listajugador)
        jugador1=Jugador(manojugador)
        listarepartidor=[]
        listarepartidor.append(mazo.dar_carta(2))
        listarepartidor.append(mazo.dar_carta(3))
        manorepartidor=Mano(listarepartidor)
        repartidor=Repartidor(manorepartidor)
        print(manorepartidor.evaluar())
        for i in 48:
            if(jugador1.plantarse()):
                if(repartidor.ganar(jugador1.mano.evaluar())):
                    if(repartidor.mano.evaluar()>=21):
                        print("gana el jugador ")
                    else:
                        print("gana la casa")
                else:
                    listarepartidor.append(mazo.dar_carta(i))
                    manorepartidor(listarepartidor)
                    repartidor(manorepartidor)
            else:
                listajugador.append((mazo.dar_carta(i)))
                manojugador(listajugador)
                jugador1(manojugador)

    def ganador(self,vjuga,vrepa):
        if(vrepa>21 and vjuga<21):
            return "ganojugador"
        if (vjuga==vrepa or vrepa>vjuga):
             return "ganorepartidor"



