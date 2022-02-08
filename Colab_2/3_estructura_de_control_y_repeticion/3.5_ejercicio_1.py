

# Factorial de un numero entero

numero = int(input('Dime el número: '))

factorial = 1

while numero != 1:
    factorial = numero * factorial
    numero = numero - 1

print('Factorial: ' + str(factorial))