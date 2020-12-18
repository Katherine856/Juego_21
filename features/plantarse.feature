Feature: Jugador se planta

    Como jugador quiero plantarme para finalizar el turno

Scenario Outline: plantarse
Given un valor de la <mano> de un jugador
When el jugador quiere plantarse
Then el valor de la mano es mayor o igual a 18 <valor> 0 True 1 False

Examples:
| mano | valor |
    | 20  | 0  |
    | 18  | 0  |
    | 17  | 1  |
