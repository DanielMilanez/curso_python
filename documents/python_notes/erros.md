# Anotações de pesquisa

## Parte I - Falando sobre a estrutura de controle try

Enquanto estava realizando a atividade número 1 da segunda lista de exercícios senti que precisava me infromar sobre novos recursos do próprio python que acredito que o professor não tenha mencionado na aula de dicionários.

O prímeiro é o fato de conseguir utilizar uma nova estrutura de controle de fluxo que ajuda DEMAIS para o tratamento de erros.

- **try**: Seria algo como o **if** que vemos comumente em qualquer lógica de controle de fluxo. Nele o fluxo funciona da seguinte forma, primeiro o programa irá efetuar uma tentativa de executar o codigo, caso algo aconteca de maneira indesejada, o programa irá para outra condicional, evitando o erro.

- **except**: Seria esta "outra" condicional que acabo de me referir, é aqui onde "tratamos" o erro de maneira geral.

- **else**: Assim como na estrutura if, o else seria uma contra partida, uma exceção direta do try caso tudo ocorra como o esperado, caso não ocorra erros, o codigo irá pular a etapa anterior e virá direto para cá.

- **finaly**: Aqui é onde o codigo irá executar sempre, sem pular ou ignorar este trecho.

Exemplo de utilização do try, vamos tentar dividir um número por zero.
```
a = 10
b = 0

try:
	print(a/b)

# Aqui no except temos uma coletania de erros que podem acontecer no seu código, e cada um deles espera que um erro ocorra.
# No nosso caso vamos verificar se a divisão por zero está realmente sendo feita.

except ZeroDivisionError as error:
	print(error)

else:
	print('Sem erros')

finally:
	print('Aqui sempre vai printar')

```
Na documentação do python você consegue acessar mais informações sobre erros dos mais variádos tipos. [documentação](https://docs.python.org/3/library/exceptions.html).

---

