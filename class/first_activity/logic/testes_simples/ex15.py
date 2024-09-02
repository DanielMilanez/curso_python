idade = int(input('Digite sua idade: '))

if idade > 13 and idade < 19:
    if idade < 18:
        print('Você é adolecente ainda.')
    else:
        print('Você já é um adulto.')
else:
    print('Idade não permitida.') 
