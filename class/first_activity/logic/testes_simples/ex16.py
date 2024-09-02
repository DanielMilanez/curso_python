combustivel = input('Digite o tipo de combústivel que você deseja utilizar (gasolina, etanol, disel): ')

match combustivel:
    case 'gasolina': 
        print('O preço pelo litro da gasolina é: R$5,89')
    case 'etanol':
        print('O preço pelo litro do etanol é: R$10,30')
    case 'disel':
        print('O preço pelo litro do disel é: R$6,30')
