from itertools import combinations


opitions = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def hud():
    for i, value in enumerate(opitions):
        if i == 2 or i == 5 or i == 8:
            print(value)
        else:
            print(value, end=' | ')


def play(jogada, player):
    opitions[jogada] = player


def altern_player(player):
    jogador = player
    if jogador == 'X':
        jogador = 'O'
    else:
        jogador = 'X'
    return jogador


def victory():
    # lista de tuplas é criada com todas as combinações de vitória possíveis
    vicotry_combine = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    # Cada tupla dentro da lista possui um indice e dentro do indice possui uma lista e
    # eu consigo navegar os valores dentro dessa "pequena lista" pela navegação padrão temos que acessar o indice
    # e o outro indice dentro do primeiro.

    # Então ao referenciar o ABC dentro de um for, ele ja entende que será percorrido a lista de maneira implicita
    # e so o que ele faz e pesquisar pelo segundo valor, o valor que está dentro do primeiro indice.
    resposta = any(opitions[a] == opitions[b] == opitions[c]
                   for a, b, c in vicotry_combine)
    return resposta
