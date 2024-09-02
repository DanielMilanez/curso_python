# Criar um sistema de cadastro de alunos
import alunos as est
from time import sleep as slp

selection = True

while selection == True:
    slp(.5)
    try:
        est.opitions()
        selection = int(input('Digite o valor da operação: '))

        if selection != 5 and selection != 1:
            matricula = int(input('Digite o número da matricula: '))
            selection = est.selections(selection, matricula)
        else:
            selection = est.selections(selection, None)

    except ValueError:
        print('\033[31mErro\033[m: entrada inválida. Por favor, digite um número.')
