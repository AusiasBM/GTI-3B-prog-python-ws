

# Realiza un script que genere 10 identificadores de socio aleatoriamente. Un identificador de socio está basado en 3 letras y 2 números del 0 al 9. Si se genera un identificador repetido, tendrá que generarse otro hasta que no salga repetido.

import random

az = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
identificadores = []

for i in range(0, 10):
    ident = random.choice(az) + random.choice(az) + random.choice(az) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    
    while identificadores.count(ident) == 1:
        ident = random.choice(az) + random.choice(az) + random.choice(az) + str(random.randint(0, 9)) + str(random.randint(0, 9))

    identificadores.append(ident)

print(identificadores)
