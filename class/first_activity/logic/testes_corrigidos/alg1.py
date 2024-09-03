numeros_extenso = ['um', 'dois', 'três']
num = int(input('Digite um número de 1 a 3: '))


while num < 1 or num > 3:
    print('numero inválido')
    num = int(input('Digite um número de 1 a 3: '))

print(f'Seu número por extenso é: {numeros_extenso[num - 1]}')
