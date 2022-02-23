
# Escribe una función que reciba el nombre de un fichero que contiene palabras (cada línea tiene una palabra) 
# y que devuelva la palabra que tiene una longitud máxima y su longitud.

def palabraMasLarga(nombreFichero):
    palabra = ""
    longitud = 0
    with open(nombreFichero, mode="rt", encoding="utf-8") as f:
        for pa in f:
            if(len(pa) >= longitud):
                palabra = pa
                longitud = len(palabra)
    return palabra, longitud

palabra, longitud = palabraMasLarga("ejercicio2.txt")

print("Palabra: " + palabra + "Longitud: " + str(longitud))