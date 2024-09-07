# Pandas: O guia de sobrevivência

O Pandas é uma biblioteca muito utilizada para trabalhar com dados. Com ela, podemos fazer diversas operações. Mas, antes de começar, é necessário instalar o Pandas e importá-lo. Para isso, use o comando: `import pandas as pd`.

O Pandas funciona com **dataframes**. Dataframe é uma tabela dentro do Python. Sempre que trabalhamos com dados em geral no Python, utilizamos dataframes.

Exemplo de **dataframe** (tabela)

<img src="../../assets/img/dataframe_exemple.png" alt="imagem da logo do python" width="65%">

---
Com tudo isso exclarecido, vamos começar. A primeira coisa que você precisa entender é que existem 3 formas de criar um **dataframe**.

## Primeira: criando um dataframe vazio:
```python
df_vendas = pd.DataFrame()
```
Embora seja possível criar desta forma, é mais comum se deparar com dataframes que, assim que são criados, já possuem valores.

Uma dica: para diferenciar das demais variáveis, ao criar uma variável que seja um dataframe, sempre coloque o prefixo `df`.

## Segunda: criando um dataframe a partir de um dicionário:
```python
# Primeiro, criamos um dicionário.
venda = {
    'data': ['15/02/2021', '16/02/2021'],
    'valor': [500, 300],
    'produto': ['feijão', 'arroz'],
    'qntde': [50, 70]
}

# Em seguida, atribuimos o dicionário a um dataframe 
df_vendas = pd.DataFrame(venda)
```
## Terceira: importando um arquivo como base de dados
Neste método, importamos um dataframe a partir de uma base de dados. Para fazer isso, é necessário ter um arquivo `.xlsx.`:

```python
df_vendas = pd.read_excel("Vendas.xlsx")
```

O que está entre aspas é a localização do arquivo. No meu caso, ele está no mesmo local do código que estou executando, por isso não preciso especificar o caminho completo do arquivo.

## Médodos para vizualização de dados

### Head
- head: mostra apenas as 5 primeiras linhas por padrão, mas você consegue alterar a quantidade de linhas mostradas adicionando um número dentro do parenteses. 

```python
# mostra 5 linhas por padrão.
print(df_vendas.head())
# mostra 10 linhas
print(df_vendas.head(10))
```
### Shape
- shape: mostra quantas linhas e colunas existem na tabela.
```python
print(df_vendas.shape)
```
### Describe
- describe: mostra as colunas númericas e mostra um resumo de toda a sua tabela. 
```python
print(df_vendas.describe())
```

## Médodos para edição de um dataframe

### Puxar informações de uma coluna na tabela
O primeiro passo é criar uma variável e em seguida atribuir o valor da variável local do seu dataframe, em seguida expecificar a coluna que deseja entre ***conchetes***. 

Lembrando que quando vc puxa uma única coluna de seu dataframe a variável que irá recebe-la não será um dataframe mas sim uma ***Series*** do panda. Entenda que cada coluna em uma tabela é uma ***Series*** do pandas.

É possível puxar vários valores de colunas distintas no mesmo comando, so que, ao invés de passar o nome de uma única coluna, você irá informar uma lista de valores.

```python
# Puxando informações de uma única coluna
produtos = df_vendas['Produto']
# Puxando informações de várias colunas
produtos = df_vendas[['Produto', 'ID Loja']]
```

- OBS.: Quando existe mais de uma coluna é uma tabela, quando existe uma única coluna é uma **Series**, o mesmo vale para linhas.

### Puxar informações de uma linha de uma tabela

Nesta parte irémos nos aprofundar um pouco mais em métodos para poder obter informações de uma linha, este é o método **.loc**.

Com este método você pode: 
- pegar uma única linha:
```Python
# Pegar uma linha, ele sempre trabalha com os indices.
# Em nosso exemplo ele vai pegar as informações da linha com indice 1
# OBS.: Isso é uma Series.
print(df_vendas.loc[1])  
```

Aqui podemos também puxar informações de várias linhas, como se estivessemos demonstrando para o computador que queremos informações de uma linha X ate uma linha Y, para isso usamos os `:` para indicar ate onde vai.

```Python
# Pegando valores de 1 linha ate outra determinada. OBS.: Isso é uma tabela.
print(df_vendas.loc[1:5])  
```

- pegar linhas de acordo com uma condição: 
```Python
print(df_vendas.loc[df_vendas['ID Loja'] == df_vendas['Norte Shopping']])  
```
Aqui estamos passando uma condição para que todas as linhas de uma determinada coluna seja demonstrada. Para isso precisamos verificar se o item da coluna possui o valor que desejamos, caso possua ele "printa".

Você também pode armazenar esses valores obtidos em uma variável. E essa seria uma variável de dataframe também.
```Python
df_vendas_noshopping = df_vendas.loc[df_vendas['ID Loja'] == df_vendas['Norte Shopping']] 
```

- pegar linhas e colunas expecíficas:

Ao passar uma única informação dentro do loc, ele apenas vai procurar pelas linhas, so que no loc ele tambem permite você procurar por linhas e colunas, então seria algo como: `df_vendas.loc[linhas, colunas]`

Isso significa que podemos pegar mais de uma coluna exibindo linhas expecificas dessa coluna.
```Python
# pegando várias linhas e colunas com base em um valor expecífico.
df_vendas_noshopping = df_vendas.loc[['ID Loja'] == df_vendas['Norte Shopping'], ['ID Loja', 'Produto', 'Quantidade']] 
print(df_vendas.loc[1])  
```
- pegar um valor específico:
Digamos que desejamos extrarir o valor "camiseta" de nosso **dataframe** para isso precisamos expecificar a linha que este item está e o nome da coluna que desejamos acessar.

```Python
# Método .loc infromando ao computador a linha | coluna para retornar o item.
print(df_vendas.loc[1, 'Produto'])  
```