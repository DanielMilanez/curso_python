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
    if (opitions[0] == opitions[1] == opitions[2] or
        opitions[0] == opitions[1] == opitions[2] or
        opitions[0] == opitions[1] == opitions[2]):
        return True
    
    elif (opitions[0] == opitions[3] == opitions[6] or
        opitions[1] == opitions[4] == opitions[7] or
        opitions[2] == opitions[5] == opitions[8]):
        return True
    
    elif (opitions[0] == opitions[4] == opitions[8] or
        opitions[2] == opitions[4] == opitions[6]):
        return True

    else:
        return False