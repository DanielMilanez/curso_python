# Estruturas de condição e operadores em python

Pesquisa realizada com base na [documentação](https://pythoniluminado.netlify.app/operadores) do site python iluminado.

No python podemos desenvolver programas contando com estruturas condicionais, onde que podemos alterar o fluxo de execução de um programa, então, um programa que antes seguia uma linha reta, pode passar a seguir uma diversidade de caminhos, basta os definir. Essas **estruturas de controle de fluxo**/ **estruturas condicionais** precisam de uma condição para funcionar, onde que essa condição é avaliada como verdadeiro ou falsa. 

# Operadores

Operadores são símbolos especiais capazes de executar computação aritmética ou lógica. Os operadores são usados para realizar operações em variáveis e valores.

Existem diversos tipos de operadores em Python:

- Operadores Aritméticos
- Operadores de Atribuição
- Operadores de Comparação
- Operadores Lógicos
- Operadores de Identidade
- Operadores de Membros
- Operadores Bitwise

Vejamos então como eles funcionam em mais detalhes.

## Operadores de comparação
**Operadores de comparação** são usados para comparar valores. Retornarão verdadeiro ou falso de acordo com a condição.

### Operadores de descrição

| OPERADOR | DESCRIÇÃO | EXEMPLO | RESULTADO |
|:-:|:-:|:-:|:-:|
|>| Maior que |5 > 3|True|
|<| Menor que |5 < 3|Flase|
|==| Igual a |5 == 5|True|
|!=| Diferente de |5 != 3|True|
|>=| Maior que ou igual a |5 >= 5|True|
|<=| Menor que ou igual a|5 <= 3|False|

### Operadores lógicos

Em qualquer linguagem de programação, podemos fazer multiplas verificações em uma única linha verificando se os valores atendem a condição. Os *operadores lógicos* por sua vez, são usados para combinar **comandos condicionais**

| OPERADOR | NOME | EXPLICAÇÃO |
|:-:|:-:|-|
|and| AND |Verifica se **AMBAS** as afirmações são verdadeiras.|
|or| OR |Verifica se **AO MENOS** uma de duas afirmações é verdadeira.|
|not| NOT |**NEGA A AFIRMAÇÃO**, aquilo que era verdadeiro se torna falso e aquilo que era falso se torna verdadeiro.|

```Python
n1, n2, n3 = 3, 6, 7
print(n1 < n2 and n1 < n3) # Resposta: True
print(n1 == n2 or n3 == n2) # Resposta: False
print(not True) # Resposta: False
```
### Operadores de identidade

Operadores de indentidade são usados para **comparar** os objetos, não se são iguais, mas se eles forem realmente **o mesmo objeto**, com o mesmo local de memória.

**IS** e **IS NOT** são operadores de indentidade no python, eles são usados para checar se dois valores (ou variáveis) estão localizados na mesma área de memória, ***duas variáveis iguais não significam que são idêndicas***!

- Exemplo com números:
```Python
x = 1
y = 1 
print(x is y)     # True
print(x is not y) # False
```
- Exemplo com strings:
```Python
a = "cachorro"
b = "cachorro"
print(a is b)      # True
print(a is not b)  # False
```
- Exemplo com listas:
```Python
z = [1,2,3]
k = [1,2,3]
print(z is k)      # False
print(z is not k)  # True
```

# Estrutura de condição IF

A estrutura condicional **IF** pode ser interpretada como SE então para se utiliza-lo pense na lógica "SE caso algo aconteçer, execute o trexo do codigo respectivo a condição".

E podemos executar várias condicionais **IF** para verificar a mesma coisa, como se estivessemos tratando tal coisa como se estivessemos pensando em todas as possíbilidades, por isso usamos o **ELIF** que seria algo como SE caso não aconteça a codicional padrão e minha condição atual esteja valida execute o meu trecho de codigo.

Desta forma conseguimos fazer um "fluxo", o computador irá entender que o trecho que for verdadeiro será executado, e os demais serão ignorados. Então se o primeiro trecho for verdade, os outros não serão executados, tudo por causa do **elif**, mas lembre-se, caso você não coloque elif na expressão o computador irá executar ela independente se a condicional de cima/ anteriores forem verdadeiras ou não.

```Python
number = 1

if number < 1:
    print('O número é MENOR que 1')
elif number > 1:
    print('O número é MAIOR do que 1')
elif number == 1:
    # Está será executada.
    print('O número é IGUAL a 1')

```

Por fim, temos o **SE NÃO** ou **ELSE** que funciona na seguinte lógica, se caso nenhuma das condicionais anteriores for verdadeira, execute o meu trecho de código, aqui, não importa se existem "elif's" ou não mas sim se existe o *IF* pois a estrutura else, so irá funcionar caso a primeira verificação não retornar o valor esperado. Por isso não preciso infomrar uma condição, pois, já está implicito que a condição é se todas as outras forem falsas.

Olhe o exemplo do nosso código anterior mas agora usando o else.

```Python
number = 1

if number < 1:
    print('O número é MENOR que 1')
elif number > 1:
    print('O número é MAIOR do que 1')
else:
    # Está será executada.
    print('O número é IGUAL a 1')

```
---
