
"""
    Dada una lista de enteros, muestra por pantalla si un número introducido por teclado está en la primera o en la última posición. 
    La longitud mínima de la lista será de 1, en caso contrario, el programa terminará.
"""

lista = [10, 11, 12, 13, 14]

numero = int(input('Dime un número: '))

if lista[0] == numero or lista[-1] == numero:
    print('Si que está')
else:
    print('No está ni en la primera ni en la última')