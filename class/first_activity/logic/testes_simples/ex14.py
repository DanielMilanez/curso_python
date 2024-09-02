num1 = int(input('Digite o valor do primeiro número: '))
num2 = int(input('Digite o valor do segundo número: '))

soma = num1 + num2

if (soma > 100):
    print(f'A soma entre {num1} + {num2} é {soma} ou seja é maior do que 100!')
else:
    print(f'A soma entre {num1} + {num2} é {soma} ou seja é MENOR do que 100!')
