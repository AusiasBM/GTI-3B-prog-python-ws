

# Dada una lista de enteros, mostrar por pantalla si hay algún número que esté repetido en dos posiciones consecutivas.

lista = [11, 11, 7, 9, 9, 7, 2]

ant = -1

for i in lista:

    if i == ant:
        print("Número repetido en dos posiciones consecutivas: ", i)
    
    ant = i