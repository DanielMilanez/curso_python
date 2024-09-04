# Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.

number_list = list()
soma = int()

for i in range(5):
    num = int(input(f'Digite o {i}° número: '))
    number_list.append(num)

print('Os números da lista são:', end=' ')
for i in range(len(number_list)):
    soma += number_list[i]
    print(number_list[i], end=' ')

print()
print(f'A soma total de todos os valores presentes na lista é: {soma}')