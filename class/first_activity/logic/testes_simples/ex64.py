from random import randint
number_list = []

for i in range(10):
    number = randint(1,100)

    if number % 3 == 0:
        number_list.append(number)

for i in range(len(number_list)):
    print(f'Os númros digitados multiplos de 3 são: {i}')