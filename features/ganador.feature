Feature: Ganador del 21

    Como repartidor quiero saber el valor de las manos para determinar quién gana.

Scenario Outline: Determinar ganador
Given una <mano> del jugador
When el repartidor
Then el <valor> es correcto

Examples:
    | mano | valor |
    | (5, picas);(J, treboles)  | 15  |
    | (9, corazones);(A, treboles)  | 20  |
    | (3, diamantes);(Q, picas)  | 13  |
    | (A, picas);(A, treboles)  | 12  |
    | (A, diamantes);(J, treboles)  | 21  |
    | (5, picas);(J, treboles);(3, treboles)  | 18  |
    | (A, picas);(A, treboles);(A, diamantes)  | 13  |
    | (A, picas);(A, treboles);(A, diamantes);(Q, picas)  | 13  |