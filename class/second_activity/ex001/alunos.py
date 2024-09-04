from os import system as sys

alunos = [
    {'Matricula': 12345, 'Nome': 'Daniel', 'Idade': 19, 'Sexo': 'M'},
    {'Matricula': 43123, 'Nome': 'Miguel', 'Idade': 22, 'Sexo': 'M'},
    {'Matricula': 13141, 'Nome': 'Samuel', 'Idade': 31, 'Sexo': 'M'},
    {'Matricula': 65471, 'Nome': 'Sarah', 'Idade': 15, 'Sexo': 'F'},
]
opitions_list = ['Cadastrar nome', 'Atualizar nome',
                 'Excluir nome', 'Mais informações', 'Sair']


def selections(slection, matricula):
    match slection:
        case 1:
            try:
                name = input('Insira o nome: ')
                mat = int(input(f'Digite a matricula de {name}: '))
                idade = int(input(f'Insira a idade de {name}: '))
                sexo = input(f'Insira o sexo de {name}: ')

                create_new(name, idade, mat, sexo)
            except ValueError:
                print('\033[31mErro: entrada inválida\033[m, saindo da operação')
        case 2:
            try:
                rename(leitor_matricula(matricula), mostrar_aluno(matricula))
            except ValueError:
                print('\033[31mErro: entrada inválida\033[m, saindo da operação')
        case 3:
            try:
                print('Excluindo aluno...')
                delete(matricula)

            except ValueError:
                print('\033[31mErro: entrada inválida\033[m, saindo da operação')
        case 4:
            print('Carregando informações sobre o aluno selecionado...')
            info(leitor_matricula(matricula))
        case 5:
            return False
    return True


def create_new(name, idade, matricula, sexo):
    alunos.append({'Nome': name, 'Matricula': matricula,
                  'Idade': idade, 'Sexo': sexo})
    opitions()


def rename(find_aluno, aluno):
    print(f'O aluno {aluno} será atualizado!')

    alunos[find_aluno]['Nome'] = input('Digite o novo nome do aluno:')
    alunos[find_aluno]['Matricula'] = int(
        input(f'Insira o número da matricula: '))
    alunos[find_aluno]['Idade'] = int(input(f'Insira a idade: '))
    alunos[find_aluno]['Sexo'] = input(f'Insira o sexo: ')


def opitions():
    sys('cls')
    print('A Academia, lista de alunos')
    print('=' * 30)

    print('Matricula - Nome do aluno')
    for aluno in alunos:
        print(f'{aluno["Matricula"]} - {aluno["Nome"]}')

    print('=' * 30)

    for indice, opition in enumerate(opitions_list):
        print(f'{indice + 1} - {opition}')
    print('=' * 30)


def delete(matricula):
    aluno = leitor_matricula(matricula)
    alunos.pop(aluno)


def leitor_matricula(matricula):
    # Rastreando o aluno a ser removido
    for i, aluno in enumerate(alunos):
        # Caso rastreado ele adiciona o valor do indice a uma variável
        if aluno['Matricula'] == matricula:
            return i
    return -1


def mostrar_aluno(matricula):
    sys('cls')
    for i, aluno in enumerate(alunos):
        # Caso rastreado ele adiciona o valor do indice a uma variável
        if aluno['Matricula'] == matricula:
            print(f'Aluno: {aluno["Nome"]}')


def info(find_aluno):
    sys('cls')

    if 0 <= find_aluno < len(alunos):
        aluno = alunos[find_aluno]
        print(f'Nome: {aluno["Nome"]}')
        print(f'Matrícula: {aluno["Matricula"]}')
        print(f'Idade: {aluno["Idade"]}')
        print(f'Sexo: {aluno["Sexo"]}')
    else:
        print('Nenhum aluno encontrado com a matrícula fornecida.')

    input('Pressione ENTER para continuar')
