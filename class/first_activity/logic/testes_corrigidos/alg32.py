word = input('Digite uma palavra: ').lower().replace(' ', '')
respota = 'Sua palavra é um palindromo!' if word == word[::-1] else 'Sua palavra não é um palindromo'
print(respota)
