

# Dado un string, muestra por pantalla un nuevo string que tenga los dos últimos caracteres movidos al inicio. La longitud mínima del string será de 2.

texto = "javascript"

if len(texto) >= 2:
    print(texto[-2:] + texto[0:-2])

else:
    print("La longitud del texto es inferior a 2")