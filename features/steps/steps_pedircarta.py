from behave import *
from mano import Mano
from jugador import Jugador
from repartidor import Repartidor

@given('un valor de la {mano:d} de un jugador y un repartidor {manor:d}')
def step(context,mano,manor):
    # context.jugador=Jugador
    context.mano = mano
    context.mano2 = manor
    context.repartidor=Repartidor("aux")


@when('el repartidor quiere pedir carta')
def step(context):
    context.valor = context.repartidor.pedir(context.mano,context.mano2)


@then('el {valor:b} de la mano es menor a la del jugador')
def step(context, valor):
    assert context.valor == valor
