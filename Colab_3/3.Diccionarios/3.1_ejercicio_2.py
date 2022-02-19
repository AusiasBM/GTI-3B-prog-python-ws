

# Escribe una función que reciba un diccionario y una lista de palabras. 
# La función debe devolver un nuevo diccionario con los items del diccionario 
# cuyas claves correspondan a alguna de las palabras de la lista. Muestra el resultado por pantalla.


def cambiarClavesDic( dic, list ):

    num = 0

    for i in dic:
        print(dic[i])
        #dic[list(num)] = dic[i].pop()
        #num += 1


dic = { 'usuario1': 23, 'usuario7': 10, 'usuario2' : 4 }
nombres = ["Pepe", "alfonso", "ana", "pedro", "juan", "pepito", "Toni"]

print( dic )

cambiarClavesDic(dic, nombres)

print( dic )
