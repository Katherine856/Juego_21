from behave import *
from mano import Mano
from jugador import Jugador

@given('un valor de la {mano:d} de un jugador')
def step(context,mano):
    # context.jugador=Jugador
    context.mano = mano
    context.jugador=Jugador()

@when('el jugador quiere pedir carta')
def step(context):
    context.valor = context.jugador.pedir(context.mano)

@then('el {valor:d} de la mano es menor a 18')
def step(context, valor):
    assert context.valor == valor
