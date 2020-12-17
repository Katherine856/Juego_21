Feature: Ganador del 21

    Como repartidor quiero saber el valor de las manos para determinar quién gana.

Scenario Outline: Determinar ganador
Given el valor de <manojugador> y el valor de <manorepartidor>
When se determine el ganador
Then <valor> el juego

Examples:
    | manojugador | manorepartidor | valor |
    |  18  |   18  |  ganorepartidor  |
    |  20 |  22  |  ganojugador  |
    |  18  |   20 |  ganorepartidor |
