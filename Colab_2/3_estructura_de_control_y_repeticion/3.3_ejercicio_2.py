
# Tarifa base de 10€ siempre que no se hable más de 180 minutos al mes.
# A partir de los 180 minutos los usuarios pagan 10 céntimos cada minuto hasta los 240 minutos
# A partir de los 240 minutos los usuarios pagan 20 céntimos cada minuto.

# Pedir los minutos y devolver lo que tienen que pagar

minutos = int(input('Introduce los minutos hablados: '))

pago = 10.0
pagoExtra = 0

if(minutos > 180 and minutos <= 240):
    minExtra = minutos - 180
    pagoExtra = minExtra * 0.10

elif(minutos > 240):
    minExtra = minutos - 240
    pagoExtra = minExtra * 0.20 + 60 * 0.10

print("La tarifa sale por: " + str(pago + pagoExtra) + "€")