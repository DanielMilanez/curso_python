gas = [{'nome': 'gasolina', 'valor': 6.50},
       {'nome': 'etanol', 'valor': 4.45},
       {'nome': 'disel', 'valor': 4.45}]

for indice, combustivel in enumerate(gas):
    print(f'{indice + 1} - {combustivel["nome"]}')

opit = int(input('Digite o tipo de combustivel: '))
print(f'O valor por litro de {gas[opit - 1]["nome"]} é: {gas[opit - 1]["valor"]}')
