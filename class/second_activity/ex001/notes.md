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

## Parte II - Falando sobre a metodos de um dicionário

Durante minha pesquisa descobri alguns métodos e jeitos especificos de se acessar um ***diconário dentro de uma lista***.

Vamos supor a seguinte lista/dicionário:

    alunos = [
        {
            'NOME': 'Daniel'
            'CPF': 00000000000
            'SEXO': 'M'
        },
        {
            'NOME': 'Sarah'
            'CPF': 00000000000
            'SEXO': 'F'
        }
    ]


Assim como uma lista comum, esta lista/dicionário também possui seus indices começando sempre pelo indice zero, para que possamos navegar uma lista, é muito simples basta criar um laço de repetição for e navegar por meio de seus indices usando a função "enumerate".

Ao criar um laço de repeticção com o enumerate o computador entende que o primeiro parametro passado é o indice e o segundo é o valor respectivo ao indice da vez, por exemplo, se estivessemos com o indice zero atualmente receberiamos o parametros do dicionário 0 que contém as informações de Daniel.

Por isso conseguimos acessar um valor expecifico apenas com um único parámetro em um laço de repetição, pois este parametro solitário é o indice. E como se faz para acessar um valor expecifico em uma matriz? primeiro você acessa o indice e depois você acessa o item. De forma similar isso ocorre aqui, mas agora o indice é o "aluno" e o que eu estou acessando é a chave que contém nesse aluno

    for aluno in alunos:
        print(f'{aluno["NOME"]} - {aluno["CPF"]}')


Olhe por exemplo esse trecho de uma função que criei no código do exercício 01:

    def rename(find_aluno, aluno):
        print(f'O aluno {aluno} será atualizado!')

        alunos[find_aluno]['Nome'] = input('Digite o novo nome do aluno:')

O que eu estou fazendo aqui é primeiro passar 2 parametros do usuário para função, esses parámetros são provenientes de uma outra função que é executada antes desta parte e fornece o indice do item selecionado através do parametro **"find_aluno"** com isso eu consigo acessar itens expecificos dentro do dicionário por meio deste parametro que foi repassado para mim, é o que ocorre no trecho: `alunos[find_aluno]['Nome']`.

---