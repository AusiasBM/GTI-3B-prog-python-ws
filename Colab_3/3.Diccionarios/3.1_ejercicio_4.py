

# Escribe un programa que lea un texto por teclado. 
# Posteriormente debe crear un diccionario donde las claves sean las palabras del texto y sus valores el número de apariciones de cada una de éstas en el texto. 
# Muestra el resultado por pantalla.


textoTeclado = str(input("Inserta un texto: "))

dic = {}

i = 0;
for word in textoTeclado.split(" "):
    dic[word] = i
    i += 1

print( dic )