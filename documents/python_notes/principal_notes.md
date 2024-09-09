[voltar](../../README.md)

# Topicos para estudo
- Estudar mais tarde: ***swagger***
- OBS.: Refatoração, quando um sistema já está funcional, mas reescrevemos ele para deixar o codigo mais simples.

# Outras anotações

| NOTES | DESCRIPTION | LINK|
|:-:|:-:|:-:|
|1| CONDICIONAIS E OPERADORES|[Aqui](./conditionals.md)|
|1| LISTAS |[ Aqui](./list.md)|
|2| DICIONÁRIOS |[ Aqui](./notebooks/dicionary.ipynb)|
|3| PARAMETROS |[ Aqui](./parametros.md)|
|4| SWITCHS |[ Aqui](./switchs.md)|
|5| TRATAMENTO DE ERROS |[ Aqui](./erros.md)|
|6| ANY & ALL |[ Aqui](./notebooks/utilidades.ipynb)|

# Anotações gerais python
- O que eu preciso para desenvolver em python? Ter o python e alguma maneira para me comunicar com ele.
    
    Refiro-me com "alguma maneira", pois consigo me comunicar com o python direto do ***CMD*** ou então do ***IDLE*** do próprio python.

- A regra de nomeclatura de python é o snake_case, não podendo haver letras maiúsculas, apenas minusculas e o espaçamento é feito utilizando o "_" (underline)


- A comutação é dividada em 3 eixos!

    ***Entrada***: Informação externa adentrando no programa.

    ***Processamento***: Apos a entrada ele processa a inofrmação.

    ***Saida***: Retorna a resposta do processo executado.

---

- ***Variável***: Espaço na memória RAM que é ocupado com alguma informação.
- ***Operadores aritimeticos***: 

    '+' > (mais) 

    '-' > (menos) 

    '*' > (multiplicação) 

    '/' > (divisão)

    '//' > (divisão inteira)

---

## Estrutura de dados

- É possível utilizar listas, túplas e dicionários em python!

    ***Listas***: São arrays de tamanho dinâmico, declaradas em outras lingaugens, listas não precisam ser homogêneas, o que torna a ferramenta mais poderosa em python.

    ***Túpla***: Uma tupla é uma coleção de objetos python separados por vírgulas. De certa forma, uma tupla é similar a uma lista em termos de indexação, objetos aninhados e repetição, mas uma tupla é IMÚTAVEL, diferente de listas que são mutáveis.

    ***Set***: Um Set é um tipo de dado de coleção não ordenada que é iterável, mutável e não tem elementos duplicados. A classe set do python representa a noção matemática de um conjunto. Não é muito comum encontrar um condigo utilizando o set, entretanto na industria pode sim, haver alguém que esta o utilizando.

    ***Dicionário***: Em python, dicionário é uma coleção ordenada, de valores de dados, usada para armazenar valores de dados como um mapa, que diferentemente de outros tipos de dados que contêm apenas um único valor como elemento, dicionário contém par chave:valor. Chave-valor é fornecido no dicionário para torná-lo mais otimizado. Em outras palavras uma coleção de objetos.

    exemplo: 

        pessoa1{
            nome: 'Daniel'
            idade: 19
        }

    pessoa1 está sendo o nosso dicionário, um dicionário possui 
---

## Versão do interpretador do codigo (criando um ambiente virtual em python)

Útil para o trabalho em equipe. Perguntas da aula, duvidas gerais.

- **o que é um ambiente virtual?** Um ambiente virtual é uma configuração isolada de software que permite que você execute e gerencie projetos e dependências de maneira separada do sistema operacional principal.

- **versões alternativas para não danificar o python padrão?** O ambiente virtual é usado com frequencia no desenvolvimento para garantir que as dependências e configurações de um projeto não conflitem com as de outros projetos ou com o sistema global, caso isso ocorra problemas de compatibilidade podem ocasionar em erros graves no sistema operacional e isso eventualmente ocasionar em uma **perca do sistema**.

Para criar um ambiente virtual em python, primeiro abrimos o terminal e execute o comando, no windows podemos escrever o comando sem o 3 mas em qualquer outro sistema precisa do 3 ao final de python.

- "-m" serve para executar um script python
- o ponto serve para ocultar algum arquivo em qualquer sistema operacional
- primeiro chamamos o modulo venv e informamos o nome do diretorio 

    python3 -m venv .venv 

Criar um ambiente não garante que estamos o utilizando, por isso o ideal é ativalo manualmente. utilize o comando `ctrl + shift + P ---> select interpreter` 

Fora o modo de ir clicando nas opições podemos usar o modo de ativação por meio de linha de código.

Nome das pastas onde fica localizado o scrpit de execução é:
- Scripts >> No Windows
- Bin >> No Mac ou Linux

Primeiro acessamos o diretório `cd ./venv/Scripts/` caso você esteja em um sistema operacional distinto, sendo ele o linux ou mac o comando é `cd ./venv/Bin/` por fim basta usar o comando de ativação `source activate`.

E para desativar o ambiente virtual podemos usar o comando `deactivate`

Existem outros gerenciadores de pacotes python, e dentro desses pacotes consigo gerenciar o ambiente virtual: virtualvenv, conda e venv

Quando estamos trabalhando em equipe precisamos de arquivo requerements usamos para listar todas as ferramentas que estamos utilizando no codigo .

`pip freeze > requirements.txt`

o comando pip freeze vai no modulo do ambiente e tira uma fotografia de todos os modulos e versões do ambiente, para isso eu uso o `> requirements.txt` para que ele pegue essa foto e escreva no novo arquivo que estou adicionando em meu codigo.

Ele pega os modulos instalados tira uma foto e lista todos os modulos que eu tenho e coloca também todas as versões deles.

Agora vamos criar um ambiente e suponto que somos alguém de fora que está acessando o codigo pela primeira vez, vamos baixar todas as dependencias solicitadas no arquivo **requirements.txt** basta utilizar o comando `pip install -r Requirements.txt`

## Gitgnore

Serve para remover o lixo gerado pelos codigos:
- pasta .vscode
- pycaches

Arquivos gerados pela compilação do codigo podem ser considerados lixo. Podemos deixar tudo automatizado para criar um gitgnore com o site [https://www.toptal.com/developers/gitignore/](gitgnore.io)


## PEP 8 Guia de estilos para python code

São regras de escritas e nomeclaturas 
- Segundo esta pep itens separados por uma virgula deve haver espaço
- Entre objetos devem ter um espaço entre e outro deve se separar por duas linhas

faça a instalação do autopep8 (microsoft) `ctrl + shift + p` 
