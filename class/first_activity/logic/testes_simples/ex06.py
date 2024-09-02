num1 = int(input('Digite o primeiro número para a operação: '))
operation = input('Digite a operação desejada: ')

match operation:
    case '+': 
        num2 = int(input('Digite o segundo número para a soma: '))
        print('=' * 30)
        print(f'O resultado da soma é: {num1 + num2}')
    case '-':
        num2 = int(input('Digite o segundo número para a soma: '))
        print('=' * 30)
        print(f'O resultado da subitração é: {num1 - num2}')
    case '*':
        num2 = int(input('Digite o segundo número para a soma: '))
        print('=' * 30)
        print(f'O resultado da multiplicação é: {num1 * num2}')
    case '/':
        num2 = int(input('Digite o segundo número para a soma: '))
        print('=' * 30)
        print(f'O resultado da divisão é: {num1 / num2}')
