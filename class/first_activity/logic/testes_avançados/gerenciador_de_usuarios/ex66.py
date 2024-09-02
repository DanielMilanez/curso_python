# abreviando nomes de modulos
import operations as op

op.hud()
while True:
    entrada = int(input('Digite um valor: ').strip().lower())

    while entrada > 4 or entrada < 0:
        print('Entrada inválida')
        entrada = int(input('Digite um valor: '))

    match entrada:
        case 1:
            op.criar()
            print('Item criado')
            op.listagem()
            op.hud()
        case 2:
            op.atualizar()
            print('Item atualizado')
            op.listagem()
            op.hud()
        case 3:
            op.deletar()
            print('Item deletado')
            op.listagem()
            op.hud()
        case 4:
            break
        case _:
            print('Opição inválida!')
