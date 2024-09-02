num = input('Digite uma cor entre vermelho azul e verde: ').lower()

match num: 
    case 'vermelho':
        print('\033[31m vermelho!\033[m')
    case 'verde':
        print('\033[32m verde!\033[m')
    case 'azul':
        print('\033[34m azul!\033[m')