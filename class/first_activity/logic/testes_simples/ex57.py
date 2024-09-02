# Este � um arquivo Python criado automaticamente.
from random import randint
import time

numero = randint(1, 10)
print('=' * 30)
print('Você consegue adivinhar o número que estou pensando??')
print('=' * 30)

print('Estou pensando em', end='')
time.sleep(1)
print('.', end='')
time.sleep(1)
print('.', end='')
time.sleep(1)
print('.')

entrada = int(input('Digite seu palpite: '))
tentativas = 0

while entrada != numero:
    print('ERROU!')
    if entrada < numero:
        print('O numero em que pensei é maior do que o número digitado')
    elif entrada > numero:
        print('O número em que pensei é menor do que o número digitado')

    entrada = int(input('Digite seu palpite: '))
    tentativas += 1

print(f'\033[32mPARABÉNS VOCÊ ACERTOU! em {tentativas} tentativas \033[m')