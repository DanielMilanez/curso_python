# Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.

number_list = []
maior = 0
menor = 0

for repeat in range(5):
    num = int(input(f'Digite o {repeat + 1}° número: '))
    number_list.append(num)

print('A lista númerica é:', end=' ')
for number in range(len(number_list)):
    # Adicionando o maior valor a lista mesmo quando ele for 0
    if maior < number_list[number] or maior == 0:
        maior = number_list[number]
    
    # Adicionando o menor valor a lista mesmo quando ele for 0
    if menor > number_list[number] or menor == 0:
        menor = number_list[number]

    print(number_list[number], end=' ')

print()
print(f'Sendo seu maior valor {maior} e seu menor valor sendo {menor}')