from behave import *
from mazo import Mazo
from jugador import Jugador
from repartidor import Repartidor
from juego import Juego

@given('un mazo barajado')
def implementacion(context):
    context.juego = Juego()
    context.mazo = Mazo()
    context.mazo.barajar()
    print(len(context.mazo.cartas))
    context.aux=len(context.mazo.cartas)


@when('el repartidor entrega 2 cartas')
def implementacion(context):
    context.jugador = Jugador(context.juego.reparto())
    context.repartidor = Repartidor(context.juego.reparto())

@then('el jugador obtiene 2 cartas y el repartidor 2 cartas')
def implementacion(context):
    assert len(context.jugador.mano.cartas)==2
    assert len(context.repartidor.mano.cartas)==2
# @then('la cantidad de cartas en el mazo son 48')
# def implementacion(context):
#     print(len(context.mazo.cartas),context.aux-2)
#     assert  len(context.mazo.cartas) == context.aux-2