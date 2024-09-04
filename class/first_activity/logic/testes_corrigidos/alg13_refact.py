# Primeiro passo é criar um dicionário e dentro das chaves adicionar uma lista respectiva

meses_ano = {
    "Primavera": ["Março", "Abril", "Maio"],
    "Verão": ["Junho", "Julho", "Agosto"],
    "Outono": ["Setembro", "Outubro", "Novembro"],
    "Inverno": ["Dezembro", "Janeiro", "Fevereiro"]
}

# Criando uma função para que possamos reutiliza-la em outras partes do código
def mostra_estacao():
    # Copiando o dicionário para a memória (as chaves)
    # ao fazer o for em um dicionário, diferente de uma lista o indice e o valor se torna a chave e o valor respectivo
    for estacao, meses in meses_ano.items():
        # se a opição digitada estiver dentro de meses ou seja os valores dentro das chaves estações
        if opit in meses:
            # retorne a estação correspondente ao mês
            return estacao
    # caso contrário retorne uma mensagem de erro
    return "Mês não encontrado"

# capitalizando a entrada do usuáiro para que os valores que estão dentro do dicionário sejam lidos de maneira correta
opit = input('Digite o mês: ').capitalize()
result = mostra_estacao()

print(f'A estação deste mês de {opit} é: {result}')
