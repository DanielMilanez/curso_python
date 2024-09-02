modo_de_transporte = input('Selecione o modo de transporte (carro, bicicleta, caminhada)')
print('=' * 30)

match modo_de_transporte:
    case 'carro':
        print('A velocidade média de um carro é: 190km/h')
    case 'bicicleta':
        print('A velocidade média de uma bicicleta pode variar de: 15km/h a 25km/h')
    case 'caminhada':
        print('A velocidade média de uma pessoa caminhando é de 3.6km/h')
