import processamento as pros
from os import system

player = 'O'

# Game
while True:
    # Armando o jogo para o jogador 2
    player = pros.altern_player(player)
    system('clear')
    # Armando jogo para o jogador 1
    jogamos = pros.jogadas(player)

    if jogamos == False:
        break
    