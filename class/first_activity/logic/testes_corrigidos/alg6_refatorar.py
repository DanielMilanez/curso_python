num1 = int(input('Informe o primeiro número: '))
oper = input('Informe a operação (+ - / *): ')
num2 = int(input('Informe o primeiro número: '))

match oper:
    case '+':
        print(f'{num1} {oper} {num2} = {num1 + num2}')
    case '-':
        print(f'{num1} {oper} {num2} = {num1 - num2}')
    case '/':
        print(f'{num1} {oper} {num2} = {num1 / num2}')
    case '+':
        print(f'{num1} {oper} {num2} = {num1 * num2}')
    case _:
        print('Opição inválida')
