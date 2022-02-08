

valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))
valor3 = int(input('Valor 3: '))

if(abs(valor1 - valor2) <= 1 and abs(valor3 - valor1) > 2 and abs(valor3 - valor2) > 2):
    print('Si que se cumplen todas las diferencias')