
# Escribe un programa que genere un fichero de texto con los números del 1 al 5000 y sus cuadrados.

with open("ejercicio1.txt", mode="wt", encoding="utf-8") as f:
    for i in range(1, 5000):
        f.write(str(i) + " => " + str(i*i) + "\n")
        #f.write("Hola\n")