[voltar](../README.md)

# Aprendendo GIT

Objetivo da aula é ensinar os estudantes aprenderem o básico de git.

## Lista de comandos GIT
| comand | description |
|-|-|
| ***git init*** | Inicia o monitoramento do projeto |
| ***git branch*** -M nome | Alterando o nome da branch |
| ***git status***| Visualizando as atualizações do projeto |
| ***git add .***| Manda os arquivos para a área de staging (em espera) |
| ***git add "nome do arquivo"***| Manda arquivos especificos para a área de staging (em espera) |
| ***git log*** | Vizualizar lista de commits do projeto |
| ***git restore --staged*** | Remove o arquivo da área de staged|
| ***git config --global user.name 'Nome'*** | Configura o nome do operador para o git |
| ***git config --global user.email 'Email'*** | Configura o email do operador para o git 
| ***git config --list*** | Retorna as configurações globais do git |
| ***git commit -m "descrição"*** | Cria um ponto de restauração do projeto |
| ***git checkout "nome da branch"*** | Faz a mudança da branch para a branch ja existente |
| ***git checkout -b "nome da branch"*** | Faz a mudança da branch no projeto criando uma nova e ja fazendo a troca |
| ***git branch***| Mostra a lista de branchs disponíveis |
| ***git branch -m "nome antigo" "nome novo"***| Altera o nome da branch|
| ***git merge***| Mescla as branchs |
| ***git branch -d "nome" ***| Deletar a branch apenas se toda a branch ja tiver sido feita o merg se os arquivos estiverem atualizados|
| ***git branch -D "nome" ***| Deletar a branch ignorando as diferenciações|
| ***git remote add origin "link" ***| Vincular repositório local com o online|
| ***git remote ***| Vereficar a conexção remota|
| ***git push -u origin main*** | Enviando o condigo para a plataforma online |
| ***git pull*** | Atualizando repositório local com o repositório online|


## Anotações gerais

### *Retorno Infinito*

- Quando o git sinaliza com ":" ao demonstrar o retorno de uma linha de comando, e para isso vamos usar um exemplo.

    Suponha a utilização do comando:

    ```
        git log
    ``` 

    Ao utilizar este comando é comum nos depararmos com a situação. Mas isso significa que não houve espaço o bastante para que todas as informações fossem exibidas, para demonstrar as demais informações, basta precionar enter ate que a informação "(END)" seja demonstrada, quando demonstrar, basta clicar na letra "Q" de quit para finalizar a execução do codigo.

### *Controle de Atualizações*

- Cada commit possui uma hash que seria um indentificador dele, tornando possível localiza-los no futuro.

    Nunca devemos enviar commits para a branch principal, pois caso seja enviado uma atualiação que não foi testada ou verificada, pode causar problemas, para isso é necessáro se criar uma ramificação, criando uma brach.

    Novas brachs tendem a ter o nome da feature que está sendo adicionada no programa.

- Eu só consigo navegar entre branchs, SE eu ja tiver "comitado" tudo que deveria ser comitado dentro da branch.

- Ao mesclar branchs a branch que foi mescalada a atual não é deletada!

[voltar](README.md)
