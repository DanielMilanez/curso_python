num = int(input('Digite um número: '))

# condicional ternária, consigo fazer o if e else em uma linha apenas
resposta = 'seu número é maior ou igual a 10' if num > 10 or num == 10 else 'seu número é menor do que 10'
print(resposta)
