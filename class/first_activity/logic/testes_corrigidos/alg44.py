num_par = list()

for i in range(10):
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        num_par.append(num)

print('Os números pares são: ', sorted(num_par))
