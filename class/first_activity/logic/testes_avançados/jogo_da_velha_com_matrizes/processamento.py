from os import system

# Coordenadas para a verificação
mapeamento = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]

# Desenhando tela
def desenho(player):
    if player == 'X':
        print('É a vez do primeiro jogador!')
    elif player == 'O':
        print('É a vez do segundo jogador!')

    for opition, value in enumerate(mapeamento):
        # Exibindo o tabuleiro de 3 em 3 e mesclando com "|"
        print(' | '.join(mapeamento[opition]))

# Entrada
def jogadas(player):
    desenho(player)

    # Verificar se há um vencedor
    if victory():
        return False

    # Recebendo valores
    leitor_coluna = int(input('Digite o valor da coluna: '))
    leitor_linha = int(input('Digite o valor da linha: '))

    # Condicional para valores excedidos
    while (leitor_coluna > 3 or leitor_linha > 3) or (leitor_coluna < 0 or leitor_linha < 0):
        desenho(player)
        print('\033[31mEntrada inválida\033[m, por favor insira valores adequados. Digite números de 1 a 3')
        leitor_coluna = int(input('Digite o valor da coluna: '))
        leitor_linha  = int(input('Digite o valor da linha: '))

    # Pegando valores das cordenadas X e Y e subitraindo 1 para que eles entrem no range da matriz 0 a 2
    cordenada_y = leitor_coluna - 1
    cordenada_x = leitor_linha - 1

    marcar_jogada(cordenada_x, cordenada_y, player)

# Marcando entrada
def marcar_jogada(cordenada_x, cordenada_y, player):
    if player == 'X' and mapeamento[cordenada_x][cordenada_y] not in ['O', 'X']:
        # Subistituindo valor atual da cordenada expecificada
        mapeamento[cordenada_x][cordenada_y] = 'X'

    elif player == 'O' and mapeamento[cordenada_x][cordenada_y] not in ['X', 'O']:
        # Subistituindo valor atual da cordenada expecificada
        mapeamento[cordenada_x][cordenada_y] = 'O'
        
    else:
        system('clear')
        print('\033[31mJogada inválida\033[m, esse espaço está preenchido!')
        jogadas(player)

# Condição de vitória
def check_winner(player):
    return (
        # Vereficando se qualquer uma das linhas está retornando os 3 valores como verdadeiro
        any(all(mapeamento[i][j] == player for j in range(3)) for i in range(3)) or  
        any(all(mapeamento[i][j] == player for i in range(3)) for j in range(3)) or  
        all(mapeamento[i][i] == player for i in range(3)) or  
        all(mapeamento[i][2 - i] == player for i in range(3)))

def altern_player(player):
    jogador = player
    if jogador == 'X':
        jogador = 'O'
    else:
        jogador = 'X'
    return jogador

def victory():
    if check_winner('X'):
        print('Fim de jogo! O jogador 1 ganhou!')
        return True
    elif check_winner('O'):
        print('Fim de jogo! O jogador 2 ganhou!')
        return True
    return False
