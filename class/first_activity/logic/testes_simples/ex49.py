# Este � um arquivo Python criado automaticamente.

count = 0
list_number = []

for i in range(7):
    num = int(input('Digite um número: ')) 

    if num > 40:
        count += 1
        list_number.append(num)

print('=' * 40)
print(f'A quantidade de números maiores do que 40 é: {count}')
print('E os números que são maiores são:', end=' ')

for i in range(len(list_number)):
    print(list_number[i], end=', ')