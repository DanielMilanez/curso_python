from random import randint
from os import system

def sorteio(select_tema):
    system('clear')
    frutas = ['melancia', 'pessego', 'manga', 'pera', 'morango']
    animais = ['porco', 'cabra', 'galinha', 'vaca', 'baleia']
    cep = ['barcelona', 'bugaria', 'argelhia', 'armenia', 'brasil']

    sorteio = randint(0, 5)
    palavra = None

    if select_tema == 'frutas':
        palavra = frutas[sorteio]
        return palavra

    elif select_tema == 'animais':
        print('Você escolheu Animais')
        palavra = animais[sorteio]
        return palavra

    elif select_tema == 'cep':
        print('Você escolheu CEP!')
        palavra = cep[sorteio]
        return palavra

    else:
        return False

# Hud
print('=' * 30)
print('Temas existentes', end=' ')
print('\n - Animais \n - CEP \n - Frutas')
print('=' * 30)

# Question
palavra_chave = input('Digite o tema: ').lower()
palavra_chave = sorteio(palavra_chave)

while palavra_chave == False:
    print('=' * 30)
    print('Temas existentes', end=' ')
    print('\n - Animais \n - CEP \n - Frutas')
    print('=' * 30)

    palavra_chave = input('\033[31mTema inválido\033[m, digite um tema: ').lower().strip()
    palavra_chave = sorteio(palavra_chave)

print('=' * 30)

# Game
vida = 6
letra_digitada = []
contador_de_tentativas = 0

while True: 
    for letra in palavra_chave:
        if letra in letra_digitada:
            print(letra, end=' ')
        else:
            print('_', end=' ')

    tentativa = input('Seu palpite: ').lower()
    letra_digitada.append(tentativa)

    # Caso erre o palpite da letra
    if tentativa not in palavra_chave:
        print('Você ERROU, tente novamente.')
        print(f'Você possui {vida} vidas')
        print('=' * 30)
        vida -= 1
    
    # Caso zere as vidas
    if vida <= 0:
        print(f'Você perdeu, você não conseguiu adivinhar a palavra correta, ela era {palavra_chave}')
        break
    
    # Caso acerte a palavra chave
    if tentativa == palavra_chave:
        print('=' * 30)
        print(f'\033[33mVocê ganhou!\033[m Em {contador_de_tentativas} tentativas!')
        break
    
    contador_de_tentativas += 1
    