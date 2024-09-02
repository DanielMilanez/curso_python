from os import system

nomes = ['Daniel', 'Miguel', 'Samuel', 'Rodrigo']
opitions = ['Cadastrar nome', 'Atualizar nome', 'Excluir nome', 'Sair']

def hud():
    for indice, opition in enumerate(opitions):
        print(f'{indice + 1} - {opition}')
    print('=' * 30)

def listagem():
    system('clear')
    print('=' * 8)
    for idice, value in enumerate(nomes):
        print(f'{idice}: {value}')
    print('=' * 8)

def criar():
    print('Lista de itens existentes')
    listagem()
    val = input('Digite o item a ser criado: ').strip().capitalize()     
    nomes.append(val) 

def deletar():
    print('Lista de itens disponiveis para deleção')
    listagem()
    val = int(input('Digite o valor da unidade para deleção: ').strip().capitalize())
    nomes.pop(val)

def atualizar():
    listagem()
    val = int(input('Digite o indice do item a ser atualizado: '))        
    atualizado = input(f'Digite o valor para atualizar no item {nomes[val]}: ').strip().capitalize()
    nomes[val] = atualizado
