num1 = int(input('Informe o primeiro número: '))
operat = input('Informe a operação: ')
num2 = int(input('Informe o primeiro número: '))

# criando uma função lambda dentro de uma chave de um dicionário.
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

if operat in operations:
    result = operations[operat](num1, num2)
    print(f'Numero {num1} {operations} {num2}, é: {result}')
else:
    print('Operação inválida.')
