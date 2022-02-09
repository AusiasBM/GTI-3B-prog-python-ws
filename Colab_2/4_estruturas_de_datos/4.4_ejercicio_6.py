

# Dados dos strings, muestra por pantalla la cantidad de veces que el segundo string aparece en el primero.

texto1 = "el perro de ramon ramirez no tiene rabo"
texto2 = "r"

veces = 0

for i in texto1:
    if i == texto2:
        veces += 1
    
print(veces)