Feature: repartir 2 cartas

    Como repartidor quiero repartir 2 cartas al jugador y a si mismo

Scenario: repartir
Given un mazo barajado
When el repartidor entrega 2 cartas
Then el jugador obtiene 2 cartas y el repartidor 2 cartas


