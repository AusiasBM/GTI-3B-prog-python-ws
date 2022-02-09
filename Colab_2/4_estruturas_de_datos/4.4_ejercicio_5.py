

# Dado un string, muestra por pantalla un nuevo string que sea el original, repitiendo cada caracter dos veces.

texto = "hola"
textoRep = ""

for i in texto:
    textoRep += i*2

print(textoRep)