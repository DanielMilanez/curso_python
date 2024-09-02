import velha_func as vf
player = 'X'

# Game
while True:
    vf.hud()
    marca = int(input('Onde deseja jogar? '))
    vf.play(marca, player)
    player = vf.altern_player(player)