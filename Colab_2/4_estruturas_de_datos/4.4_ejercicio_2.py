

# Modifica el script anterior para que repita sólo los 3 primeros caracteres del string. La longitud mínima del string será de 3, si no, el programa mostrará un mensaje y terminará.


texto = "hola"
valor = 5

if len(texto) >= 3:
    print(texto[0:3] * valor)

else:
    print("La longitud del texto es inferior a 3")