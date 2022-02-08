
# 1. Implementa un programa que lea la hora en formato 24 horas y lo convierta a formato 12 horas

hora = int(input('Introduce la hora: '))
minutos = int(input('Introduce los minutos: '))

pm = False

if hora > 12:
    pm = True

    if hora == 13:
        hora = 1
    elif hora == 14:
        hora = 2
    elif hora == 15:
        hora = 3
    elif hora == 16:
        hora = 4
    elif hora == 17:
        hora = 5
    elif hora == 18:
        hora = 6
    elif hora == 19:
        hora = 7
    elif hora == 20:
        hora = 8
    elif hora == 21:
        hora = 9
    elif hora == 22:
        hora = 10
    elif hora == 23:
        hora = 11
    elif hora == 24 or hora == 00 or hora == 0:
        hora = 12
    else:
        print("hora incorrecta")
    
if minutos >= 0 and minutos <= 60:
    if pm:
        print(str(hora) + ":" + str(minutos) + " PM")
    else:
        print(str(hora) + ":" + str(minutos) + " AM")
else:
    print("Minutos incorrectos")