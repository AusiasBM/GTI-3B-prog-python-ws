
# Dado un string, muestra por pantalla un nuevo string que sea 3 copias de los últimos dos caracteres del string original. Lo longitud mínima del string será de 2, si no, el programa mostrará un mensaje y terminará.

texto = "hola"
valor = 3

if len(texto) >= 2:
    print(texto[-2:] * valor)

else:
    print("La longitud del texto es inferior a 2")