dia_semana = ['domingo', 'segunda', 'terça',
              'quarta', 'quinta', 'sexta', 'sábado']

for indice, dia in enumerate(dia_semana):
    print(f'{indice + 1} - {dia}')

dia = int(input('Digite um número de 1 a 7: '))
print(f'O dia que você escolheu foi {dia_semana[dia - 1]}')
