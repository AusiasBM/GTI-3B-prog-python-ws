

from tokenize import String


diaSemana = int(input('De que dia quieres saber la alarma entre 1 y 7: ' ))
vacaciones = str(input('¿Estas de vacaciones contesta s(si), n(no)? '))
alarma = '8:00'

if(vacaciones == 's' and diaSemana <= 5 or vacaciones == 'n' and diaSemana >= 6):
    alarma = '10:00'
elif(vacaciones == 's' and diaSemana >= 6):
    alarma = 'Apagada'

print('Ese dia la alarma es o está: ' + alarma)