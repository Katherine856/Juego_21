from behave import *
from mano import Mano
from jugador import Jugador
from juego import Juego

@given('el valor de {manojugador:d} y el valor de {manorepartidor:d}')
def step(context,manojugador,manorepartidor):
    # context.jugador=Jugador
    context.mano = manojugador
    context.mano2=manorepartidor
    context.juego=Juego()

@when('se determine el ganador')
def step(context):
    context.valor = context.juego.ganador(context.mano,context.mano2)

@then('{valor} el juego')
def step(context, valor):
    assert context.valor == valor

