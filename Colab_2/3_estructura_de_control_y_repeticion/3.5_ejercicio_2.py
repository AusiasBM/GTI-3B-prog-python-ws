

import random

puntos = 100
numAleatorio = random.randint(0, 100)
print(numAleatorio)

numUser = int(input('¿Que número crees que es? '))

while numUser != numAleatorio:
    puntos -= 1
    if(numUser < numAleatorio):
        if((numAleatorio % numUser) == 0):
            print("Es multiplo/divisor")
        else:
            print("No es multiplo/divisor")
    elif(numUser > numAleatorio):
        if((numUser % numAleatorio) == 0):
            print("Es multiplo/divisor")
        else:
            print("No es multiplo/divisor")

    numUser = int(input('¿Que número crees que es? '))
    

print("--- PUNTUCACIÓN ---")
print("       " + str(puntos))

