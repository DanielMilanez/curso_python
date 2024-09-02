# Listas

- Eu consigo utilizar um método dentro da lista para que se possa adicionar itens a minha lista.
```
    lista.append(valor_a_ser_adicionado)
```
- Strings também são considerados como listas para o python, a lista é um conjunto de caracteres.
    
- Eu consigo utilizar o metodo split() para poder recortar as palavras de uma frase e separa-los em uma lista.

---

Paradigma da programação: é a metodologia que uma linguagem possui, o python por sua vez pode assumir qualquer tipo de paradigma.

Sendo eles:
1. Orientado a objetos
2. Funcional
3. Estruturado

Função lambida -> É uma função anonima que executa o que ela foi feita para fazer, ela não possui um nome, pois, ela é atribuida a uma variável que pode ser utilizada pelo sistema.

```
    exemplo = lambida a_value, b_value: # Digite o codigo aqui.
    print(exemplo)
```

Vamos para uma pratica!

```
    soma = lambida a_value, b_value: a_value + b_value
    print(soma(10, 5))
```
O resutado será 15.



## Metodos de listas

Eu consigo acessar um elemento e alterar o valor dele dentro de uma lista, supondo que não temos a informação do indice o que estamos fazendo usamos o metodo index para encontrar a primeira ocorrencia com este elemento que desejamos alterar.

|Codigo|Funcionalidade|
|-|-|
|append| adicione um elemento ao final |
|extend| extende a lista com os novos elementos|
|insert| insere elementos em uma posição especifica|
|remove| exclui um elemento da lista|
|pop| exclui o último elemento da lista por padrão, mas podemos expecificar para excluir um elemento expecifico|
|index| retorna o indice da primeira ocorrencia de um valor procurado |
|cout| contabilizando quantidade de elementos repetidos |
|sort| ordena a lista de maeira crescente (numerica ou alfabetica) |
|del| deleta um idice expecifico da lista ou ela toda se um indice não for expecificado. (**Codigo legado**) |


OBS.: Arquivos notebooks rodam python, mas também ele serve como documentação pois ele aceita markdown, a extenção é: ***ipynb*** ele é usado para analise de dados, pois ele analisa pedaço por pedaço do codigo.

Feito para relatorio, analise ou estudo.

Composto por celulas, blocos onde podemos adicionar um codigo python ou codigo markdown


## Matrizes

Uma matriz é uma lista dentro de outra, onde que podemos ficar intercalando entre o indice da lista primaria para navegar nas sub-listas existentes
        
Suponha uma matriz:

        numero = [[1, 2, 3], [4, 5, 6]]
    
Cada um desses indices 0 e 1 estão separados por uma virgula e dentro desses indices existe uma lista. E independente de ser uma tupla ou um dicionário eu consigo acessar os parametros dentro dessa lista e consigo navegar por eles.