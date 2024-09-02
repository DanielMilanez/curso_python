estado_civil = input('Digite seu estado civil: ')

match estado_civil:
    case 'solteiro':
        print('Você está sozinho, arrume alguém, seu perdedor.')
    case 'casado':
        print('Você está casado, vai levar gaia')
    case 'viúvo':
        print('Sinto muito pela sua perda')
    case 'divorciado':
        print('Você levou gaia')
    case _:
        print('Entrada inválida!')
