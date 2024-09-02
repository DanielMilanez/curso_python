## Parametros

Parâmetros Opcionais: Parâmetros opcionais são valores que você pode ou não passar para uma função. Eles têm um valor padrão predefinido, mas você pode escolher fornecer um valor diferente se quiser. É como quando você vai a um restaurante e o garçom pergunta se você quer batatas fritas com seu hambúrguer. As batatas fritas são opcionais - você pode pedir com ou sem elas.

Funções com parametros infinitos. Essas são funções podem receber parametros inderteminados.
- parametro não nomiar: nominal posicional quando mando apenas um valor sem uma expecificação 
- paremetro nomial: quando mando valores com expecificações

Funções recursivas. Essas são funções que chamam a si mesma durante sua execução

Exemplo: 
```
    def calcula_fatorial(numero):
        if numero == 0 or numero == 1:
            return 1
        else:
            return numero * calcula_fatorial(numero - 1)
```

Parâmetros nomeados: Parâmetros nomeados/nomial permitem que você passe valores para uma função especificando explicitamente o nome do parâmetro ao qual o valor se refere. Isso pode tornar seu código mais legível, pois mostra claramente qual valor é atribuído a cada parâmetro.

```
    def mostrar_info(nome, idade):
        print("Nome:", nome)
        print("Idade:", idade)

    mostrar_info(nome="Ana", idade=30)  # Passando valores usando parâmetros nomeados
```

Parâmetros não-noeados: São eles o inverso dos nomeados, pois eles não expecificam explicitamente o nome do parâmetro ao qual o valor se refere.