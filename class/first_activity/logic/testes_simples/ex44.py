list_number = []
for i in range(10):
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        list_number.append(num)

print('Os números pares digitados foram: ')

for number in range(len(list_number)):
    print(list_number[number])