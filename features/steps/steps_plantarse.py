from behave import *
from mano import Mano
from jugador import Jugador

@given('un valor de la {mano:d} de un jugador')
def step(context,mano):
    # context.jugador=Jugador
    context.mano = mano
    context.jugador=Jugador("aux")

@when('el jugador quiere plantarse')
def step(context):
    context.valor = context.jugador.plantarse(context.mano)

@then('el valor de la mano es mayor o igual a 18 {valor:d} 0 True 1 False')
def step(context, valor):
    assert context.valor == valor



