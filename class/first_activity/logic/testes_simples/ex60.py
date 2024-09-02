# Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.

num = int(input('Digite um número: '))
print('Os divisores deste número são: ')

for i in range(num):

    if num % (i + 1) == 0:
        print(i + 1, end=' ')
