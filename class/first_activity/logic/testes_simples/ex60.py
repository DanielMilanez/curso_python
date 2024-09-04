# Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.

num = int(input('Digite um número: '))
print('Os divisores deste número são:', end=' ')

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=' ')
