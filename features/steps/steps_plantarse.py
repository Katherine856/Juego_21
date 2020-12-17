from behave import *
from mano import Mano
from jugador import Jugador

@given('un {mano}')
def step(context,mano):
    # context.jugador=Jugador
    context.mano = Mano(mano.split(";"))

@when('el jugador quiere plantarse')
def step(context):
    context.valor = context.mano.cartas

@then('el {valor:d} de la mano es mayor o igual a 18')
def step(context, valor):
    assert context.valor == True
