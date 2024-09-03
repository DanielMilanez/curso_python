meses_ano = {
    "Primavera": ["Março", "Abril", "Maio"],
    "Verão": ["Junho", "Julho", "Agosto"],
    "Outono": ["Setembro", "Outubro", "Novembro"],
    "Inverno": ["Dezembro", "Janeiro", "Fevereiro"]
}


def mostra_estacao():
    for estacao, meses in meses_ano.items():
        if opit in meses:
            return estacao
    return "Mês não encontrado"


opit = input('Digite o mês: ').capitalize()
result = mostra_estacao()

print(f'A estação deste mês de {opit} é: {result}')
