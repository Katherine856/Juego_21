Feature: Repartidor pide una carta

    Como Repartidor quiero solicitar una carta adicional para seguir jugando
Scenario Outline: pedir carta
Given un valor de la <mano> de un jugador y un repartidor <manor>
When el repartidor quiere pedir carta
Then el <valor> de la mano es menor a la del jugador

Examples:
| mano | manor | valor |
    | 20  | 18 |  1|
    | 18  | 18 | 1|
    | 17  | 16  |1  |
    | 18| 20  |0 |