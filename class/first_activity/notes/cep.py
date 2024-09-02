# Aprendendo a vincular o codigo em uma API

# Modulo: Importar funções de outro arquivo, que eu mesmo criei.

# Biblioteca: Conjunto de modulos funcionando juntos.

import requests 

# viacep.com.br/ws/01001000/json/ isso é um endpoint de outra API, um ponto de acesso.
cep = 72640000
link = f'https://www.viacep.com.br/ws/{cep}/json/'

resposta = requests.get(link) # busca algo
# post manda uma informação
# delet retira um cep da API
# atualizar put

endereco = resposta.json() # retorna um arquivo json e atribui a uma variável
print(endereco) 

# Todas as vezes que eu faço uma busca em uma API terei um codigo para o retorno. 
# https://http.cat/ mostra a lista de erros
