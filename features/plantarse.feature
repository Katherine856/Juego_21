Feature: Jugador se planta

    Como jugador quiero plantarme para finalizar el turno

Scenario Outline: plantarse
Given una <mano>
When el jugador quiere plantarse
Then el <valor> de la mano es mayor o igual a 18

Examples:
| mano | valor |
    | (9, corazones);(A, treboles)  | 20  |
