

estilo1 = int(input('Estilo de vestir suyo: '))
estilo2 = int(input('Estilo de vestir de su compañero: '))

if(estilo1 >= 8 and estilo2 != 2 or estilo2 >= 8 and estilo1 != 2):
    print('Si hay mesa')
else:
    print('No se sabe si habrá mesa')