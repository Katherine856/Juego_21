from behave import *
from mano import Mano
from carta import Carta

@given('una {mano} para sumar sus cartas')
def step(context, mano):
    aux=mano.split(";")
    cartas = []
    for t in aux:
        valor, pinta = t[1:-1].split(",")
        cartas.append(Carta(valor, pinta))
    context.mano = Mano(cartas)

@when('el jugador suma la mano')
def step(context):
    context.valor = context.mano.evaluar()

@then('el {valor:d} es correcto')
def step(context, valor):
    assert context.valor == valor
