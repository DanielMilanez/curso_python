# Este � um arquivo Python criado automaticamente.

maior = None
for i in range(5):
    num = int(input('Digite um número: '))
    
    if maior < num or maior is None:
        maior = num

print(f'O maior número digitado foi: {maior}')
