

# Dados dos strings, muestra por pantalla un mensaje indicando si uno de los dos aparece al final del otro, ignorando diferencias de mayúsculas y minúsculas. Por ejemplo, el string "AbC" y "HiaBc" debería mostrar que si que aparece uno al final del otro.

texto1 = "AbC"
texto2 = "HiaBc"

textoMin1 = texto1.lower()
textoMin2 = texto2.lower()




if len(textoMin1) > len(textoMin2):
    if textoMin2 == textoMin1[-len(textoMin2):]:
        print('Si que aparece uno al final del otro')
elif len(textoMin1) < len(textoMin2):
    if textoMin1 == textoMin2[-len(textoMin1):]:
        print('Si que aparece uno al final del otro')
elif len(textoMin1) == len(textoMin2):
    if textoMin1 == textoMin2:
        print('Si que aparece uno al final del otro')