Feature: Jugador pide una carta

    Como jugador quiero pedir una carta

Scenario Outline: pedir carta
Given un valor de la <mano> de un jugador
When el jugador quiere pedir carta
Then el <valor> de la mano es menor a 18

Examples:
| mano | valor |
    | 20  | 1  |
    | 18  | 1  |
    | 17  | 0  |