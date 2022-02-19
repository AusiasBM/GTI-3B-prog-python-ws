

# Implementa la siguiente función generadora:

def suma_tiempos(inicio, fin, incremento):
    """Función que devuelve tuplas de tiempo (hh,mm,ss) desde una hora inicial hasta una hora final 
    Args: inicio (hh,mm,ss), fin (hh,mm,ss), incremento (segundos)
    Returns: hora (hh,mm,ss)
    """
    
    hora = inicio[0]
    minutos = inicio[1]
    segundos = inicio[2]

    while fin[0] != hora and fin[1] != minutos and fin[2] != segundos:
        if (segundos + incremento) >= 60:
            if minutos >= 60:
                minutos = 0
                hora += 1
            else:
                minutos += 1

            segundos = 0
        else:
            segundos += 1
        

        yield hora, minutos, segundos

tuplaInicio = ( 14, 24, 58 )
tuplaFin = ( 14, 25, 3 )


manegador = suma_tiempos( tuplaInicio, tuplaFin )
